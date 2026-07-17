# Quantum Playground ⚛️

**An interactive quantum computing playground for curious people, built on real Qiskit circuits.**

No equations. No installs. No physics degree required. Just click, explore, and discover superposition, entanglement, and quantum gates the way they should be discovered: by playing with them.

🚀 **[Try it live](https://YOUR-APP-URL.streamlit.app)** &nbsp;·&nbsp; Built by [Ouarda Jodi Wilson](https://www.linkedin.com/in/YOUR-PROFILE), IBM Qiskit Advocate

<!-- Add a hero screenshot or GIF here after deploying:
![Quantum Playground](docs/screenshot-home.png)
-->

## What's inside

| Module | What you learn | The hook |
|---|---|---|
| 🪙 **1. Superposition** | A qubit can be heads *and* tails at once | Flip a real quantum coin, then tilt it to any angle on an interactive 3D Bloch sphere |
| 🎲 **2. Two Qubits** | Possibilities double with every qubit | Watch 4 outcomes exist at once, and learn why 300 qubits beat the atom count of the observable universe |
| 🔗 **3. Entanglement** | Einstein's "spooky action at a distance" | Build a Bell state and see mismatches vanish: always both heads or both tails |
| 🎛️ **4. Gates Lab** | Gates are rotations you can stack | Build your own circuits, watch the Bloch sphere respond live, and beat 5 lab challenges |

Every interaction runs a **real Qiskit circuit**, simulated exactly. The probabilities, the Bloch sphere arrow, the measurement outcomes: all of it comes straight from the statevector, not from canned animations.

## Highlights

- **Interactive 3D Bloch sphere** (Plotly): drag to rotate, tilt the qubit with a slider, verified against Qiskit's own expectation values
- **Gates Lab sandbox**: stack X, H, Z, and RY gates, see the generated Qiskit code for every circuit you build
- **Lab challenges** that sneak in deep ideas, like building an X gate out of H·Z·H and discovering phase along the way
- **Progress tracking**: mission bar and checkmarks as you complete modules
- **Show me the code** panels throughout, so curious students can graduate from clicking to coding

## Run locally

```bash
git clone https://github.com/YOUR-USERNAME/quantum_playground.git
cd quantum_playground
pip install -r requirements.txt
streamlit run Home.py
```

Requires Python 3.10+ (Qiskit is retiring 3.9 support).

## Tech

- [Qiskit](https://qiskit.org) for quantum circuit simulation (statevectors, gates, measurement sampling)
- [Streamlit](https://streamlit.io) for the interactive interface
- [Plotly](https://plotly.com/python/) for the 3D Bloch sphere
- Matplotlib for probability charts

## For teachers and outreach organizers

This app was designed for classrooms, STEM clubs, and quantum outreach events. Each module is a self-contained 10 to 15 minute lesson that works on a projector or on students' own devices. If you use it in a session, I would love to hear how it went.

## Feedback

Found a bug, have an idea, or used this with students? [Open an issue](https://github.com/YOUR-USERNAME/quantum_playground/issues) or reach out on LinkedIn. Feedback from real classrooms shapes what gets built next.

## Disclaimer

This is a personal project and is not affiliated with or endorsed by IBM. Qiskit is an open-source SDK originally developed by IBM.

## License

MIT. Use it, remix it, teach with it.
