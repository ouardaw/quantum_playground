"""
Quantum Playground — Module 3: Entanglement
The "spooky action at a distance." Two qubits linked with a Hadamard + CNOT (Bell state),
so measuring one instantly determines the other. Uses real Qiskit circuits.
"""

import streamlit as st
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from quantum_style import inject_quantum_css, render_hero, callout, dark_bar_chart, render_sidebar

st.set_page_config(page_title="Entanglement | Quantum Playground", page_icon="🔗", layout="centered", initial_sidebar_state="expanded")
inject_quantum_css()
render_sidebar("entanglement")

# ── Hero ───────────────────────────────────────────────────────────────────────
render_hero(
    title="🔗 MODULE 3: ENTANGLEMENT",
    subtitle="The spookiest thing in all of physics",
)

# ── Recap ──────────────────────────────────────────────────────────────────────
callout(
    "<b style='color:#ffe066;'>Recap:</b> Two qubits in superposition can be in all four states "
    "(00, 01, 10, 11) at once. Now we are going to <b style='color:#f59e0b;'>link</b> them "
    "so they can never disagree."
)

# ── Part 1: The setup ──────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🔧 Linking two qubits</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="color:#d4c5f9;">
We start the same way as before, putting the first qubit into superposition with a
<b style="color:#a78bfa;">Hadamard gate</b>.
Then we add one new move: a <b style="color:#ffe066;">CNOT gate</b>.
A CNOT ties the second qubit to the first, so the second one copies whatever the first becomes.<br><br>
Once we do this, the two qubits are <b style="color:#f59e0b;">entangled</b>. They are no longer two
separate coins — they are one linked system with a shared fate.
</div>
""", unsafe_allow_html=True)

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
sv = Statevector(qc)
probs = sv.probabilities_dict()
ordered = {k: probs.get(k, 0.0) for k in ["00", "01", "10", "11"]}

st.code(
    "from qiskit import QuantumCircuit\n\n"
    "qc = QuantumCircuit(2)\n"
    "qc.h(0)        # put qubit 0 in superposition\n"
    "qc.cx(0, 1)    # CNOT: entangle qubit 1 with qubit 0",
    language="python",
)

st.markdown('<div style="color:#a78bfa; font-size:0.95rem; margin-bottom:0.5em;">Look at what is possible now:</div>', unsafe_allow_html=True)
st.pyplot(dark_bar_chart(ordered, "Entangled qubits — a Bell state"))

callout(
    "<b style='color:#ffe066;'>Look closely.</b> Only <b>|00⟩</b> and <b>|11⟩</b> are possible, each at 50%. "
    "The states 01 and 10 are simply <b style='color:#f59e0b;'>gone</b>. The two qubits will always come "
    "out matching: either both heads, or both tails. Never one of each."
)

# ── Part 2: Observe ────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🔮 Now measure just ONE of them</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="color:#d4c5f9;">
Here is the spooky part. Even though each qubit is still random, the moment you measure
<b style="color:#ffe066;">one</b> of them, the <b style="color:#f59e0b;">other</b> one instantly
locks into the same value. It does not matter if they are right next to each other or on opposite
sides of the galaxy. Measure one, and you instantly know the other.
</div>
""", unsafe_allow_html=True)

if "ent_results" not in st.session_state:
    st.session_state.ent_results = []

col1, col2 = st.columns(2)
with col1:
    if st.button("🔮 Measure the first qubit!"):
        outcome = sv.sample_counts(1)
        bits = list(outcome.keys())[0]
        st.session_state.ent_results.append(bits)
with col2:
    if st.button("🔄 Reset"):
        st.session_state.ent_results = []

