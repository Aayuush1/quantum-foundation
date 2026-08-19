<div align="center">

# Quantum Foundation

**A hands-on, code-first curriculum for quantum computing — from your first qubit to real IBM Quantum hardware.**

[![CI](https://github.com/Aayuush1/quantum-foundation/actions/workflows/ci.yml/badge.svg)](https://github.com/Aayuush1/quantum-foundation/actions/workflows/ci.yml)
[![Python 3.9–3.13](https://img.shields.io/badge/python-3.9%E2%80%933.13-blue.svg)](https://www.python.org/downloads/)
[![Qiskit 1.0+](https://img.shields.io/badge/qiskit-1.0%2B-6133BD.svg)](https://qiskit.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

---

## Overview

Quantum Foundation is a six-module, progressive learning path through quantum computing. Every concept is taught **through runnable, tested code** — not slides. You start by flipping a single qubit and finish by running variational algorithms and physical simulations, with a clear on-ramp to real quantum hardware at the end.

**What makes this different:**

- **Everything runs.** All modules are tested and CI-verified across Python 3.9–3.13.
- **Modern API.** Written for Qiskit 1.0+ — no deprecated patterns, no outdated tutorials.
- **Progressive structure.** Each module builds directly on the last: gates → entanglement → algorithms → error correction → quantum ML → simulation.
- **Hardware-ready.** Swap one line to run the same circuits on IBM Quantum processors.

> *"If quantum mechanics hasn't profoundly shocked you, you haven't understood it yet."* — Niels Bohr

---

## Table of Contents

- [Quick Start](#quick-start)
- [Curriculum](#curriculum)
- [Module Details](#module-details)
- [Algorithm Speedups at a Glance](#algorithm-speedups-at-a-glance)
- [Testing](#testing)
- [Running on Real Quantum Hardware](#running-on-real-quantum-hardware)
- [Project Structure](#project-structure)
- [Suggested Learning Path](#suggested-learning-path)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Aayuush1/quantum-foundation.git
cd quantum-foundation

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run your first quantum circuit
python 01-single-qubit-gates/single_qubit_gates.py
```

Expected output:

```text
============================================================
1.1 X GATE (Quantum NOT)
============================================================
Measurement results (1000 shots): {'1': 1000}
-> X gate flipped |0> to |1> 100% of the time!
```

That's it — you've just run a quantum NOT gate on a simulator. From here, follow the curriculum below.

---

## Curriculum

| # | Module | Topics Covered | Level | Run |
|---|--------|----------------|-------|-----|
| 01 | [Single-Qubit Gates](01-single-qubit-gates/) | X, H, Y, Z, S, T gates, Bloch sphere, rotations | Beginner | `python 01-single-qubit-gates/single_qubit_gates.py` |
| 02 | [Multi-Qubit Gates](02-multi-qubit-gates/) | CNOT, SWAP, Toffoli, Bell states, entanglement, teleportation | Intermediate | `python 02-multi-qubit-gates/multi_qubit_gates.py` |
| 03 | [Quantum Algorithms](03-quantum-algorithms/) | Deutsch–Jozsa, Grover's, Shor's, QFT, QPE, Bernstein–Vazirani | Advanced | `python 03-quantum-algorithms/quantum_algorithms.py` |
| 04 | [Quantum Error Correction](04-quantum-error-correction/) | Bit-flip & phase-flip codes, Shor code, threshold theorem | Advanced | `python 04-quantum-error-correction/quantum_error_correction.py` |
| 05 | [Quantum Machine Learning](05-quantum-ml/) | VQE, QNNs, feature maps, QAOA, quantum kernels | Expert | `python 05-quantum-ml/quantum_ml.py` |
| 06 | [Quantum Simulation](06-quantum-simulation/) | Harmonic oscillator, Ising model, tunneling, quantum walks | Expert | `python 06-quantum-simulation/quantum_simulation.py` |

---

## Module Details

<details>
<summary><strong>01 · Single-Qubit Gates</strong> — the building blocks</summary>

A qubit is the quantum analogue of a classical bit: instead of being strictly `0` or `1`, it exists in a superposition `α|0⟩ + β|1⟩`. This module teaches you to manipulate that state.

- **X gate** — quantum NOT: flips `|0⟩ ↔ |1⟩`
- **H (Hadamard) gate** — creates superposition; the foundation of nearly every quantum speedup
- **Y and Z gates** — combined bit/phase flips and pure phase flips
- **S and T gates** — π/2 and π/4 phase rotations, essential for universal computation
- **Bloch sphere** — the geometric picture of a qubit's state, and how each gate rotates it

**Key insight:** The Hadamard gate is the "magic gate." Putting a qubit into superposition is what lets quantum algorithms explore many possibilities at once.

</details>

<details>
<summary><strong>02 · Multi-Qubit Gates</strong> — entanglement and teleportation</summary>

Things get genuinely quantum when qubits interact. This module covers the gates and phenomena that have no classical counterpart.

- **CNOT** — the controlled-NOT, the workhorse two-qubit gate
- **SWAP and Toffoli** — multi-qubit state manipulation and reversible logic
- **Bell states** — the four maximally entangled two-qubit states
- **Entanglement** — measuring one qubit instantly determines its partner, at any distance
- **Quantum teleportation** — transferring a quantum state using entanglement + classical bits

**Key insight:** Entanglement is correlation beyond anything classical physics allows. It powers quantum communication, cryptography, and teleportation protocols.

</details>

<details>
<summary><strong>03 · Quantum Algorithms</strong> — where the speedups live</summary>

The famous algorithms, implemented end-to-end so you can see exactly where the quantum advantage comes from.

- **Deutsch–Jozsa** — the first proven exponential separation between quantum and classical
- **Grover's search** — quadratic speedup for unstructured search
- **Shor's algorithm** — polynomial-time factoring; the reason post-quantum cryptography exists
- **Quantum Fourier Transform (QFT)** — the engine inside Shor's and phase estimation
- **Quantum Phase Estimation (QPE)** — extracting eigenvalues, central to quantum chemistry
- **Bernstein–Vazirani** — recovering a hidden bit string in a single query

**Key insight:** Shor's algorithm breaks RSA in principle. Understanding *why* requires understanding interference — and this module builds that intuition step by step.

</details>

<details>
<summary><strong>04 · Quantum Error Correction</strong> — fighting decoherence</summary>

Real qubits are fragile. This module shows how the field protects quantum information without violating the no-cloning theorem.

- **Bit-flip code** — encode one logical qubit into three physical qubits; correct via majority vote
- **Phase-flip code** — the dual construction in the Hadamard basis
- **Shor code** — nine-qubit code correcting arbitrary single-qubit errors
- **Threshold theorem** — why arbitrarily long quantum computation is possible in principle

**Key insight:** You cannot copy an unknown quantum state (no-cloning theorem), so classical backup strategies fail. Redundancy must be encoded *across* entangled physical qubits instead.

</details>

<details>
<summary><strong>05 · Quantum Machine Learning</strong> — hybrid quantum-classical computing</summary>

The most commercially active area of near-term quantum computing: hybrid loops where a quantum processor evaluates hard functions and a classical optimizer steers.

- **VQE** — the Variational Quantum Eigensolver for ground-state energies
- **QNNs** — quantum neural networks with parameterized circuits
- **Feature maps** — embedding classical data into quantum Hilbert space
- **QAOA** — approximate optimization for combinatorial problems
- **Quantum kernels** — kernel methods with quantum-computed inner products

**Key insight:** VQE-class algorithms are already used in industry (molecular simulation for batteries and drug discovery) because they tolerate the noise of today's hardware.

</details>

<details>
<summary><strong>06 · Quantum Simulation</strong> — Feynman's original dream</summary>

*"Nature isn't classical, dammit, and if you want to make a simulation of nature, you'd better make it quantum mechanical."* — Richard Feynman

- **H₂ molecule** — ground-state energy estimation, the "hello world" of quantum chemistry
- **Ising model** — magnetism and spin interactions
- **Quantum tunneling** — dynamics with no classical analogue
- **Quantum random walks** — quadratically faster spreading than classical walks

**Key insight:** Simulating quantum systems is the most natural application of quantum computers — and arguably the one that will matter first.

</details>

---

## Algorithm Speedups at a Glance

| Algorithm | Classical Cost | Quantum Cost | Speedup | Why It Matters |
|-----------|---------------|--------------|---------|----------------|
| Deutsch–Jozsa | 2ⁿ⁻¹ + 1 queries | **1 query** | Exponential | First proven quantum advantage |
| Grover's Search | N queries | **√N queries** | Quadratic | Search, SAT solving, optimization |
| Shor's Algorithm | Sub-exponential | **Polynomial** | Exponential | Breaks RSA/ECC — drives post-quantum crypto |
| QPE | Exponential | **Polynomial** | Exponential | Quantum chemistry, materials science |

---

## Testing

Every module ships with unit tests covering the physics, not just the syntax.

```bash
# Run the full test suite
python -m pytest tests/

# Or run directly
python tests/test_all.py
```

**Coverage includes:** single-qubit gate operations (X, H, Y, Z) · superposition verification · CNOT and entanglement · Bell state generation · SWAP · Deutsch–Jozsa · Grover's search · VQE ground-state energy · quantum kernel computation.

CI runs the suite on every push across **Python 3.9, 3.10, 3.11, 3.12, and 3.13** via GitHub Actions.

---

## Running on Real Quantum Hardware

Every circuit in this repo runs on IBM Quantum processors with a one-line backend swap:

```python
# Simulator (default)
simulator = AerSimulator()

# Real IBM Quantum hardware
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService(channel="ibm_quantum", token="YOUR_TOKEN")
backend = service.least_busy(operational=True, simulator=False)
```

Get a free API token at [quantum.ibm.com](https://quantum.ibm.com/). Free-tier access is enough to run every circuit in this repository.

---

## Project Structure

```text
quantum-foundation/
├── 01-single-qubit-gates/        # X, H, Y, Z, S, T · Bloch sphere
│   ├── single_qubit_gates.py
│   └── README.md
├── 02-multi-qubit-gates/         # CNOT, SWAP, Toffoli · Bell states · teleportation
│   ├── multi_qubit_gates.py
│   └── README.md
├── 03-quantum-algorithms/        # Deutsch–Jozsa · Grover · Shor · QFT · QPE
│   ├── quantum_algorithms.py
│   └── README.md
├── 04-quantum-error-correction/  # Bit-flip · phase-flip · Shor code
│   ├── quantum_error_correction.py
│   └── README.md
├── 05-quantum-ml/                # VQE · QNN · QAOA · quantum kernels
│   ├── quantum_ml.py
│   └── README.md
├── 06-quantum-simulation/        # H₂ · Ising · tunneling · quantum walks
│   ├── quantum_simulation.py
│   └── README.md
├── tests/                        # Full unit-test suite
├── .github/workflows/ci.yml      # CI: Python 3.9–3.13
├── requirements.txt
├── ROADMAP.md
├── CONTRIBUTING.md
├── TROUBLESHOOTING.md
└── LICENSE
```

Each module directory contains its own README with theory notes, so the main README stays clean while depth is always one click away.

---

## Suggested Learning Path

| Week | Focus | Milestone |
|------|-------|-----------|
| **1** | Modules 01–02 | Understand gates, superposition, and entanglement; modify circuits and observe outcomes |
| **2** | Module 03 | Run all six algorithms; write your own oracle for Grover's |
| **3** | Modules 04–06 | Error correction, hybrid quantum ML, and physical simulation |
| **4** | Real hardware | Deploy circuits to IBM Quantum and compare against simulator results |

The path is a guideline, not a rule — each module runs standalone if you want to jump straight to a topic.

---

## Documentation

| Document | Contents |
|----------|----------|
| [ROADMAP.md](ROADMAP.md) | Planned features and future modules |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute code, docs, or ideas |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Common setup and runtime issues |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [SECURITY.md](SECURITY.md) | Reporting vulnerabilities |

---

## Contributing

Contributions are welcome — especially:

- Jupyter notebook versions of the modules
- Additional algorithms or simulations
- Interactive visualizations
- Translations and documentation improvements

```bash
git clone https://github.com/YOUR_USERNAME/quantum-foundation.git
git checkout -b feature/your-idea
# make your changes, then open a pull request
```

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR.

---

## License

Distributed under the [MIT License](LICENSE) — free for learning, teaching, research, and commercial use.

---

<div align="center">

If this repository helped you learn quantum computing, consider giving it a **star** — it helps others find it.

Maintained by [@Aayuush1](https://github.com/Aayuush1)

</div>
