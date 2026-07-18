"""
Quantum Playground - Module 4: Gates Lab
An interactive sandbox: stack real quantum gates on a qubit and watch the
Bloch sphere arrow and probabilities respond live. Uses real Qiskit circuits.
"""

import streamlit as st
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from quantum_style import (
    inject_quantum_css, render_hero, callout, dark_bar_chart,
    render_sidebar, bloch_sphere_fig, bloch_2d_fig, mark_complete, coin_html,
    render_stepper,
)

st.set_page_config(page_title="Gates Lab | Quantum Playground", page_icon="🎛️", layout="centered", initial_sidebar_state="expanded")
inject_quantum_css()
render_sidebar("gates_lab")


MAX_GATES = 8

# ── Hero ───────────────────────────────────────────────────────────────────────
render_hero(
    title="🎛️ MODULE 4: GATES LAB",
    subtitle="Take the controls: build your own quantum circuit",
)
render_stepper("gates_lab")

# ── Intro ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cosmic-card" style="color:#d4c5f9;">
Quantum <b style="color:#ffe066;">gates</b> are the moves of quantum computing. Each one
rotates the qubit's arrow on the Bloch sphere in its own special way.
Stack gates below and watch the arrow and the probabilities respond
<b style="color:#f59e0b;">instantly</b>. Every click builds a real Qiskit circuit.
</div>
""", unsafe_allow_html=True)

# ── Gate palette ───────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🧰 Your gate toolbox</div>', unsafe_allow_html=True)

if "lab_gates" not in st.session_state:
    st.session_state.lab_gates = []

gates_full = len(st.session_state.lab_gates) >= MAX_GATES

g1, g2, g3 = st.columns(3)
with g1:
    if st.button("➕ X: FLIP", key="add_x", use_container_width=True, disabled=gates_full):
        st.session_state.lab_gates.append(("x", None))
with g2:
    if st.button("➕ H: SPLIT", key="add_h", use_container_width=True, disabled=gates_full):
        st.session_state.lab_gates.append(("h", None))
with g3:
    if st.button("➕ Z: PHASE", key="add_z", use_container_width=True, disabled=gates_full):
        st.session_state.lab_gates.append(("z", None))

ry_col1, ry_col2 = st.columns([2, 1])
with ry_col1:
    ry_angle = st.slider("RY tilt angle (degrees)", 0, 180, 45, 5, key="ry_angle")
with ry_col2:
    st.write("")
    if st.button(f"➕ RY({ry_angle}°)", key="add_ry", use_container_width=True, disabled=gates_full):
        st.session_state.lab_gates.append(("ry", ry_angle))

u1, u2 = st.columns(2)
with u1:
    if st.button("↩️ Undo last gate", key="undo", use_container_width=True,
                 disabled=len(st.session_state.lab_gates) == 0):
        st.session_state.lab_gates.pop()
with u2:
    if st.button("🔄 Clear circuit", key="clear", use_container_width=True,
                 disabled=len(st.session_state.lab_gates) == 0):
        st.session_state.lab_gates = []

if gates_full:
    st.markdown('<div style="color:#f59e0b; text-align:center; font-size:0.9rem;">🛑 Circuit full (8 gates max). Undo or clear to keep building.</div>', unsafe_allow_html=True)

# ── Build the real circuit ─────────────────────────────────────────────────────
qc = QuantumCircuit(1)
for gate, arg in st.session_state.lab_gates:
    if gate == "x":
        qc.x(0)
    elif gate == "h":
        qc.h(0)
    elif gate == "z":
        qc.z(0)
    elif gate == "ry":
        qc.ry(np.radians(arg), 0)
sv = Statevector(qc)
p_heads, p_tails = sv.probabilities()

# Mark module complete once they've experimented with 2+ gates
if len(st.session_state.lab_gates) >= 2:
    mark_complete("gates_lab")

# ── Circuit display ────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🔬 Your circuit right now</div>', unsafe_allow_html=True)

if st.session_state.lab_gates:
    chips = []
    for gate, arg in st.session_state.lab_gates:
        label = f"RY({arg}°)" if gate == "ry" else gate.upper()
        chips.append(
            f'<span style="display:inline-block; background:linear-gradient(135deg,#7c3aed,#3a86ff); '
            f'color:#fff; font-family:Orbitron,sans-serif; font-weight:700; font-size:0.9rem; '
            f'padding:0.4em 0.8em; margin:0.15em; border-radius:8px; '
            f'box-shadow:0 3px 0 #5b21b6, 0 0 10px rgba(124,58,237,0.4);">{label}</span>'
        )
    st.markdown(f"""
    <div class="cosmic-card" style="text-align:center; padding:0.9rem;">
      <span style="color:#a78bfa; font-family:'Orbitron',sans-serif; font-size:0.85rem;">|0⟩ →</span>
      {' <span style="color:#6b7280;">→</span> '.join(chips)}
      <span style="color:#a78bfa; font-family:'Orbitron',sans-serif; font-size:0.85rem;">→ 📏</span>
    </div>
    """, unsafe_allow_html=True)

    code_lines = ["from qiskit import QuantumCircuit", "import numpy as np", "", "qc = QuantumCircuit(1)"]
    for gate, arg in st.session_state.lab_gates:
        if gate == "ry":
            code_lines.append(f"qc.ry(np.radians({arg}), 0)")
        else:
            code_lines.append(f"qc.{gate}(0)")
    with st.expander("💻 See this circuit as Qiskit code"):
        st.code("\n".join(code_lines), language="python")
else:
    st.markdown("""
    <div class="cosmic-card" style="text-align:center; padding:0.9rem; color:#a78bfa;">
      Your circuit is empty. The qubit starts as <b style="color:#ffe066;">|0⟩ (heads)</b>.
      Add a gate above to get started!
    </div>
    """, unsafe_allow_html=True)

# ── Live state: sphere + probabilities ─────────────────────────────────────────
use_2d = st.toggle("Sphere not showing? Switch to the 2D view", key="bloch_2d_lab")
if use_2d:
    st.pyplot(bloch_2d_fig(sv, title="Live Bloch view: the arrow IS your qubit"))
    st.markdown(
        '<div style="color:#6b7280; font-size:0.82rem; text-align:center;">'
        'Nothing is hidden in this flat view: X, H, Z, and RY always keep '
        'the arrow in this slice of the sphere.</div>',
        unsafe_allow_html=True,
    )
else:
    st.plotly_chart(
        bloch_sphere_fig(sv, title="Live Bloch sphere: the arrow IS your qubit"),
        use_container_width=True,
        config={"displayModeBar": False},
    )

st.pyplot(dark_bar_chart({"Heads": p_heads, "Tails": p_tails}, "Measurement chances right now"))

# ── Measure ────────────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🔮 Measure it!</div>', unsafe_allow_html=True)

if "lab_results" not in st.session_state:
    st.session_state.lab_results = []

m1, m2 = st.columns(2)
with m1:
    if st.button("🔮 Measure the qubit!", key="lab_measure", use_container_width=True):
        outcome = sv.sample_counts(1)
        bit = list(outcome.keys())[0]
        st.session_state.lab_results.append("Heads" if bit == "0" else "Tails")
with m2:
    if st.button("🔄 Reset tally", key="lab_reset", use_container_width=True):
        st.session_state.lab_results = []

if st.session_state.lab_results:
    latest = st.session_state.lab_results[-1]
    st.markdown(
        f'<div class="result-display">{coin_html(latest, 84)}<br>'
        f'<span style="font-family:\'Space Grotesk\',sans-serif; font-size:1.8rem; color:#f59e0b;">'
        f'{latest}</span></div>',
        unsafe_allow_html=True,
    )
    heads = st.session_state.lab_results.count("Heads")
    tails = st.session_state.lab_results.count("Tails")
    st.markdown(f"""
    <div class="cosmic-card" style="text-align:center; padding:0.8rem;">
      {coin_html("H", 26)} <b style="color:#ffe066;">{heads}</b>
      <span style="color:#6b7280;"> · </span>
      {coin_html("T", 26)} <b style="color:#a78bfa;">{tails}</b>
      <span style="color:#6b7280;"> out of {heads + tails} measurements of this circuit</span>
    </div>
    """, unsafe_allow_html=True)

# ── Gate reference ─────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">📖 What does each gate do?</div>', unsafe_allow_html=True)

r1, r2 = st.columns(2)
for col, icon, name, desc in [
    (r1, "🔃", "X: the flip", "Flips heads ↔ tails. On the sphere: spins the arrow half-way around, pole to pole. The quantum version of NOT."),
    (r2, "🪄", "H: the split", "Makes superposition! Sends heads to the equator (50/50). Apply it twice and it undoes itself. That is interference at work."),
    (r1, "👻", "Z: the phase flip", "Sneaky: it does not change the chances at all. It spins the arrow around the equator. Invisible alone, but it changes how gates after it combine."),
    (r2, "🎚️", "RY: the tilt", "Your precision dial. Tilts the arrow by any angle you choose, giving lopsided superpositions like 80/20."),
]:
    with col:
        st.markdown(f"""
        <div class="cosmic-card" style="padding:0.9rem; min-height:150px;">
          <div style="font-family:'Orbitron',sans-serif; font-size:0.95rem; color:#f59e0b; margin-bottom:0.4em;">
            {icon} {name}
          </div>
          <div style="color:#d4c5f9; font-size:0.88rem;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ── Challenges ─────────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🏆 Lab challenges</div>', unsafe_allow_html=True)

