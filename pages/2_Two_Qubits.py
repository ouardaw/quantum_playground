"""
Quantum Playground - Module 2: Two Qubits
Shows how superposition scales: two qubits hold all four possibilities at once.
Uses real Qiskit circuits with two Hadamard gates.
"""

import streamlit as st
import random
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from quantum_style import (
    inject_quantum_css, render_hero, callout, dark_bar_chart,
    render_sidebar, mark_complete, next_module_button, coin_html,
)

st.set_page_config(page_title="Two Qubits | Quantum Playground", page_icon="🎲", layout="centered", initial_sidebar_state="expanded")
inject_quantum_css()
render_sidebar("two_qubits")

# ── Hero ───────────────────────────────────────────────────────────────────────
render_hero(
    title="🎲 MODULE 2: TWO QUBITS",
    subtitle="When superposition starts to multiply",
)

# ── Recap ──────────────────────────────────────────────────────────────────────
callout(
    "<b style='color:#ffe066;'>Quick recap from Module 1:</b> a single qubit can be heads and tails "
    "at the same time. That is superposition. Now let's see what happens with "
    "<b style='color:#f59e0b;'>two</b> of them."
)

# ── Part 1: Two normal coins ───────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🪙 Two normal coins</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="color:#d4c5f9;">
If you flip two regular coins, there are exactly four things that can happen:
heads-heads, heads-tails, tails-heads, or tails-tails.
But at any moment, you only ever get <b style="color:#ffe066;">one</b> of those four.
</div>
""", unsafe_allow_html=True)

if "classical_two" not in st.session_state:
    st.session_state.classical_two = None

if st.button("🎲 Flip two normal coins"):
    st.session_state.classical_two = (random.choice("01"), random.choice("01"))

if st.session_state.classical_two:
    bits = "".join(st.session_state.classical_two)
    coins = " ".join(coin_html(b, 72) for b in bits)
    names = {"0": "Heads", "1": "Tails"}
    label = f"{names[bits[0]]} + {names[bits[1]]}"
    st.markdown(
        f'<div class="result-display">{coins}<br>'
        f'<span style="font-family:\'Space Grotesk\',sans-serif; font-size:1.4rem; color:#f59e0b;">'
        f'{label}</span></div>',
        unsafe_allow_html=True,
    )

# ── Part 2: Two quantum coins ──────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">⚛️ Two quantum coins</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="color:#d4c5f9;">
Now we put <b style="color:#ffe066;">both</b> qubits into superposition by giving each one its own Hadamard gate.
Here is the strange part: the two qubits together are now in
<b style="color:#f59e0b;">all four possibilities at once</b>, each with an equal chance.
</div>
""", unsafe_allow_html=True)

qc = QuantumCircuit(2)
qc.h(0)
qc.h(1)
sv = Statevector(qc)
probs = sv.probabilities_dict()
ordered = {k: probs.get(k, 0.0) for k in ["00", "01", "10", "11"]}

st.code(
    "from qiskit import QuantumCircuit\n\n"
    "qc = QuantumCircuit(2)\n"
    "qc.h(0)   # put qubit 0 in superposition\n"
    "qc.h(1)   # put qubit 1 in superposition",
    language="python",
)

st.markdown('<div style="color:#a78bfa; font-size:0.95rem; margin-bottom:0.5em;">What is happening inside the two qubits right now:</div>', unsafe_allow_html=True)
st.pyplot(dark_bar_chart(ordered, "Two qubits in superposition"))

callout(
    "<b style='color:#ffe066;'>Whoa.</b> All four states (00, 01, 10, 11) exist at the same time, "
    "each at 25%. The two qubits have not decided what they are. They are exploring every "
    "possibility at once."
)