if st.session_state.ent_results:
    latest = st.session_state.ent_results[-1]
    names = {"0": "Heads", "1": "Tails"}
    first, second = names[latest[0]], names[latest[1]]
    coins = " ".join("👑" if b == "0" else "🪙" for b in latest)
    st.markdown(
        f'<div class="result-display">{coins}<br>'
        f'<span style="font-family:\'Space Grotesk\',sans-serif; font-size:1.2rem; color:#f59e0b;">'
        f'First: {first} → Second instantly: {second}</span></div>',
        unsafe_allow_html=True,
    )

    tally = {s: st.session_state.ent_results.count(s) for s in ["00", "01", "10", "11"]}
    total = len(st.session_state.ent_results)
    st.markdown(f"""
    <div class="cosmic-card" style="text-align:center; padding:0.8rem;">
      <div style="color:#a78bfa; margin-bottom:0.4em;">Across {total} measurements:</div>
      <div style="display:flex; justify-content:center; gap:1.2em; flex-wrap:wrap;">
        {"".join(f'<span style="color:#ffe066;"><b>|{s}⟩:</b> {tally[s]}</span>' for s in ["00","01","10","11"])}
      </div>
    </div>
    """, unsafe_allow_html=True)
    if tally["01"] == 0 and tally["10"] == 0 and total >= 6:
        callout(
            "Notice you have gotten <b style='color:#ffe066;'>zero mismatches</b>. "
            "No 01, no 10. The qubits are perfectly correlated. That is entanglement."
        )

# ── Part 3: Why it matters ─────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🌌 Why this matters</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="color:#d4c5f9;">
Einstein hated this. He called it <b style="color:#ffe066;">"spooky action at a distance"</b> because
it seemed impossible that two particles could be so perfectly linked.
But experiments have proven it real, over and over, for decades.
In 2022 the Nobel Prize in Physics was awarded for exactly this kind of work.<br><br>
Entanglement is not just a curiosity. It is the foundation of:
</div>
""", unsafe_allow_html=True)

col_a, col_b, col_c = st.columns(3)
for col, icon, title, desc in [
    (col_a, "💻", "Quantum Computing", "Entangled qubits work together in ways normal bits never could"),
    (col_b, "🔐", "Quantum Encryption", "Unbreakable codes that reveal if anyone is eavesdropping"),
    (col_c, "🚀", "Quantum Teleportation", "Moving a quantum state from one place to another using entanglement"),
]:
    with col:
        st.markdown(f"""
        <div class="cosmic-card" style="text-align:center; padding:0.9rem; margin-bottom:0.5rem;">
          <div style="font-size:1.8rem;">{icon}</div>
          <div style="font-family:'Orbitron',sans-serif; font-size:0.8rem; color:#f59e0b;
                      margin:0.3em 0; letter-spacing:0.06em;">{title}</div>
          <div style="color:#a78bfa; font-size:0.82rem;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ── Going deeper ───────────────────────────────────────────────────────────────
st.write("")
with st.expander("💻 Show me the full code"):
    st.code(
        """from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Entangle two qubits into a Bell state
qc = QuantumCircuit(2)
qc.h(0)        # superposition on qubit 0
qc.cx(0, 1)    # CNOT links qubit 1 to qubit 0

sv = Statevector(qc)
print(sv.probabilities_dict())
# {'00': 0.5, '11': 0.5}
# only matching outcomes are possible!

# Measure -> always 00 or 11, never 01 or 10
print(sv.sample_counts(1))  # e.g. {'11': 1}
""",
        language="python",
    )

with st.expander("🤔 Wait, is anything traveling faster than light?"):
    st.markdown("""
    <div style="color:#d4c5f9;">
    Great question — and the answer is <b style="color:#ffe066;">no</b>.
    Even though the qubits match instantly, you cannot use entanglement to send a message
    faster than light, because the outcome of each measurement is still random.
    You only discover the link <b style="color:#a78bfa;">after</b> you compare notes the normal way.
    The universe is strange, but it still plays fair.
    </div>
    """, unsafe_allow_html=True)

# ── Wrap up ────────────────────────────────────────────────────────────────────
callout(
    "<b style='color:#ffe066;'>What you just learned:</b> two qubits can be entangled so their results "
    "are perfectly linked, no matter how far apart they are. Measure one and you instantly know the other. "
    "This is one of the deepest and most useful ideas in all of science."
)

st.markdown("""
<div class="cosmic-card" style="text-align:center; padding:1.3rem 1rem;">
  <div style="font-size:2.2rem; margin-bottom:0.4em;">🪐</div>
  <div style="font-family:'Orbitron',sans-serif; color:#f59e0b; font-size:1rem;
              letter-spacing:0.1em; margin-bottom:0.6em;">YOU DID IT.</div>
  <div style="color:#d4c5f9;">
    You have now explored superposition, how it scales across qubits, and entanglement —
    the three ideas at the very heart of quantum computing.
    That is more than most adults will ever understand about the quantum world.
    <b style="color:#ffe066;">Welcome to the future.</b>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.page_link("Home.py", label="← Back to Home")
