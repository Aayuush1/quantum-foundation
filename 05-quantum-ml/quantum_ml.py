"""
============================================================
05 - QUANTUM MACHINE LEARNING
============================================================
This module explores the intersection of quantum computing and ML.

What is Quantum ML?
------------------
Quantum ML uses quantum computers to enhance machine learning tasks.
This can mean:
- Faster training using quantum algorithms
- Quantum feature maps for better data representation
- Quantum neural networks as ansatze

Current Status:
--------------
QML is still in early research stages. "Quantum advantage" for ML
has not been definitively demonstrated yet, but it's a very active
area of research!
"""

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import os
import matplotlib.pyplot as plt
import numpy as np


def vqe_demo():
    """Demonstrate VQE for finding ground state energy."""
    print("=" * 60)
    print("5.1 VARIATIONAL QUANTUM EIGENSOLVER (VQE)")
    print("=" * 60)

    theta = Parameter('theta')

    qc = QuantumCircuit(1)
    qc.ry(theta, 0)

    print("Ansatz: RY(theta)|0>")
    print("Goal: Find theta that minimizes <psi|Z|psi>")

    best_energy = float('inf')
    best_theta = 0

    thetas = np.linspace(0, 2*np.pi, 100)
    energies = []

    simulator = AerSimulator()

    for t in thetas:
        bound_qc = qc.assign_parameters({theta: t})
        bound_qc.measure_all()

        job = simulator.run(bound_qc, shots=1000)
        counts = job.result().get_counts()

        p0 = counts.get('0', 0) / 1000
        p1 = counts.get('1', 0) / 1000
        energy = p0 - p1

        energies.append(energy)

        if energy < best_energy:
            best_energy = energy
            best_theta = t

    print(f"\nOptimization results:")
    print(f"  Best theta: {best_theta:.4f} rad ({np.degrees(best_theta):.1f} degrees)")
    print(f"  Best energy: {best_energy:.4f}")
    print(f"  True ground state energy: -1.0")
    print(f"  Accuracy: {abs(best_energy - (-1)):.4f}")

    plt.figure(figsize=(10, 6))
    plt.plot(thetas, energies, 'b-', linewidth=2)
    plt.axhline(y=-1, color='r', linestyle='--', label='True Ground State')
    plt.axvline(x=best_theta, color='g', linestyle='--', label=f'Best theta = {best_theta:.2f}')
    plt.xlabel('Theta (radians)')
    plt.ylabel('Energy')
    plt.title('VQE Energy Landscape')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(os.path.dirname(__file__), "..", "assets", "vqe_energy_landscape.png"), dpi=150, bbox_inches='tight')
    plt.close()

    print("\n[OK] Saved energy landscape plot to assets/vqe_energy_landscape.png")
    print("-> VQE finds the ground state by classical optimization of quantum parameters!\n")


def qnn_demo():
    """Demonstrate a simple quantum neural network."""
    print("=" * 60)
    print("5.2 QUANTUM NEURAL NETWORK (QNN)")
    print("=" * 60)

    theta1 = Parameter('theta1')
    theta2 = Parameter('theta2')

    qc = QuantumCircuit(2)
    qc.ry(theta1, 0)
    qc.cx(0, 1)
    qc.ry(theta2, 1)

    print("QNN Architecture:")
    print("  Input: |00>")
    print("  Layer 1: RY(theta1) on qubit 0")
    print("  Layer 2: CNOT(0, 1)")
    print("  Layer 3: RY(theta2) on qubit 1")
    print("  Output: Measure qubit 1")

    print("\nCircuit diagram:")
    print(qc.draw('text'))

    print("\n-> QNNs can be trained using gradient descent")
    print("-> Gradients are computed using the parameter-shift rule")
    print("-> Current challenge: Barren plateaus in training landscapes\n")


def feature_map_demo():
    """Demonstrate a quantum feature map."""
    print("=" * 60)
    print("5.3 QUANTUM FEATURE MAP")
    print("=" * 60)

    x, y = 0.5, 0.3

    qc = QuantumCircuit(2)
    qc.ry(x * np.pi, 0)
    qc.ry(y * np.pi, 1)
    qc.cx(0, 1)
    qc.rz((x * y) * np.pi, 1)

    print(f"Classical data point: ({x}, {y})")
    print("Feature map circuit:")
    print(qc.draw('text'))

    sv = Statevector.from_instruction(qc)
    print(f"\nQuantum state: {sv.data}")
    print(f"Amplitudes: {np.abs(sv.data)**2}")

    print("\n-> Classical data is encoded into quantum amplitudes")
    print("-> The quantum state lives in a 2^n dimensional Hilbert space")
    print("-> This high-dimensional representation might help classification\n")


def qaoa_demo():
    """Demonstrate QAOA for Max-Cut on a simple graph."""
    print("=" * 60)
    print("5.4 QUANTUM APPROXIMATE OPTIMIZATION (QAOA)")
    print("=" * 60)

    beta = Parameter('beta')
    gamma = Parameter('gamma')

    qc = QuantumCircuit(2)

    qc.h(0)
    qc.h(1)

    qc.cx(0, 1)
    qc.rz(gamma, 1)
    qc.cx(0, 1)

    qc.rx(beta, 0)
    qc.rx(beta, 1)

    print("QAOA Circuit for Max-Cut:")
    print("  Graph: 2 nodes, 1 edge")
    print("  Goal: Find partition that maximizes cut")
    print(qc.draw('text'))

    print("\n-> QAOA alternates between problem and mixer Hamiltonians")
    print("-> Parameters are optimized classically")
    print("-> Good for NP-hard optimization problems\n")


def quantum_kernel_demo():
    """Demonstrate a quantum kernel."""
    print("=" * 60)
    print("5.5 QUANTUM KERNEL METHOD")
    print("=" * 60)

    def feature_map(x):
        qc = QuantumCircuit(1)
        qc.ry(x * np.pi, 0)
        return qc

    x1, x2 = 0.3, 0.7

    qc1 = feature_map(x1)
    qc2 = feature_map(x2)

    sv1 = Statevector.from_instruction(qc1)
    sv2 = Statevector.from_instruction(qc2)

    kernel = np.abs(np.vdot(sv1.data, sv2.data))**2

    print(f"Quantum Kernel K({x1}, {x2}) = {kernel:.4f}")

    classical_kernel = x1 * x2
    print(f"Classical Linear Kernel = {classical_kernel:.4f}")

    print("\n-> Quantum kernels may provide advantages for certain datasets")
    print("-> Used in quantum support vector machines (QSVM)")
    print("-> Still an active area of research!\n")


if __name__ == "__main__":
    print("\n" + "[M]" * 30)
    print("QUANTUM FOUNDATIONS: QUANTUM MACHINE LEARNING")
    print("[M]" * 30 + "\n")

    vqe_demo()
    qnn_demo()
    feature_map_demo()
    qaoa_demo()
    quantum_kernel_demo()

    print("=" * 60)
    print("[OK] ALL QUANTUM ML DEMOS COMPLETE!")
    print("=" * 60)
    print("\nKEY TAKEAWAYS:")
    print("* VQE: Hybrid algorithm for finding ground state energies")
    print("* QNN: Parameterized circuits as neural networks")
    print("* Feature maps: Encode classical data into quantum states")
    print("* QAOA: Quantum algorithm for combinatorial optimization")
    print("* Quantum kernels: Similarity measures via quantum circuits")
    print("* QML is promising but still in early research stages")
