"""
Quantum Playground - Home
An interactive web app to teach quantum computing concepts.
Built by Ouarda Wilson, IBM Qiskit Advocate.
"""

import streamlit as st
from quantum_style import inject_quantum_css, render_hero, cosmic_card, callout, render_sidebar

st.set_page_config(
    page_title="Quantum Playground",
    page_icon="⚛️",
    layout="centered",
    initial_sidebar_state="expanded",
)

inject_quantum_css()
render_sidebar("home")

# ── Hero ───────────────────────────────────────────────────────────────────────
render_hero(
    title="⚛️ QUANTUM PLAYGROUND",
    subtitle="Step into the weirdest corner of the universe!!!",
)

# ── Intro ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cosmic-card" style="text-align:center; padding:1.2rem 1.4rem;">
  <span style="font-size:1.08rem; color:#d4c5f9;">
    Quantum computing sounds like magic. It is not. But it is genuinely strange,
    and once you see it for yourself, you will never look at the universe the same way again.<br><br>
    Everything here is built with <b style="color:#ffe066;">real quantum circuits</b> in Qiskit,
    the same open-source toolkit researchers use, and simulated exactly with Qiskit's
    statevector tools. No equations required. Just click, explore, and let yourself be amazed.
  </span>
</div>
""", unsafe_allow_html=True)

# ── Module cards ───────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">📡 Pick a place to start</div>', unsafe_allow_html=True)

# Module 1
st.markdown("""
<div class="cosmic-card" style="border-left: 4px solid #f59e0b;">
  <div style="font-family:'Orbitron',sans-serif; font-size:1.15rem; color:#f59e0b; margin-bottom:0.5em; letter-spacing:0.08em;">
    🪙 MODULE 1: SUPERPOSITION
  </div>
  <div style="color:#d4c5f9; font-size:1rem; margin-bottom:0.2em;">
    A regular coin is heads or tails. A quantum coin is <b style="color:#ffe066;">both at once</b> until you look.
    Meet the quantum coin and the Hadamard gate.
  </div>
</div>
""", unsafe_allow_html=True)
st.page_link("pages/1_Superposition.py", label="⚡ Start Module 1 →")

st.write("")

# Module 2
st.markdown("""
<div class="cosmic-card" style="border-left: 4px solid #7c3aed;">
  <div style="font-family:'Orbitron',sans-serif; font-size:1.15rem; color:#a78bfa; margin-bottom:0.5em; letter-spacing:0.08em;">
    🎲 MODULE 2: TWO QUBITS
  </div>
  <div style="color:#d4c5f9; font-size:1rem; margin-bottom:0.2em;">
    One quantum coin gives you 2 possibilities. Two give you 4, all at the same time.
    Watch the magic multiply.
  </div>
</div>
""", unsafe_allow_html=True)
st.page_link("pages/2_Two_Qubits.py", label="⚡ Start Module 2 →")

st.write("")

# Module 3
st.markdown("""
<div class="cosmic-card" style="border-left: 4px solid #3a86ff;">
  <div style="font-family:'Orbitron',sans-serif; font-size:1.15rem; color:#60a5fa; margin-bottom:0.5em; letter-spacing:0.08em;">
    🔗 MODULE 3: ENTANGLEMENT
  </div>
  <div style="color:#d4c5f9; font-size:1rem; margin-bottom:0.2em;">
    Two quantum coins can become linked so that measuring one instantly tells you the other.
    Einstein called it <b style="color:#ffe066;">spooky</b>.
  </div>
</div>
""", unsafe_allow_html=True)
st.page_link("pages/3_Entanglement.py", label="⚡ Start Module 3 →")

st.write("")

# Module 4
st.markdown("""
<div class="cosmic-card" style="border-left: 4px solid #ffe066;">
  <div style="font-family:'Orbitron',sans-serif; font-size:1.15rem; color:#ffe066; margin-bottom:0.5em; letter-spacing:0.08em;">
    🎛️ MODULE 4: GATES LAB
  </div>
  <div style="color:#d4c5f9; font-size:1rem; margin-bottom:0.2em;">
    Take the controls! Stack real quantum gates, spin the 3D Bloch sphere,
    and beat the <b style="color:#ffe066;">lab challenges</b>. Your circuit, your rules.
  </div>
</div>
""", unsafe_allow_html=True)
st.page_link("pages/4_Gates_Lab.py", label="⚡ Enter the Gates Lab →")

# ── Footer ─────────────────────────────────────────────────────────────────────
st.write("")
st.markdown("""
<div style="text-align:center; color:#6b7280; font-size:0.85rem; margin-top:1rem; letter-spacing:0.05em;">
  Built by <b style="color:#a78bfa;">Ouarda Wilson</b>, IBM Qiskit Advocate ·
  Powered by Qiskit + Streamlit
</div>
""", unsafe_allow_html=True)
