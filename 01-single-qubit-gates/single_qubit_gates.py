"""
============================================================
01 - SINGLE QUBIT GATES
============================================================
This module covers the fundamental building blocks of quantum computing:
single qubit gates. Think of these as the "alphabet" of quantum circuits.

What is a Qubit?
----------------
A classical bit is either 0 or 1. A qubit can be 0, 1, or BOTH at the same
time (called "superposition"). We represent a qubit's state as:
    |psi> = alpha|0> + beta|1>
where alpha and beta are complex numbers, and |alpha|^2 + |beta|^2 = 1.

The Bloch Sphere is a way to visualize any single qubit state as a point
on the surface of a sphere.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import os
import numpy as np


def x_gate_demo():
    """Demonstrate the X (NOT) gate."""
    print("=" * 60)
    print("1.1 X GATE (Quantum NOT)")
    print("=" * 60)

    qc = QuantumCircuit(1, 1)
    qc.x(0)
    qc.measure(0, 0)

    print("Circuit: |0> --[X]--(measure)--> |1>")
    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    counts = job.result().get_counts()

    print(f"Measurement results (1000 shots): {counts}")
    print("-> X gate flipped |0> to |1> 100% of the time!\n")
    return qc


def h_gate_demo():
    """Demonstrate the H (Hadamard) gate creating superposition."""
    print("=" * 60)
    print("1.2 H GATE (Hadamard - Creates Superposition)")
    print("=" * 60)

    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    print("Circuit: |0> --[H]--(measure)--> |0> or |1> (50/50)")
    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=10000)
    counts = job.result().get_counts()

    print(f"Measurement results (10000 shots): {counts}")
    print("-> The qubit is in SUPERPOSITION!")
    print("-> Measuring collapses it randomly to |0> or |1> with 50% probability each.\n")
    return qc


def z_gate_demo():
    """Demonstrate the Z (phase flip) gate."""
    print("=" * 60)
    print("1.3 Z GATE (Phase Flip)")
    print("=" * 60)

    qc0 = QuantumCircuit(1, 1)
    qc0.z(0)
    qc0.measure(0, 0)

    print("Z|0> = |0> (no change)")
    print(qc0.draw('text'))

    simulator = AerSimulator()
    job0 = simulator.run(qc0, shots=1000)
    print(f"Measurement: {job0.result().get_counts()}")

    qc1 = QuantumCircuit(1, 1)
    qc1.x(0)
    qc1.z(0)
    qc1.measure(0, 0)

    print("\nZ|1> = -|1> (phase flips, but measurement still shows |1>)")
    print(qc1.draw('text'))

    job1 = simulator.run(qc1, shots=1000)
    print(f"Measurement: {job1.result().get_counts()}")
    print("-> Phase is 'invisible' in standard measurement!\n")


def y_gate_demo():
    """Demonstrate the Y gate."""
    print("=" * 60)
    print("1.4 Y GATE")
    print("=" * 60)

    qc = QuantumCircuit(1, 1)
    qc.y(0)
    qc.measure(0, 0)

    print("Y|0> = i|1>")
    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    print(f"Measurement: {job.result().get_counts()}")
    print("-> Y flips |0> to |1> (with a phase factor i)\n")


def s_t_gate_demo():
    """Demonstrate S and T phase gates."""
    print("=" * 60)
    print("1.5 S AND T GATES (Phase Gates)")
    print("=" * 60)

    qc_s = QuantumCircuit(1, 1)
    qc_s.x(0)
    qc_s.s(0)
    qc_s.measure(0, 0)

    print("S|1> = i|1>")
    print(qc_s.draw('text'))

    simulator = AerSimulator()
    job_s = simulator.run(qc_s, shots=1000)
    print(f"S gate measurement: {job_s.result().get_counts()}")

    qc_t = QuantumCircuit(1, 1)
    qc_t.x(0)
    qc_t.t(0)
    qc_t.measure(0, 0)

    print("\nT|1> = e^(ipi/4)|1>")
    print(qc_t.draw('text'))

    job_t = simulator.run(qc_t, shots=1000)
    print(f"T gate measurement: {job_t.result().get_counts()}")
    print("-> Like Z, phase is invisible in standard measurement.\n")


def bloch_sphere_demo():
    """Visualize single qubit states on the Bloch sphere."""
    print("=" * 60)
    print("1.6 BLOCH SPHERE VISUALIZATION")
    print("=" * 60)
    print("Generating Bloch sphere plots for different states...")

    fig, axes = plt.subplots(2, 3, figsize=(15, 10), subplot_kw={'projection': '3d'})
    fig.suptitle('Single Qubit States on the Bloch Sphere', fontsize=16, fontweight='bold')

    states = [
        ("|0>", [1, 0]),
        ("|1>", [0, 1]),
        ("|+> = H|0>", None),
        ("|-> = HX|0>", None),
        ("|i+> = SH|0>", None),
        ("|i-> = SHX|0>", None),
    ]

    for idx, (name, state) in enumerate(states):
        row, col = idx // 3, idx % 3
        ax = axes[row, col]

        if state is not None:
            sv = Statevector(state)
        else:
            qc = QuantumCircuit(1)
            if "|+>" in name:
                qc.h(0)
            elif "|->" in name:
                qc.x(0)
                qc.h(0)
            elif "|i+>" in name:
                qc.h(0)
                qc.s(0)
            elif "|i->" in name:
                qc.x(0)
                qc.h(0)
                qc.s(0)
            sv = Statevector.from_instruction(qc)

        # Manual Bloch sphere plotting
        x = 2 * np.real(np.conj(sv.data[0]) * sv.data[1])
        y = 2 * np.imag(np.conj(sv.data[0]) * sv.data[1])
        z = np.abs(sv.data[0])**2 - np.abs(sv.data[1])**2

        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        xs = np.outer(np.cos(u), np.sin(v))
        ys = np.outer(np.sin(u), np.sin(v))
        zs = np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_wireframe(xs, ys, zs, alpha=0.2, color='gray')

        ax.plot([-1, 1], [0, 0], [0, 0], 'k-', alpha=0.3)
        ax.plot([0, 0], [-1, 1], [0, 0], 'k-', alpha=0.3)
        ax.plot([0, 0], [0, 0], [-1, 1], 'k-', alpha=0.3)

        ax.plot([0, x], [0, y], [0, z], 'r-', linewidth=2)
        ax.scatter([x], [y], [z], color='red', s=100)

        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(name, fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), "..", "assets", "bloch_sphere_states.png"), dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Saved to assets/bloch_sphere_states.png")
    print("-> |0> is at the North Pole, |1> at the South Pole")
    print("-> |+> is on the +X axis (equator), |-> on the -X axis")
    print("-> |i+> and |i-> are on the +/-Y axes\n")


def custom_rotation_demo():
    """Demonstrate arbitrary single-qubit rotations."""
    print("=" * 60)
    print("1.7 CUSTOM ROTATIONS")
    print("=" * 60)

    theta = np.pi / 3
    phi = 0
    lam = 0

    qc = QuantumCircuit(1)
    qc.u(theta, phi, lam, 0)

    print(f"Applying U(theta=pi/3, phi=0, lam=0)")
    print(qc.draw('text'))

    sv = Statevector.from_instruction(qc)
    print(f"Statevector: {sv.data}")
    print(f"Probability of |0>: {abs(sv.data[0])**2:.4f}")
    print(f"Probability of |1>: {abs(sv.data[1])**2:.4f}")
    print("-> This creates a biased superposition (not 50/50)\n")


if __name__ == "__main__":
    print("\n" + "[*]" * 30)
    print("QUANTUM FOUNDATIONS: SINGLE QUBIT GATES")
    print("[*]" * 30 + "\n")

    x_gate_demo()
    h_gate_demo()
    z_gate_demo()
    y_gate_demo()
    s_t_gate_demo()
    bloch_sphere_demo()
    custom_rotation_demo()

    print("=" * 60)
    print("[OK] ALL SINGLE QUBIT GATE DEMOS COMPLETE!")
    print("=" * 60)
    print("\nKEY TAKEAWAYS:")
    print("* X = NOT gate (flips |0> <-> |1>)")
    print("* H = Creates superposition (|0> -> equal mix)")
    print("* Z = Phase flip (invisible in standard measurement)")
    print("* Y = Combined X+Z effect")
    print("* S/T = Phase rotations (pi/2 and pi/4)")
    print("* Any single-qubit gate = combination of rotations")
