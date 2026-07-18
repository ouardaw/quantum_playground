"""
Quantum Playground - Module 1: Superposition
The Quantum Coin. Teaches superposition using a real Hadamard gate on a Qiskit statevector.
"""

import streamlit as st
import random
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from quantum_style import (
    inject_quantum_css, render_hero, callout,
    dark_bar_chart, render_sidebar, bloch_sphere_fig, bloch_2d_fig,
    mark_complete, next_module_button, coin_html,
)

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
    st.markdown(
        f'<div class="result-display">{coin_html(st.session_state.classical_flip, 84)}<br>'
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
        mark_complete("superposition")
with col2:
    if st.button("🔄 Reset"):
        st.session_state.quantum_results = []

if st.session_state.quantum_results:
    latest = st.session_state.quantum_results[-1]
    st.markdown(
        f'<div class="result-display">{coin_html(latest, 84)}<br>'
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
      {coin_html("H", 26)} <b style="color:#ffe066;">{heads} heads</b>
      <span style="color:#6b7280;"> · </span>
      {coin_html("T", 26)} <b style="color:#a78bfa;">{tails} tails</b>
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
with st.expander("🧠 Want to go a little deeper? (The Bloch sphere)", expanded=False):
    st.markdown("""
    <div style="color:#d4c5f9;">
    Scientists picture a qubit as an arrow inside a ball called the <b style="color:#ffe066;">Bloch sphere</b>.
    If the arrow points straight up, the qubit is definitely heads (0).
    Straight down means definitely tails (1).
    When our qubit is in superposition, the arrow points straight out at the <b style="color:#a78bfa;">equator</b>,
    perfectly balanced between the two. That is exactly what the Hadamard gate did.<br><br>
    Measuring the qubit forces that arrow to snap up or down, which is why you get heads or tails.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="cosmic-section" style="font-size:1.05rem;">🕹️ Try it yourself: tilt the qubit!</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="color:#d4c5f9; font-size:0.95rem; margin-bottom:0.4em;">
    Drag the slider to rotate the qubit's arrow from heads (0°) to tails (180°).
    The sphere below is <b style="color:#ffe066;">interactive</b>, so drag it to spin it around!
    </div>
    """, unsafe_allow_html=True)

    theta_deg = st.slider("Rotation angle θ (degrees)", 0, 180, 90, 5)
    qc_tilt = QuantumCircuit(1)
    qc_tilt.ry(np.radians(theta_deg), 0)
    sv_tilt = Statevector(qc_tilt)
    p_heads, p_tails = sv_tilt.probabilities()

    use_2d = st.toggle("Sphere not showing? Switch to the 2D view", key="bloch_2d_m1")
    if use_2d:
        st.pyplot(bloch_2d_fig(sv_tilt, title=f"θ = {theta_deg}°: the arrow IS the qubit"))
        st.markdown(
            '<div style="color:#6b7280; font-size:0.82rem; text-align:center;">'
            'Nothing is hidden in this flat view: the gates in this app always keep '
            'the arrow in this slice of the sphere.</div>',
            unsafe_allow_html=True,
        )
    else:
        st.plotly_chart(
            bloch_sphere_fig(sv_tilt, title=f"θ = {theta_deg}°: the arrow IS the qubit"),
            use_container_width=True,
            config={"displayModeBar": False},
        )

    st.markdown(f"""
    <div class="cosmic-card" style="text-align:center; padding:0.8rem;">
      <span style="color:#ffe066; font-size:1.1rem;">👑 Heads: <b>{p_heads*100:.0f}%</b></span>
      <span style="color:#6b7280;"> · </span>
      <span style="color:#a78bfa; font-size:1.1rem;">🪙 Tails: <b>{p_tails*100:.0f}%</b></span>
    </div>
    """, unsafe_allow_html=True)

    if theta_deg == 0:
        st.markdown('<div style="color:#a78bfa; text-align:center;">Arrow at the north pole → definitely heads. No quantum weirdness yet.</div>', unsafe_allow_html=True)
    elif theta_deg == 180:
        st.markdown('<div style="color:#a78bfa; text-align:center;">Arrow at the south pole → definitely tails.</div>', unsafe_allow_html=True)
    elif theta_deg == 90:
        st.markdown('<div style="color:#ffe066; text-align:center;">⭐ The equator! Perfect 50/50 superposition, exactly what the Hadamard gate does.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="color:#a78bfa; text-align:center;">A <b>lopsided</b> superposition, still both at once, but leaning one way. Qubits can be tilted to any angle!</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="callout-quantum" style="margin-top:0.8em;">
    <b style="color:#ffe066;">One more secret:</b> a qubit in superposition is not just a hidden
    coin flip. The <i>direction</i> the arrow points around the equator (called the
    <b style="color:#a78bfa;">phase</b>) also matters, and it lets qubits <b>interfere</b> with
    each other like waves, adding up or canceling out. No ordinary coin can do that,
    and it is where quantum computers get their real power.
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
next_module_button("MODULE 2: TWO QUBITS 🎲", "pages/2_Two_Qubits.py", "next_two_qubits")
st.page_link("Home.py", label="← Back to Home")
