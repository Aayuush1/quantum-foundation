"""
============================================================
06 - QUANTUM SIMULATION
============================================================
This module uses quantum computers to simulate quantum systems.

Why Simulate Quantum Systems?
----------------------------
Classical computers struggle to simulate quantum systems because
the state space grows exponentially with the number of particles.

A quantum computer with n qubits can naturally simulate a quantum
system with n particles (in principle).

This was Richard Feynman's original motivation for quantum computing!
"""

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np


def harmonic_oscillator_demo():
    """Demonstrate quantum harmonic oscillator energy levels."""
    print("=" * 60)
    print("6.1 QUANTUM HARMONIC OSCILLATOR")
    print("=" * 60)

    n_levels = 4

    print(f"Simulating {n_levels} energy levels of harmonic oscillator")
    print("Energy levels: E_n = (n + 1/2) * hbar * omega")
    print()

    for n in range(n_levels):
        energy = (n + 0.5)
        print(f"  n = {n}: E_{n} = {energy:.1f} * hbar * omega")

    print()
    print("-> On a real quantum computer, we'd prepare these states")
    print("-> and measure their properties")
    print("-> This is crucial for quantum chemistry calculations!\n")


def ising_model_demo():
    """Demonstrate simulation of the Ising model."""
    print("=" * 60)
    print("6.2 ISING MODEL")
    print("=" * 60)

    J = 1.0
    h = 0.5

    print(f"2-qubit Ising model:")
    print(f"  J = {J} (coupling)")
    print(f"  h = {h} (external field)")
    print()

    qc = QuantumCircuit(2)

    if J > 0:
        print("Ferromagnetic case (J > 0):")
        print("  Ground state: spins aligned (|00> or |11>)")
        qc.h(0)
        qc.cx(0, 1)
    else:
        print("Antiferromagnetic case (J < 0):")
        print("  Ground state: spins anti-aligned (|01> or |10>)")
        qc.x(0)
        qc.h(0)
        qc.cx(0, 1)

    print(qc.draw('text'))

    sv = Statevector.from_instruction(qc)
    print(f"\nStatevector: {sv.data}")

    print("-> Ising model is used to study magnetism and phase transitions")
    print("-> Quantum simulation can find ground states of larger systems\n")


def tunneling_demo():
    """Demonstrate quantum tunneling concept."""
    print("=" * 60)
    print("6.3 QUANTUM TUNNELING")
    print("=" * 60)

    qc = QuantumCircuit(1)

    print("Initial state: particle on left side of barrier")

    tunneling_amplitude = 0.1
    dt = 0.1
    num_steps = 50

    for _ in range(num_steps):
        qc.rx(2 * tunneling_amplitude * dt, 0)

    print(f"Simulated tunneling for t = {num_steps * dt}")
    print(qc.draw('text'))

    sv = Statevector.from_instruction(qc)
    prob_left = abs(sv.data[0])**2
    prob_right = abs(sv.data[1])**2

    print(f"\nProbability on left:  {prob_left:.4f}")
    print(f"Probability on right: {prob_right:.4f}")

    print("-> Particle has tunneled through the barrier!")
    print("-> Classically impossible, but quantum mechanically allowed\n")


def h2_molecule_demo():
    """Demonstrate H2 molecule ground state estimation."""
    print("=" * 60)
    print("6.4 H2 MOLECULE GROUND STATE")
    print("=" * 60)

    print("H2 molecule simulation:")
    print("  2 hydrogen atoms")
    print("  2 electrons")
    print("  Bond length: 0.74 Angstroms")
    print()

    theta = Parameter('theta')

    qc = QuantumCircuit(2)
    qc.x(1)
    qc.ry(theta, 0)
    qc.cx(0, 1)
    qc.ry(-theta, 1)

    print("Ansatz circuit:")
    print(qc.draw('text'))

    print("\nTrue ground state energy: ~-1.85 Hartree")
    print("-> VQE can find this using a quantum computer")
    print("-> This is one of the most promising near-term applications!\n")


def quantum_random_walk_demo():
    """Demonstrate a quantum random walk."""
    print("=" * 60)
    print("6.5 QUANTUM RANDOM WALK")
    print("=" * 60)

    n_positions = 4
    n_steps = 3

    qc = QuantumCircuit(3, 2)

    print("Initial state: position 0, coin |0>")

    for step in range(n_steps):
        qc.h(2)
        qc.cx(2, 0)
        qc.cx(2, 1)
        print(f"Step {step + 1} completed")

    qc.measure([0, 1], [0, 1])

    print("\nCircuit:")
    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    counts = job.result().get_counts()

    print(f"\nPosition distribution after {n_steps} steps:")
    for pos, count in sorted(counts.items()):
        print(f"  Position {pos}: {count} shots")

    print("-> Quantum walks spread faster than classical random walks!")
    print("-> This speedup is used in quantum search algorithms\n")


if __name__ == "__main__":
    print("\n" + "[A]" * 30)
    print("QUANTUM FOUNDATIONS: QUANTUM SIMULATION")
    print("[A]" * 30 + "\n")

    harmonic_oscillator_demo()
    ising_model_demo()
    tunneling_demo()
    h2_molecule_demo()
    quantum_random_walk_demo()

    print("=" * 60)
    print("[OK] ALL QUANTUM SIMULATION DEMOS COMPLETE!")
    print("=" * 60)
    print("\nKEY TAKEAWAYS:")
    print("* Quantum simulation was Feynman's original motivation for QC")
    print("* Quantum computers naturally simulate quantum systems")
    print("* H2 molecule: promising near-term application")
    print("* Ising model: studies magnetism and phase transitions")
    print("* Quantum tunneling: classically impossible phenomenon")
    print("* Quantum walks: quadratically faster than classical")
