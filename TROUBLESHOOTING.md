# Troubleshooting

## Common Issues

### "ModuleNotFoundError: No module named 'qiskit'"
**Fix:** Install dependencies
```bash
pip install -r requirements.txt
```

### "SyntaxError: unterminated string literal"
**Cause:** Unicode characters in the file
**Fix:** Re-download the repository. All code is ASCII-only.

### "matplotlib is slow to import"
**Cause:** First-time import on Windows
**Fix:** Wait 10-30 seconds. Or upgrade: `pip install matplotlib --upgrade`

### "FileNotFoundError: assets/..."
**Cause:** Running from wrong directory
**Fix:** Run from the project root:
```bash
cd quantum-foundation
python 01-single-qubit-gates/single_qubit_gates.py
```

### "TypeError: plot_bloch_multivector() got unexpected keyword argument"
**Cause:** Qiskit version mismatch
**Fix:** Upgrade Qiskit: `pip install qiskit --upgrade`

### "AttributeError: 'QuantumCircuit' object has no attribute 'c_if'"
**Cause:** Old Qiskit API
**Fix:** Use `if_test` instead (already fixed in this repo)

## Still Stuck?

Open an issue with:
- Your OS and Python version
- Full error message
- What you were trying to run