# ── Part 3: The big idea ───────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">💥 Why this is a big deal</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card">
  <div style="color:#d4c5f9; margin-bottom:0.8em;">Count the possibilities:</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.6em;">
    <div class="cosmic-card" style="padding:0.7rem; margin-bottom:0; text-align:center; border-radius:16px;">
      <div style="font-family:'Orbitron',sans-serif; color:#f59e0b; font-size:1.4rem; font-weight:700;">2</div>
      <div style="color:#a78bfa; font-size:0.85rem;">1 qubit</div>
    </div>
    <div class="cosmic-card" style="padding:0.7rem; margin-bottom:0; text-align:center; border-radius:16px;">
      <div style="font-family:'Orbitron',sans-serif; color:#f59e0b; font-size:1.4rem; font-weight:700;">4</div>
      <div style="color:#a78bfa; font-size:0.85rem;">2 qubits</div>
    </div>
    <div class="cosmic-card" style="padding:0.7rem; margin-bottom:0; text-align:center; border-radius:16px;">
      <div style="font-family:'Orbitron',sans-serif; color:#f59e0b; font-size:1.4rem; font-weight:700;">1,024</div>
      <div style="color:#a78bfa; font-size:0.85rem;">10 qubits</div>
    </div>
    <div class="cosmic-card" style="padding:0.7rem; margin-bottom:0; text-align:center; border-radius:16px;">
      <div style="font-family:'Orbitron',sans-serif; color:#ffe066; font-size:0.95rem; font-weight:700;">more than atoms in the<br>observable universe</div>
      <div style="color:#a78bfa; font-size:0.85rem;">300 qubits</div>
    </div>
  </div>
  <div style="color:#d4c5f9; margin-top:0.9em;">
    Every qubit you add <b style="color:#ffe066;">doubles</b> the number of states the system
    can hold at once. But raw possibilities are only half the story. The real trick is that
    quantum algorithms use <b style="color:#f59e0b;">interference</b> to make wrong answers
    cancel out and right answers stand out. That combination is the engine of
    quantum computing's power.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Part 4: Observe ────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🔮 What happens when we look?</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="color:#d4c5f9;">
Just like before, the moment you measure, the qubits have to choose.
All four possibilities collapse into just one. Try it a bunch of times.
</div>
""", unsafe_allow_html=True)

if "two_results" not in st.session_state:
    st.session_state.two_results = []

col1, col2 = st.columns(2)
with col1:
    if st.button("🔮 Observe both qubits!"):
        outcome = sv.sample_counts(1)
        bits = list(outcome.keys())[0]
        st.session_state.two_results.append(bits)
        mark_complete("two_qubits")
with col2:
    if st.button("🔄 Reset"):
        st.session_state.two_results = []

if st.session_state.two_results:
    latest = st.session_state.two_results[-1]
    names = {"0": "Heads", "1": "Tails"}
    coins = " ".join(coin_html(b, 72) for b in latest)
    label = f"{names[latest[0]]} + {names[latest[1]]}"
    st.markdown(
        f'<div class="result-display">{coins}<br>'
        f'<span style="font-family:\'Space Grotesk\',sans-serif; font-size:1.3rem; color:#f59e0b;">'
        f'{label} &nbsp;|{latest}⟩</span></div>',
        unsafe_allow_html=True,
    )
    tally = {s: st.session_state.two_results.count(s) for s in ["00", "01", "10", "11"]}
    total = len(st.session_state.two_results)
    st.markdown(f"""
    <div class="cosmic-card" style="text-align:center; padding:0.8rem;">
      <div style="color:#a78bfa; margin-bottom:0.4em;">Across {total} observations:</div>
      <div style="display:flex; justify-content:center; gap:1.2em; flex-wrap:wrap;">
        {"".join(f'<span style="color:#ffe066;"><b>|{s}⟩:</b> {tally[s]}</span>' for s in ["00","01","10","11"])}
      </div>
    </div>
    """, unsafe_allow_html=True)
    if total >= 12:
        callout(
            "See how all four outcomes show up roughly equally? "
            "Each measurement is random, but the equal superposition reveals itself over many tries."
        )

# ── Going deeper ───────────────────────────────────────────────────────────────
st.write("")
with st.expander("💻 Show me the full code"):
    st.code(
        """from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Two qubits
qc = QuantumCircuit(2)
qc.h(0)   # superposition on qubit 0
qc.h(1)   # superposition on qubit 1

sv = Statevector(qc)
print(sv.probabilities_dict())
# {'00': 0.25, '01': 0.25, '10': 0.25, '11': 0.25}
# all four possibilities at once!

# Observe -> collapses to ONE of the four
print(sv.sample_counts(1))  # e.g. {'10': 1}
""",
        language="python",
    )

# ── Wrap up ────────────────────────────────────────────────────────────────────
callout(
    "<b style='color:#ffe066;'>What you just learned:</b> adding qubits multiplies the possibilities "
    "a quantum system can hold at once. Two qubits, four states. The number doubles with every qubit "
    "you add, and quantum algorithms steer all those possibilities with interference to find answers."
)

st.markdown("""
<div style="text-align:center; color:#a78bfa; margin-top:0.5em;">
  Coming next: what if two qubits became <b style="color:#ffe066;">linked</b>,
  so looking at one instantly tells you the other? That is <b style="color:#f59e0b;">entanglement</b>. 🔗
</div>
""", unsafe_allow_html=True)
st.write("")
next_module_button("MODULE 3: ENTANGLEMENT 🔗", "pages/3_Entanglement.py", "next_entanglement")
st.page_link("Home.py", label="← Back to Home")
