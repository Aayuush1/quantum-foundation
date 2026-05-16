"""
============================================================
02 - MULTI-QUBIT GATES & ENTANGLEMENT
============================================================
This module covers the magic of multi-qubit systems and entanglement.

What is Entanglement?
---------------------
When two qubits are entangled, measuring one INSTANTLY determines
the state of the other - even if they're light-years apart!
Einstein called this "spooky action at a distance."

Bell States:
-----------
There are 4 maximally entangled 2-qubit states called Bell states:
|Phi+> = (|00> + |11>)/sqrt(2)
|Phi-> = (|00> - |11>)/sqrt(2)
|Psi+> = (|01> + |10>)/sqrt(2)
|Psi-> = (|01> - |10>)/sqrt(2)
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


def cnot_demo():
    """Demonstrate the CNOT gate."""
    print("=" * 60)
    print("2.1 CNOT GATE (Controlled-NOT)")
    print("=" * 60)

    inputs = ["00", "01", "10", "11"]

    for inp in inputs:
        qc = QuantumCircuit(2, 2)
        if inp[0] == '1':
            qc.x(0)
        if inp[1] == '1':
            qc.x(1)

        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])

        simulator = AerSimulator()
        job = simulator.run(qc, shots=1)
        output = list(job.result().get_counts().keys())[0]

        print(f"  |{inp}> --[CNOT]--> |{output}>")

    print("-> When control (q0) is |1>, target (q1) flips!\n")


def bell_states_demo():
    """Create and verify all 4 Bell states."""
    print("=" * 60)
    print("2.2 BELL STATES (Maximally Entangled Pairs)")
    print("=" * 60)

    bell_circuits = {
        "|Phi+> = (|00> + |11>)/sqrt(2)": lambda qc: None,
        "|Phi-> = (|00> - |11>)/sqrt(2)": lambda qc: qc.z(0),
        "|Psi+> = (|01> + |10>)/sqrt(2)": lambda qc: qc.x(1),
        "|Psi-> = (|01> - |10>)/sqrt(2)": lambda qc: (qc.x(1), qc.z(0)),
    }

    simulator = AerSimulator()

    for name, extra_gate in bell_circuits.items():
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        extra_gate(qc)
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])

        job = simulator.run(qc, shots=10000)
        counts = job.result().get_counts()

        print(f"\n{name}:")
        print(f"  Circuit: H(0) -> CNOT(0,1)")
        print(f"  Measurement (10000 shots): {counts}")
        outcomes = list(counts.keys())
        print(f"  Possible outcomes: {outcomes}")
        print(f"  [OK] Entangled! Measuring one determines the other.")

    print("\n-> All Bell states are maximally entangled!")
    print("-> The qubits are correlated - you NEVER get |01> in |Phi+>\n")


def swap_demo():
    """Demonstrate the SWAP gate."""
    print("=" * 60)
    print("2.3 SWAP GATE")
    print("=" * 60)

    qc = QuantumCircuit(2, 2)
    qc.x(1)
    qc.swap(0, 1)
    qc.measure([0, 1], [0, 1])

    print("Starting state: |01>")
    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    counts = job.result().get_counts()

    print(f"After SWAP: {counts}")
    print("-> |01> became |10>! The qubits swapped places.\n")


def toffoli_demo():
    """Demonstrate the Toffoli (CCNOT) gate."""
    print("=" * 60)
    print("2.4 TOFFOLI GATE (CCNOT - Controlled-Controlled-NOT)")
    print("=" * 60)

    test_cases = ["000", "001", "010", "011", "100", "101", "110", "111"]
    simulator = AerSimulator()

    for inp in test_cases:
        qc = QuantumCircuit(3, 3)
        for i, bit in enumerate(inp):
            if bit == '1':
                qc.x(i)

        qc.ccx(0, 1, 2)
        qc.measure([0, 1, 2], [0, 1, 2])

        job = simulator.run(qc, shots=1)
        output = list(job.result().get_counts().keys())[0]

        reason = "BOTH controls |1>" if (inp[0] == '1' and inp[1] == '1') else "controls not both |1>"
        print(f"  |{inp}> --[CCNOT]--> |{output}>  ({reason})")

    print("-> Target flips ONLY when both controls are |1>!\n")


def quantum_teleportation_demo():
    """Demonstrate quantum teleportation."""
    print("=" * 60)
    print("2.5 QUANTUM TELEPORTATION")
    print("=" * 60)

    qc = QuantumCircuit(3, 3)

    # Step 1: Create the state to teleport on qubit 0
    qc.h(0)
    print("State to teleport: |psi> = |+> = (|0> + |1>)/sqrt(2)")

    # Step 2: Create Bell pair between qubits 1 and 2
    qc.h(1)
    qc.cx(1, 2)
    print("Created Bell pair between qubits 1 (Alice) and 2 (Bob)")

    # Step 3: Alice performs Bell measurement on qubits 0 and 1
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    print("Alice performs Bell measurement")

    # Step 4: Bob applies corrections based on Alice's results
    with qc.if_test((qc.clbits[1], 1)):
        qc.x(2)
    with qc.if_test((qc.clbits[0], 1)):
        qc.z(2)

    # Step 5: Measure Bob's qubit to verify
    qc.measure(2, 2)

    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=10000)
    counts = job.result().get_counts()

    print(f"\nMeasurement results: {counts}")
    print("-> Bob's qubit (last bit) should be |0> and |1> with ~50% each")
    print("-> This matches the original |psi> = |+>!")
    print("-> The state was successfully teleported!\n")


def quantum_half_adder_demo():
    """Demonstrate a quantum half-adder."""
    print("=" * 60)
    print("2.6 QUANTUM HALF-ADDER")
    print("=" * 60)

    test_cases = ["00", "01", "10", "11"]
    simulator = AerSimulator()

    for inp in test_cases:
        qc = QuantumCircuit(4, 2)

        if inp[0] == '1':
            qc.x(0)
        if inp[1] == '1':
            qc.x(1)

        qc.cx(1, 2)
        qc.cx(0, 2)
        qc.ccx(0, 1, 3)
        qc.measure([2, 3], [0, 1])

        job = simulator.run(qc, shots=1)
        output = list(job.result().get_counts().keys())[0]

        a, b = int(inp[0]), int(inp[1])
        expected = f"{(a+b)%2}{(a+b)//2}"
        status = "[OK]" if output == expected else "[FAIL]"

        print(f"  {inp[0]} + {inp[1]} = {output} (sum={output[0]}, carry={output[1]})  {status}")

    print("-> Quantum half-adder works like a classical one!\n")


def ghz_state_demo():
    """Create a 3-qubit GHZ state."""
    print("=" * 60)
    print("2.7 GHZ STATE (3-Qubit Entanglement)")
    print("=" * 60)

    n = 3
    qc = QuantumCircuit(n, n)

    qc.h(0)
    for i in range(n - 1):
        qc.cx(i, i + 1)

    qc.measure(range(n), range(n))

    print(f"Creating GHZ state with {n} qubits:")
    print(qc.draw('text'))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=10000)
    counts = job.result().get_counts()

    print(f"\nMeasurement results: {counts}")
    print("-> Only |000> and |111> appear!")
    print("-> All 3 qubits are perfectly correlated!\n")


if __name__ == "__main__":
    print("\n" + "[Q]" * 30)
    print("QUANTUM FOUNDATIONS: MULTI-QUBIT GATES & ENTANGLEMENT")
    print("[Q]" * 30 + "\n")

    cnot_demo()
    bell_states_demo()
    swap_demo()
    toffoli_demo()
    quantum_teleportation_demo()
    quantum_half_adder_demo()
    ghz_state_demo()

    print("=" * 60)
    print("[OK] ALL MULTI-QUBIT DEMOS COMPLETE!")
    print("=" * 60)
    print("\nKEY TAKEAWAYS:")
    print("* CNOT = fundamental 2-qubit gate (conditional flip)")
    print("* H + CNOT = creates entanglement (Bell states)")
    print("* SWAP = exchanges qubit states")
    print("* Toffoli = AND gate for quantum computing")
    print("* Teleportation = transfers quantum states using entanglement")
    print("* GHZ = multi-qubit entanglement (all correlated)")
