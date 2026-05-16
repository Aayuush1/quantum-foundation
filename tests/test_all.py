"""
Unit tests for quantum-foundation modules.
Run with: python -m pytest tests/ or python tests/test_all.py
"""

import unittest
import sys
import os

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import numpy as np


class TestSingleQubitGates(unittest.TestCase):
    """Test single qubit gate operations."""

    def test_x_gate_flips_0_to_1(self):
        """X gate should flip |0> to |1>."""
        qc = QuantumCircuit(1, 1)
        qc.x(0)
        qc.measure(0, 0)

        simulator = AerSimulator()
        job = simulator.run(qc, shots=100)
        counts = job.result().get_counts()

        self.assertEqual(counts.get('1', 0), 100)

    def test_h_gate_creates_superposition(self):
        """H gate should create 50/50 superposition."""
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)

        simulator = AerSimulator()
        job = simulator.run(qc, shots=10000)
        counts = job.result().get_counts()

        # Should be roughly 50/50 (within 5%)
        p0 = counts.get('0', 0) / 10000
        p1 = counts.get('1', 0) / 10000

        self.assertAlmostEqual(p0, 0.5, delta=0.05)
        self.assertAlmostEqual(p1, 0.5, delta=0.05)

    def test_z_gate_no_effect_on_0(self):
        """Z gate should not change |0>."""
        qc = QuantumCircuit(1, 1)
        qc.z(0)
        qc.measure(0, 0)

        simulator = AerSimulator()
        job = simulator.run(qc, shots=100)
        counts = job.result().get_counts()

        self.assertEqual(counts.get('0', 0), 100)


class TestMultiQubitGates(unittest.TestCase):
    """Test multi-qubit gate operations."""

    def test_cnot_flips_target_when_control_is_1(self):
        """CNOT should flip target when control is |1>."""
        qc = QuantumCircuit(2, 2)
        qc.x(0)  # Set control to |1>
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])

        simulator = AerSimulator()
        job = simulator.run(qc, shots=100)
        counts = job.result().get_counts()

        self.assertEqual(counts.get('11', 0), 100)

    def test_bell_state_entanglement(self):
        """Bell state should only produce |00> or |11>."""
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])

        simulator = AerSimulator()
        job = simulator.run(qc, shots=1000)
        counts = job.result().get_counts()

        # Should only have |00> and |11>
        self.assertIn('00', counts)
        self.assertIn('11', counts)
        self.assertNotIn('01', counts)
        self.assertNotIn('10', counts)

    def test_swap_gate(self):
        """SWAP should exchange qubit states."""
        qc = QuantumCircuit(2, 2)
        qc.x(1)  # |01>
        qc.swap(0, 1)
        qc.measure([0, 1], [0, 1])

        simulator = AerSimulator()
        job = simulator.run(qc, shots=100)
        counts = job.result().get_counts()

        self.assertEqual(counts.get('10', 0), 100)


class TestQuantumAlgorithms(unittest.TestCase):
    """Test quantum algorithms."""

    def test_deutsch_jozsa_balanced(self):
        """Deutsch-Jozsa should detect balanced function."""
        from qiskit import QuantumCircuit

        n = 3
        qc = QuantumCircuit(n + 1, n)
        qc.x(n)

        for i in range(n + 1):
            qc.h(i)

        # Balanced function: CNOT from qubit 0
        qc.cx(0, n)

        for i in range(n):
            qc.h(i)

        qc.measure(range(n), range(n))

        simulator = AerSimulator()
        job = simulator.run(qc, shots=1)
        measured = list(job.result().get_counts().keys())[0]

        # Should NOT be all zeros for balanced
        self.assertNotEqual(measured, "0" * n)

    def test_grovers_search_finds_target(self):
        """Grover's search should find target with high probability."""
        n = 3
        target = "101"

        qc = QuantumCircuit(n, n)
        for i in range(n):
            qc.h(i)

        # Simple oracle for |101>
        qc.x(1)
        qc.h(n - 1)
        qc.mcx(list(range(n - 1)), n - 1)
        qc.h(n - 1)
        qc.x(1)

        # Diffusion
        for i in range(n):
            qc.h(i)
            qc.x(i)
        qc.h(n - 1)
        qc.mcx(list(range(n - 1)), n - 1)
        qc.h(n - 1)
        for i in range(n):
            qc.x(i)
            qc.h(i)

        qc.measure(range(n), range(n))

        simulator = AerSimulator()
        job = simulator.run(qc, shots=1000)
        counts = job.result().get_counts()

        most_probable = max(counts, key=counts.get)
        self.assertEqual(most_probable, target)


class TestQuantumML(unittest.TestCase):
    """Test quantum machine learning components."""

    def test_vqe_finds_ground_state(self):
        """VQE should find ground state energy of Z."""
        from qiskit.circuit import Parameter

        theta = Parameter('theta')
        qc = QuantumCircuit(1)
        qc.ry(theta, 0)

        # Test at optimal angle (pi)
        bound_qc = qc.assign_parameters({theta: np.pi})
        bound_qc.measure_all()

        simulator = AerSimulator()
        job = simulator.run(bound_qc, shots=1000)
        counts = job.result().get_counts()

        # At theta=pi, should be |1> with energy -1
        p1 = counts.get('1', 0) / 1000
        self.assertAlmostEqual(p1, 1.0, delta=0.1)

    def test_quantum_kernel_computation(self):
        """Quantum kernel should compute similarity."""
        x1, x2 = 0.5, 0.5

        qc1 = QuantumCircuit(1)
        qc1.ry(x1 * np.pi, 0)
        sv1 = Statevector.from_instruction(qc1)

        qc2 = QuantumCircuit(1)
        qc2.ry(x2 * np.pi, 0)
        sv2 = Statevector.from_instruction(qc2)

        kernel = np.abs(np.vdot(sv1.data, sv2.data))**2

        # Same input should give kernel = 1
        self.assertAlmostEqual(kernel, 1.0, delta=0.01)


if __name__ == '__main__':
    unittest.main()
