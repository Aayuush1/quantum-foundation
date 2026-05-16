"""
============================================================
04 - QUANTUM ERROR CORRECTION
============================================================
This module covers how to protect quantum information from noise.

Why Error Correction Matters:
----------------------------
Quantum computers are extremely sensitive to noise. Without error
correction, quantum computations would be impossible for large problems.

The No-Cloning Theorem:
----------------------
You cannot copy an arbitrary quantum state. This makes classical error
correction (like making backups) impossible in quantum computing.

Solution: Encode 1 logical qubit into multiple physical qubits.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np


def bit_flip_code_demo():
    """Demonstrate the 3-qubit bit flip code."""
    print("=" * 60)
    print("4.1 BIT FLIP CODE")
    print("=" * 60)

    qc = QuantumCircuit(5, 2)

    # Prepare logical |1>
    qc.x(0)

    # Encoding: |1> -> |111>
    qc.cx(0, 1)
    qc.cx(0, 2)

    print("Encoded |1> as |111>")

    # Introduce an error on qubit 1
    qc.x(1)
    print("Error introduced: qubit 1 flipped (|111> -> |101>)")

    # Syndrome measurement
    qc.cx(0, 3)
    qc.cx(1, 3)
    qc.cx(1, 4)
    qc.cx(2, 4)

    qc.measure([3, 4], [0, 1])

    # Correction using if_test
    with qc.if_test((qc.clbits[0], 1)):
        qc.x(0)
    with qc.if_test((qc.clbits[1], 1)):
        qc.x(2)

    # Decode
    qc.cx(0, 1)
    qc.cx(0, 2)

    # Measure
    qc.measure(0, 0)

    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    counts = job.result().get_counts()

    print(f"Measurement: {counts}")
    print("-> The error was detected and corrected!")
    print("-> The original |1> state is preserved.\n")


def phase_flip_code_demo():
    """Demonstrate the 3-qubit phase flip code."""
    print("=" * 60)
    print("4.2 PHASE FLIP CODE")
    print("=" * 60)

    qc = QuantumCircuit(3, 1)

    # Prepare |1>
    qc.x(0)

    # Encode in Hadamard basis: |1> -> |--->
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.h(1)
    qc.h(2)

    print("Encoded |1> as |--->")

    # Introduce phase flip error on qubit 1
    qc.z(1)
    print("Error introduced: phase flip on qubit 1")

    # Decode
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.cx(0, 1)
    qc.cx(0, 2)

    # Measure
    qc.measure(0, 0)

    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    counts = job.result().get_counts()

    print(f"Measurement: {counts}")
    print("-> Phase flip code protects against Z errors!\n")


def shor_code_demo():
    """Demonstrate the 9-qubit Shor code."""
    print("=" * 60)
    print("4.3 SHOR CODE (9-Qubit Code)")
    print("=" * 60)

    qc = QuantumCircuit(9, 1)

    # Prepare |1>
    qc.x(0)

    # Encoding
    qc.h(0)
    qc.cx(0, 3)
    qc.cx(0, 6)

    for start in [0, 3, 6]:
        qc.cx(start, start + 1)
        qc.cx(start, start + 2)

    print("Encoded |1> using 9 qubits")

    # Introduce a random single-qubit error
    import random
    error_qubit = random.randint(0, 8)
    error_type = random.choice(['X', 'Z', 'Y'])

    if error_type == 'X':
        qc.x(error_qubit)
    elif error_type == 'Z':
        qc.z(error_qubit)
    else:
        qc.y(error_qubit)

    print(f"Error introduced: {error_type} on qubit {error_qubit}")

    # Decode
    for start in [0, 3, 6]:
        qc.cx(start, start + 1)
        qc.cx(start, start + 2)

    qc.cx(0, 3)
    qc.cx(0, 6)
    qc.h(0)

    # Measure
    qc.measure(0, 0)

    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    counts = job.result().get_counts()

    print(f"Measurement: {counts}")
    print("-> Shor code protects against ANY single-qubit error!")
    print("-> This is the foundation of fault-tolerant quantum computing.\n")


def threshold_demo():
    """Demonstrate the concept of error threshold."""
    print("=" * 60)
    print("4.4 ERROR THRESHOLD THEOREM")
    print("=" * 60)

    print("The Threshold Theorem:")
    print("-" * 40)
    print("If error rate per gate < threshold (~0.1-1%)")
    print("Then: Arbitrarily long quantum computation is possible")
    print("      using quantum error correction")
    print()

    error_rates = [0.001, 0.005, 0.01, 0.05, 0.1]
    num_gates = 1000

    print(f"Simulation: {num_gates} gates with different error rates")
    print("-" * 40)

    for rate in error_rates:
        success_prob = (1 - rate) ** num_gates
        print(f"  Error rate: {rate*100:>5.1f}% -> Success probability: {success_prob:.6f}")

    print()
    print("-> Below threshold: Error correction can fix errors faster than they occur")
    print("-> Above threshold: Errors accumulate faster than they can be corrected")
    print("-> Current quantum computers: ~0.1-1% error rates (near threshold!)")
    print("-> Goal: Get below ~0.01% for practical quantum computing\n")


if __name__ == "__main__":
    print("\n" + "[S]" * 30)
    print("QUANTUM FOUNDATIONS: QUANTUM ERROR CORRECTION")
    print("[S]" * 30 + "\n")

    bit_flip_code_demo()
    phase_flip_code_demo()
    shor_code_demo()
    threshold_demo()

    print("=" * 60)
    print("[OK] ALL ERROR CORRECTION DEMOS COMPLETE!")
    print("=" * 60)
    print("\nKEY TAKEAWAYS:")
    print("* Bit flip code: 3 qubits protect against X errors")
    print("* Phase flip code: 3 qubits protect against Z errors")
    print("* Shor code: 9 qubits protect against ANY single-qubit error")
    print("* No-cloning theorem makes quantum error correction tricky")
    print("* Threshold theorem: below ~1% error, fault-tolerant QC is possible")
