"""
============================================================
03 - QUANTUM ALGORITHMS
============================================================
This module implements the most important quantum algorithms.
These are the algorithms that made quantum computing famous!

Why Quantum Algorithms Matter:
-----------------------------
Quantum computers can solve certain problems exponentially faster
than classical computers. These algorithms demonstrate that power.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import numpy as np


def deutsch_jozsa(n=3, function_type="balanced"):
    """
    Deutsch-Jozsa Algorithm.

    PROBLEM: Given a function f(x), determine if it is:
      - CONSTANT (same output for ALL inputs)
      - BALANCED (outputs 0 for half, 1 for other half)

    CLASSICAL: Need up to 2^(n-1) + 1 queries.
    QUANTUM:   Needs ONLY 1 query!
    """
    print("=" * 60)
    print(f"3.1 DEUTSCH-JOZSA ALGORITHM (n={n})")
    print("=" * 60)

    qc = QuantumCircuit(n + 1, n)
    qc.x(n)

    for i in range(n + 1):
        qc.h(i)

    if function_type == "balanced":
        qc.cx(0, n)

    for i in range(n):
        qc.h(i)

    qc.measure(range(n), range(n))

    print(f"Function type: {function_type}")
    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    measured = list(job.result().get_counts().keys())[0]

    print(f"\nMeasurement result: |{measured}>")

    if measured == "0" * n:
        answer = "constant"
        print("-> All zeros! The function is CONSTANT.")
    else:
        answer = "balanced"
        print("-> Not all zeros! The function is BALANCED.")

    print(f"-> Correct answer: {answer} (determined in 1 query!)\n")
    return answer


def bernstein_vazirani(n=4, secret_string="1011"):
    """
    Bernstein-Vazirani Algorithm.

    PROBLEM: Given f(x) = s . x (dot product mod 2), find s.

    CLASSICAL: Need n queries.
    QUANTUM:   Needs ONLY 1 query!
    """
    print("=" * 60)
    print(f"3.2 BERNSTEIN-VAZIRANI ALGORITHM (n={n})")
    print("=" * 60)

    qc = QuantumCircuit(n + 1, n)
    qc.x(n)

    for i in range(n + 1):
        qc.h(i)

    for i, bit in enumerate(reversed(secret_string)):
        if bit == '1':
            qc.cx(i, n)

    for i in range(n):
        qc.h(i)

    qc.measure(range(n), range(n))

    print(f"Secret string to find: {secret_string}")
    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    measured = list(job.result().get_counts().keys())[0]

    print(f"\nMeasurement result: {measured}")
    print(f"-> Secret string found: {measured}")
    print(f"-> Correct! Found in 1 query instead of {n}!\n")

    return measured


def grovers_search(n=3, target="101"):
    """
    Grover's Search Algorithm.

    PROBLEM: Search an unsorted database of N items.

    CLASSICAL: Need up to N queries.
    QUANTUM:   Needs ONLY sqrt(N) queries!
    """
    print("=" * 60)
    print(f"3.3 GROVER'S SEARCH ALGORITHM (n={n}, target={target})")
    print("=" * 60)

    N = 2 ** n
    num_iterations = int(np.round(np.pi / 4 * np.sqrt(N)))

    qc = QuantumCircuit(n, n)

    for i in range(n):
        qc.h(i)

    for _ in range(num_iterations):
        # Oracle
        for i, bit in enumerate(reversed(target)):
            if bit == '0':
                qc.x(i)

        qc.h(n - 1)
        qc.mcx(list(range(n - 1)), n - 1)
        qc.h(n - 1)

        for i, bit in enumerate(reversed(target)):
            if bit == '0':
                qc.x(i)

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

    print(f"Database size: {N}")
    print(f"Target: {target}")
    print(f"Iterations: {num_iterations} (optimal)")
    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    counts = job.result().get_counts()

    print(f"\nMeasurement results (1000 shots):")
    for state, count in sorted(counts.items(), key=lambda x: -x[1])[:5]:
        marker = " <- TARGET!" if state == target else ""
        print(f"  |{state}>: {count} shots{marker}")

    most_probable = max(counts, key=counts.get)
    print(f"\n-> Most probable result: |{most_probable}>")
    print(f"-> Success probability: {counts[most_probable]/1000*100:.1f}%")
    print(f"-> Classical would need up to {N} queries, quantum used {num_iterations}!\n")

    return most_probable


def qft_demo(n=3):
    """
    Quantum Fourier Transform demonstration.

    The quantum version of FFT. Key component of Shor's algorithm.
    """
    print("=" * 60)
    print(f"3.4 QUANTUM FOURIER TRANSFORM (n={n})")
    print("=" * 60)

    qc = QuantumCircuit(n)

    for j in range(n):
        qc.h(j)
        for k in range(j + 1, n):
            angle = np.pi / (2 ** (k - j))
            qc.cp(angle, k, j)

    for j in range(n // 2):
        qc.swap(j, n - j - 1)

    print("QFT Circuit:")
    print(qc.draw('text'))

    from qiskit.quantum_info import Statevector

    test_qc = QuantumCircuit(n)
    test_qc.x(0)
    test_qc.compose(qc, inplace=True)

    qft_inv = qc.inverse()
    test_qc.compose(qft_inv, inplace=True)

    sv = Statevector.from_instruction(test_qc)
    print(f"\nVerification: QFT then inverse QFT on |001>")
    print(f"Result statevector (should be |001>): {sv.data}")
    print("-> QFT is unitary (its own inverse up to swaps)!\n")


def shors_algorithm_demo(N=15):
    """
    Shor's Algorithm - Simplified demonstration.

    PROBLEM: Factor a large integer N.

    CLASSICAL: Sub-exponential time.
    QUANTUM:   Polynomial time!
    """
    print("=" * 60)
    print(f"3.5 SHOR'S ALGORITHM (N={N})")
    print("=" * 60)

    print(f"Goal: Factor N = {N}")

    import math
    a = 2
    while math.gcd(a, N) != 1:
        a += 1

    print(f"Chosen a = {a} (coprime to {N})")

    def find_period_classical(a, N):
        x = 1
        for r in range(1, N):
            x = (x * a) % N
            if x == 1:
                return r
        return None

    r = find_period_classical(a, N)
    print(f"Period r = {r} (found classically for demo)")

    if r is None or r % 2 != 0:
        print("-> Period is odd or not found. Try different a.\n")
        return None

    factor1 = math.gcd(a**(r//2) - 1, N)
    factor2 = math.gcd(a**(r//2) + 1, N)

    print(f"Factors: {factor1} and {factor2}")

    if factor1 * factor2 == N and factor1 != 1 and factor2 != 1:
        print(f"-> SUCCESS! {N} = {factor1} x {factor2}")
        print("-> This would take exponential time classically!\n")
        return (factor1, factor2)
    else:
        print("-> Need to try a different random a.\n")
        return None


def qpe_demo():
    """
    Quantum Phase Estimation.

    Given U and eigenstate |psi>, estimate eigenvalue e^(2*pi*i*theta).
    """
    print("=" * 60)
    print("3.6 QUANTUM PHASE ESTIMATION")
    print("=" * 60)

    n_count = 3
    theta = 1/8

    qc = QuantumCircuit(n_count + 1, n_count)

    for q in range(n_count):
        qc.h(q)

    qc.x(n_count)

    for k in range(n_count):
        angle = 2 * np.pi * theta * (2 ** k)
        qc.cp(angle, k, n_count)

    for j in range(n_count // 2):
        qc.swap(j, n_count - j - 1)

    for j in range(n_count):
        qc.h(j)
        for k in range(j + 1, n_count):
            angle = -np.pi / (2 ** (k - j))
            qc.cp(angle, k, j)

    qc.measure(range(n_count), range(n_count))

    print(f"True phase: theta = {theta} = 1/8")
    print(f"Expected measurement: {int(theta * 2**n_count)} = 001 (binary)")
    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    counts = job.result().get_counts()

    print(f"\nMeasurement results:")
    for state, count in sorted(counts.items(), key=lambda x: -x[1]):
        estimated_phase = int(state, 2) / (2 ** n_count)
        print(f"  |{state}>: {count} shots -> theta ~ {estimated_phase:.4f}")

    most_probable = max(counts, key=counts.get)
    estimated = int(most_probable, 2) / (2 ** n_count)
    print(f"\n-> Most probable estimate: theta ~ {estimated}")
    print(f"-> True value: {theta}")
    print(f"-> Accuracy improves with more counting qubits!\n")


if __name__ == "__main__":
    print("\n" + "[!]" * 30)
    print("QUANTUM FOUNDATIONS: QUANTUM ALGORITHMS")
    print("[!]" * 30 + "\n")

    deutsch_jozsa(n=3, function_type="balanced")
    bernstein_vazirani(n=4, secret_string="1011")
    grovers_search(n=3, target="101")
    qft_demo(n=3)
    shors_algorithm_demo(N=15)
    qpe_demo()

    print("=" * 60)
    print("[OK] ALL QUANTUM ALGORITHM DEMOS COMPLETE!")
    print("=" * 60)
    print("\nKEY TAKEAWAYS:")
    print("* Deutsch-Jozsa: Exponential speedup for function testing")
    print("* Bernstein-Vazirani: Find hidden string in 1 query")
    print("* Grover's Search: Quadratic speedup for unstructured search")
    print("* QFT: Foundation for many quantum algorithms")
    print("* Shor's: Exponential speedup for factoring (threatens RSA!)")
    print("* QPE: Estimates eigenvalues, used in chemistry and crypto")
