# Quantum Playground 🪐

An interactive web app that teaches quantum computing concepts to middle and high school students using real Qiskit circuits. No equations required, just curiosity. Live at https://quantumplayground.streamlit.app/

Built by Ouarda Jouidi Wilson, IBM Qiskit Advocate.

## Modules
1. **Superposition** — The Quantum Coin. A qubit can be heads and tails at once, using a real Hadamard gate.
2. **Two Qubits**  — Superposition scales: two qubits hold four possibilities at once.
3. **Entanglement**  — Two linked qubits and Einstein's "spooky action at a distance."

## Run locally
```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Tech
- **Qiskit** for real quantum circuit simulation (Hadamard gates, statevectors, measurement)
- **Streamlit** for the interactive interface
- **Matplotlib** for probability visualizations

## Deploy
Deploys free on [Streamlit Community Cloud](https://streamlit.io/cloud) by connecting this GitHub repo.
