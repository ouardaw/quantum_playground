"""
Quantum Playground — Module 1: Superposition
The Quantum Coin. Teaches superposition using a real Hadamard gate on a Qiskit statevector.
"""

import streamlit as st
import random
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from quantum_style import inject_quantum_css, render_hero, callout, dark_bar_chart, render_sidebar

st.set_page_config(page_title="Superposition | Quantum Playground", page_icon="🪙", layout="centered", initial_sidebar_state="expanded")
inject_quantum_css()
render_sidebar("superposition")

# ── Hero ───────────────────────────────────────────────────────────────────────
render_hero(
    title="🪙 MODULE 1: SUPERPOSITION",
    subtitle="The Quantum Coin",
)

# ── Part 1: Classical coin ─────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🪙 First, a normal coin</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="color:#d4c5f9;">
You know how a coin works. You flip it and it lands on heads or tails.
Before it lands it might be spinning, but the moment it stops it is one or the other.
Simple. Predictable. A little boring.
</div>
""", unsafe_allow_html=True)

if "classical_flip" not in st.session_state:
    st.session_state.classical_flip = None

if st.button("🪙 Flip a normal coin"):
    st.session_state.classical_flip = random.choice(["Heads", "Tails"])

if st.session_state.classical_flip:
    emoji = "👑" if st.session_state.classical_flip == "Heads" else "🪙"
    st.markdown(
        f'<div class="result-display">{emoji}<br>'
        f'<span style="font-family:\'Space Grotesk\',sans-serif; font-size:1.8rem; color:#f59e0b;">'
        f'{st.session_state.classical_flip}</span></div>',
        unsafe_allow_html=True,
    )

# ── Part 2: Quantum coin ───────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">⚛️ Now, the quantum coin</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="color:#d4c5f9;">
Here is where things get strange. A <b style="color:#ffe066;">qubit</b> (a quantum bit) is like a coin,
but before you look at it, it does not have to be heads OR tails.
It can be <b style="color:#ffe066;">both at the same time</b>. We call this <b style="color:#f59e0b;">superposition</b>.<br><br>
To put our qubit into superposition, we apply something called a <b style="color:#a78bfa;">Hadamard gate</b>.
Think of it as a perfect spin that leaves the coin balanced exactly between heads and tails.
</div>
""", unsafe_allow_html=True)

# Build the real quantum circuit
qc = QuantumCircuit(1)
qc.h(0)
sv = Statevector(qc)
probs = {"Heads": sv.probabilities()[0], "Tails": sv.probabilities()[1]}

st.markdown('<div class="cosmic-section" style="font-size:1.1rem;">🔧 The real quantum circuit</div>', unsafe_allow_html=True)
st.code(
    "from qiskit import QuantumCircuit\n\n"
    "qc = QuantumCircuit(1)\n"
    "qc.h(0)   # Hadamard gate → puts the qubit in superposition",
    language="python",
)

st.markdown('<div style="color:#a78bfa; font-size:0.95rem; margin-bottom:0.5em;">What is happening inside the qubit right now:</div>', unsafe_allow_html=True)
st.pyplot(dark_bar_chart(probs, "Quantum coin in superposition"))

callout(
    "<b style='color:#ffe066;'>Wait, what?</b> The qubit is sitting at "
    "<b>50% heads and 50% tails at the same time</b>. "
    "It has not decided yet. It is genuinely in both states until the moment we measure it."
)

# ── Part 3: Observe ────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🔮 So what happens when we look?</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="color:#d4c5f9;">
The instant you measure a qubit in superposition, it has to pick.
It <b style="color:#ffe066;">collapses</b> into either heads or tails, randomly.
Try it. Then try it again. You will get a different answer about half the time.
</div>
""", unsafe_allow_html=True)

if "quantum_results" not in st.session_state:
    st.session_state.quantum_results = []

col1, col2 = st.columns(2)
with col1:
    if st.button("🔮 Observe the quantum coin!"):
        outcome = sv.sample_counts(1)
        bit = list(outcome.keys())[0]
        st.session_state.quantum_results.append("Heads" if bit == "0" else "Tails")
with col2:
    if st.button("🔄 Reset"):
        st.session_state.quantum_results = []

if st.session_state.quantum_results:
    latest = st.session_state.quantum_results[-1]
    emoji = "👑" if latest == "Heads" else "🪙"
    st.markdown(
        f'<div class="result-display">{emoji}<br>'
        f'<span style="font-family:\'Space Grotesk\',sans-serif; font-size:1.8rem; color:#f59e0b;">'
        f'{latest}</span></div>',
        unsafe_allow_html=True,
    )
    heads = st.session_state.quantum_results.count("Heads")
    tails = st.session_state.quantum_results.count("Tails")
    total = heads + tails
    st.markdown(f"""
    <div class="cosmic-card" style="text-align:center; padding:0.8rem;">
      <span style="color:#a78bfa;">Results so far: </span>
      <b style="color:#ffe066;">👑 {heads} heads</b>
      <span style="color:#6b7280;"> · </span>
      <b style="color:#7c3aed;">🪙 {tails} tails</b>
      <span style="color:#6b7280;"> out of {total} observations</span>
    </div>
    """, unsafe_allow_html=True)
    if total >= 10:
        callout(
            f"Notice how it is hovering near 50/50? That is the superposition showing through. "
            f"Each single measurement is random, but over many tries the pattern appears."
        )

# ── Going deeper ───────────────────────────────────────────────────────────────
st.write("")
with st.expander("🧠 Want to go a little deeper? (The Bloch sphere)"):
    st.markdown("""
    <div style="color:#d4c5f9;">
    Scientists picture a qubit as an arrow inside a ball called the <b style="color:#ffe066;">Bloch sphere</b>.
    If the arrow points straight up, the qubit is definitely heads (0).
    Straight down means definitely tails (1).
    When our qubit is in superposition, the arrow points straight out at the <b style="color:#a78bfa;">equator</b>,
    perfectly balanced between the two and that is exactly what the Hadamard gate did.<br><br>
    Measuring the qubit forces that arrow to snap up or down, which is why you get heads or tails.
    </div>
    """, unsafe_allow_html=True)

with st.expander("💻 Show me the full code"):
    st.code(
        """from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Make a circuit with one qubit
qc = QuantumCircuit(1)

# Apply a Hadamard gate -> puts the qubit in superposition
qc.h(0)

# Look at the quantum state
sv = Statevector(qc)
print(sv.probabilities_dict())
# {'0': 0.5, '1': 0.5}  -> 50% heads, 50% tails!

# "Observe" the qubit -> it collapses to 0 or 1
outcome = sv.sample_counts(1)
print(outcome)  # {'0': 1} or {'1': 1}, randomly
""",
        language="python",
    )

# ── Wrap up ────────────────────────────────────────────────────────────────────
callout(
    "<b style='color:#ffe066;'>What you just learned:</b> A qubit can be in two states at once (superposition), "
    "and measuring it forces it to choose. This one idea is the foundation of everything "
    "quantum computers can do. Pretty wild for a coin, right?"
)

st.markdown("""
<div style="text-align:center; color:#a78bfa; margin-top:0.5em;">
  Coming next: what happens when you have <b style="color:#ffe066;">two</b> quantum coins at once? 🎲
</div>
""", unsafe_allow_html=True)
st.write("")
st.page_link("Home.py", label="← Back to Home")
