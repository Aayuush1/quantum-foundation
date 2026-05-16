<!-- <p align="center">
  <img src="https://raw.githubusercontent.com/aayuush1/quantum-foundation/main/assets/quantum-banner.gif" width="100%" alt="Quantum Computing Banner">
</p> -->

<h1 align="center">
  <img src="https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif" width="40">
  QUANTUM FOUNDATIONS
  <img src="https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif" width="40">
</h1>

<p align="center">
  <b>Where Classical Computing Ends, Quantum Computing Begins</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Qiskit-1.0%2B-6929C4?style=for-the-badge&logo=ibm&logoColor=white">
  <img src="https://img.shields.io/badge/Quantum-Computing-FF6F00?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge">
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=aayuush1-quantum&label=Repo%20Views&color=0e75b6&style=flat" alt="Repo Views">
  <img src="https://img.shields.io/github/stars/aayuush1/quantum-foundation?style=social" alt="Stars">
  <img src="https://img.shields.io/github/forks/aayuush1/quantum-foundation?style=social" alt="Forks">
</p>

---

## 🌌 THE QUANTUM JOURNEY

```
    ┌─────────────────────────────────────────────────────────┐
    │  CLASSICAL WORLD              QUANTUM WORLD             │
    │                                                         │
    │  Bit = 0 or 1      ───►     Qubit = |0⟩ + |1⟩            │
    │  Deterministic     ───►     Probabilistic               │
    │  Sequential        ───►     Parallel (Superposition)    │
    │  Local             ───►     Entangled (Spooky!)         │
    └─────────────────────────────────────────────────────────┘
```

> **"If quantum mechanics hasn't profoundly shocked you, you haven't understood it yet."**
> — *Niels Bohr*

---

## ⚡ QUICK START — RUN IN 30 SECONDS

```bash
# 1. Clone the quantum realm
git clone https://github.com/aayuush1/quantum-foundation.git
cd quantum-foundation

# 2. Install the quantum toolkit
pip install -r requirements.txt

# 3. FIRE THE FIRST CIRCUIT!
python 01-single-qubit-gates/single_qubit_gates.py
```

**Expected output:**
```
[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]
QUANTUM FOUNDATIONS: SINGLE QUBIT GATES
[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]

============================================================
1.1 X GATE (Quantum NOT)
============================================================
Measurement results (1000 shots): {'1': 1000}
-> X gate flipped |0⟩ to |1⟩ 100% of the time!
```

---

## 🗺️ THE COMPLETE ROADMAP

| Module | Topic | Concepts | Difficulty | Run |
|--------|-------|----------|------------|-----|
| **01** | Single Qubit Gates | X, H, Y, Z, S, T, Bloch Sphere, Rotations | ⭐ Beginner | `python 01-single-qubit-gates/single_qubit_gates.py` |
| **02** | Multi-Qubit Gates | CNOT, SWAP, Toffoli, Bell States, Entanglement, Teleportation | ⭐⭐ Intermediate | `python 02-multi-qubit-gates/multi_qubit_gates.py` |
| **03** | Quantum Algorithms | Deutsch-Jozsa, Grover's, Shor's, QFT, QPE, Bernstein-Vazirani | ⭐⭐⭐ Advanced | `python 03-quantum-algorithms/quantum_algorithms.py` |
| **04** | Error Correction | Bit Flip, Phase Flip, Shor Code, Threshold Theorem | ⭐⭐⭐ Advanced | `python 04-quantum-error-correction/quantum_error_correction.py` |
| **05** | Quantum ML | VQE, QNN, Feature Maps, QAOA, Quantum Kernels | ⭐⭐⭐⭐ Expert | `python 05-quantum-ml/quantum_ml.py` |
| **06** | Quantum Simulation | Harmonic Oscillator, Ising Model, Tunneling, Random Walks | ⭐⭐⭐⭐ Expert | `python 06-quantum-simulation/quantum_simulation.py` |

---

## 🎯 WHAT YOU WILL MASTER

### Module 01 — Single Qubit Gates
```
|0⟩ ──[X]──► |1⟩          NOT Gate
|0⟩ ──[H]──► |+⟩          SUPERPOSITION
|1⟩ ──[Z]──► -|1⟩         PHASE FLIP
|0⟩ ──[Y]──► i|1⟩         COMBINED GATE
```

**Key Insight:** The Hadamard gate (H) is the **magic gate** that creates superposition — the heart of quantum speedup.

---

### Module 02 — Entanglement (Spooky Action!)
```
Alice                    Bob
  |0⟩ ──[H]──┐            ┌──[M]──► ?
             ├──[CNOT]───┤
  |0⟩ ───────┘            └──[M]──► ?

Result: Measuring Alice INSTANTLY determines Bob's state!
Distance doesn't matter. Einstein called it "spooky action at a distance."
```

**Key Insight:** Entangled qubits are correlated even if they're light-years apart. This powers quantum communication.

---

### Module 03 — Quantum Algorithms (The Speedups!)

| Algorithm | Classical | Quantum | Speedup | Impact |
|-----------|-----------|---------|---------|--------|
| **Deutsch-Jozsa** | 2^(n-1)+1 queries | **1 query** | Exponential | First quantum speedup proven |
| **Grover's Search** | N queries | **sqrt(N)** | Quadratic | Database search, SAT solvers |
| **Shor's Algorithm** | Sub-exponential | **Polynomial** | Exponential | **Breaks RSA encryption!** |
| **QPE** | Exponential | **Polynomial** | Exponential | Chemistry, materials science |