callout(
    "<b style='color:#ffe066;'>Can you…</b><br>"
    "1️⃣ Make the qubit <b>100% tails</b>? (one gate does it)<br>"
    "2️⃣ Get a perfect <b>50/50</b> without using RY?<br>"
    "3️⃣ Apply <b>H twice in a row</b>. Why does the second H undo the first? "
    "That cancelation is <b style='color:#f59e0b;'>interference</b>, the engine of quantum algorithms!<br>"
    "4️⃣ Build <b>H → Z → H</b> and look at the result. You just built an X gate out of "
    "other gates, and the 'invisible' Z was the secret ingredient. 👻<br>"
    "5️⃣ Make a qubit that lands heads about <b>85%</b> of the time. (hint: RY at a small angle)"
)

# ── Wrap up ────────────────────────────────────────────────────────────────────
st.write("---")
callout(
    "<b style='color:#ffe066;'>What you just learned:</b> gates rotate a qubit's arrow on the "
    "Bloch sphere, and stacking them builds circuits. Some gates (like Z) change nothing you can "
    "see on their own but everything about how the circuit combines. That hidden phase, plus "
    "interference, is exactly what real quantum algorithms are made of."
)

# ── What's next ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cosmic-card" style="text-align:center; padding:1.2rem 1rem;">
  <div style="font-size:2rem; margin-bottom:0.3em;">🚀</div>
  <div style="font-family:'Orbitron',sans-serif; color:#f59e0b; font-size:1rem;
              letter-spacing:0.1em; margin-bottom:0.6em;">READY FOR THE REAL THING?</div>
  <div style="color:#d4c5f9; font-size:0.95rem;">
    You have been building real Qiskit circuits this whole time. The next step is
    <a href="https://quantum.ibm.com/composer" target="_blank"
       style="color:#ffe066; font-weight:700;">IBM Quantum Composer</a>,
    where you can build bigger circuits with the full gate set and run them on
    <b style="color:#ffe066;">actual quantum computers</b>
    (a free IBM account includes limited time on real devices).
    The same ideas carry over, with one exciting twist: real hardware is
    <b style="color:#f59e0b;">noisy</b>, so your perfect 50/50 might come out 48/52.
    Spotting that noise is part of the fun, and taming it is one of the biggest
    open challenges in quantum computing.
  </div>
</div>
""", unsafe_allow_html=True)

st.page_link("Home.py", label="← Back to Home")