**Key Insight:** Shor's algorithm threatens modern encryption. This is why the world is racing to build quantum computers AND post-quantum cryptography.

---

### Module 04 — Quantum Error Correction

```
Logical Qubit          Physical Qubits
    |1⟩     ───►    |111⟩  (3 qubits)
                     ↑↑↑
                   Bit Flip Code

    If one flips:   |101⟩  
    Majority vote:  → |1⟩   (corrected!)
```

**Key Insight:** The No-Cloning Theorem says you can't copy quantum states. So classical backup strategies don't work. We encode 1 logical qubit into 3+ physical qubits instead.

---

### Module 05 — Quantum Machine Learning

```
Classical Data ──► Quantum Feature Map ──► Quantum Kernel ──► Classical Optimizer
      ↑                                              ↓
      └────────────── Hybrid Loop ◄──────────────────┘
```

**Key Insight:** VQE (Variational Quantum Eigensolver) is already being used by companies like BMW and Roche to simulate molecules for battery and drug research.

---

### Module 06 — Quantum Simulation

**Feynman's Original Dream:** *"Nature isn't classical, dammit, and if you want to make a simulation of nature, you'd better make it quantum mechanical."*

Simulate:
- ⚛️ H2 molecule ground state energy
- 🧲 Ising model magnetism
- 🚇 Quantum tunneling (classically impossible!)
- 🎲 Quantum random walks (quadratically faster)

---

## 🛠️ TECH STACK

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" height="30">
  <img src="https://img.shields.io/badge/Qiskit-6929C4?style=flat-square&logo=ibm&logoColor=white" height="30">
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" height="30">
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white" height="30">
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" height="30">
</p>

---

## 📊 REPOSITORY STATS

```
Total Modules:        6
Total Lines of Code:  ~2000+
Quantum Gates Covered: 15+
Algorithms Implemented: 6
Tests Included:       Yes (tests/)
CI/CD:               GitHub Actions
Python Versions:     3.9, 3.10, 3.11, 3.12, 3.13
```

---

## 🧪 RUN THE TESTS

```bash
# Run all unit tests
python -m pytest tests/

# Or run individual test file
python tests/test_all.py
```

**Test coverage includes:**
- ✅ X, H, Y, Z gate operations
- ✅ Superposition verification
- ✅ CNOT and entanglement
- ✅ Bell state generation
- ✅ SWAP gate
- ✅ Deutsch-Jozsa algorithm
- ✅ Grover's search
- ✅ VQE ground state
- ✅ Quantum kernel computation

---

## 🎓 LEARNING PATH

```
WEEK 1: FOUNDATIONS
  Day 1-2: Run Module 01 (Single Qubit Gates)
  Day 3-4: Run Module 02 (Multi-Qubit & Entanglement)
  Day 5-7: Modify circuits, add gates, break things!

WEEK 2: ALGORITHMS
  Day 8-10: Run Module 03 (Quantum Algorithms)
  Day 11-12: Implement your own oracle for Grover's
  Day 13-14: Try different targets, measure success rates

WEEK 3: ADVANCED
  Day 15-17: Run Module 04 (Error Correction)
  Day 18-19: Run Module 05 (Quantum ML)
  Day 20-21: Run Module 06 (Simulation)

WEEK 4: MASTERY
  Day 22+: Run on REAL IBM Quantum hardware!
  Go to: https://quantum-computing.ibm.com/
```

---

## 🌟 WHY THIS REPO?

| Feature | Most Tutorials | This Repo |
|---------|---------------|-----------|
| Working code | ❌ Often broken | ✅ All tested |
| Qiskit 1.0+ compatible | ❌ Outdated | ✅ Latest API |
| ASCII-only (no Unicode bugs) | ❌ Emojis break Windows | ✅ Cross-platform |
| Unit tests | ❌ Missing | ✅ Included |
| CI/CD pipeline | ❌ Missing | ✅ GitHub Actions |
| Complete learning path | ❌ Fragmented | ✅ 6 modules, progressive |
| Real quantum hardware ready | ❌ Simulator only | ✅ IBM Quantum compatible |

---

## 🚀 RUN ON REAL QUANTUM HARDWARE

```python
# Replace this:
simulator = AerSimulator()

# With IBM Quantum backend:
from qiskit_ibm_runtime import QiskitRuntimeService
service = QiskitRuntimeService(channel="ibm_quantum", token="YOUR_TOKEN")
backend = service.least_busy(operational=True, simulator=False)
```

**Get your free IBM Quantum token:** https://quantum-computing.ibm.com/

---

## 🤝 CONTRIBUTE

```bash
# 1. Fork
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/quantum-foundation.git

# 3. Create branch
git checkout -b feature/amazing-idea

# 4. Make magic
# 5. Push and PR!
```

**Ideas welcome:**
- Jupyter notebook versions
- New quantum algorithms
- Interactive visualizations
- Video tutorials
- Translations

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📜 LICENSE

MIT License — use freely for learning, teaching, research, or commercial projects.

---

<p align="center">
  <img src="https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif" width="200">
</p>

<p align="center">
  <b>Built with curiosity, caffeine, and quantum entanglement</b><br>
  <a href="https://github.com/aayuush1">@aayuush1</a>
</p>

<p align="center">
  ⭐ Star this repo if it helped you learn quantum computing! ⭐
</p>
