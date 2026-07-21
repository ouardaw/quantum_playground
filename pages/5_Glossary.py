"""
Quantum Playground - Glossary
A beginner-friendly dictionary of the quantum words used across the app.
Every definition: one plain sentence, then an everyday analogy.
"""

import streamlit as st
from quantum_style import (
    inject_quantum_css, render_sidebar, render_footer, img_b64, render_hero_img,
)

st.set_page_config(page_title="Glossary | Quantum Playground", page_icon="📚",
                   layout="centered", initial_sidebar_state="auto")
inject_quantum_css()
render_sidebar("glossary")

# ── Header ─────────────────────────────────────────────────────────────────────
render_hero_img("assets/hero_glossary.jpg",
                "Glossary: every quantum word, in plain language.")

# ── Terms ──────────────────────────────────────────────────────────────────────
# (term, accent colour, definition, analogy)
BLOCH_ICON = (
    f'<img src="{img_b64("assets/home_icon.jpg")}" alt="" '
    f'style="width:62px; height:62px; border-radius:12px; float:right; '
    f'margin:0 0 0.5em 0.9em;" />'
)

TERMS = [
    ("Qubit", "#f59e0b",
     "The basic unit of a quantum computer, like a bit in a normal computer, "
     "except it can hold a mix of 0 and 1 until you measure it.",
     "A coin that is still deciding what it wants to be.",
     ),

    ("Superposition", "#f59e0b",
     "A qubit holding both |0⟩ and |1⟩ at the same time, each with its own chance "
     "of showing up when measured.",
     "Not a spinning coin you simply cannot see. Genuinely both faces at once, "
     "until the moment you look.",
     ),

    ("Measurement", "#3a86ff",
     "Looking at a qubit. The instant you do, it stops being a mix and becomes "
     "one definite answer: 0 or 1.",
     "Opening your hand to see which way the coin landed. Once you look, "
     "the in-between is gone.",
     ),

    ("Entanglement", "#3a86ff",
     "Two or more qubits linked so that their results are perfectly related, "
     "no matter how far apart they are.",
     "Two coins that always land the same way as each other, even in different cities. "
     "Each one is still random on its own.",
     ),

    ("Quantum gate", "#a78bfa",
     "An operation that changes a qubit's state. Gates are the moves you make "
     "when building a quantum program.",
     "A dance step for the qubit. X spins it around, H splits it in half, "
     "Z quietly changes its timing.",
     ),

    ("Quantum circuit", "#a78bfa",
     "A sequence of gates applied to one or more qubits, ending in a measurement.",
     "A recipe. Each gate is one instruction, followed in order.",
     ),

    ("Bloch sphere", "#7c3aed",
     BLOCH_ICON +
     "A globe used to picture the state of a single qubit. The North pole is |0⟩, "
     "the South pole is |1⟩, and an arrow points to the qubit's current state.",
     "A globe where the arrow's latitude tells you your odds, "
     "and its longitude tells you the phase.",
     ),

    ("Phase", "#7c3aed",
     "The hidden part of a quantum state. Phase does not change your odds on its own, "
     "but it changes how qubits combine later.",
     "Timing in music. One note played early sounds the same alone, "
     "but changes the chord completely.",
     ),

    ("Interference", "#ffe066",
     "When quantum possibilities combine, adding up to make some answers more likely "
     "and cancelling out to make others vanish.",
     "Two waves in a pond meeting. Crest on crest makes a bigger wave, "
     "crest on trough leaves flat water.",
     ),

    ("Rotation (RY)", "#ffe066",
     "A gate that tilts the qubit's arrow by any angle you choose, giving you "
     "lopsided odds instead of a plain 50/50.",
     "A dimmer switch instead of an on/off switch.",
     ),

    ("Hadamard gate (H)", "#f59e0b",
     "The gate that creates superposition. It takes a definite |0⟩ and turns it into "
     "an equal mix of |0⟩ and |1⟩.",
     "The perfect coin flip. Apply it twice and it undoes itself, "
     "which is interference at work.",
     ),

    ("Ket notation (|0⟩)", "#3a86ff",
     "The angle-bracket shorthand physicists use to write quantum states, "
     "invented by Paul Dirac.",
     "|0⟩ just means 'the qubit is 0'. With two qubits, |10⟩ means one came out 1 "
     "and the other 0.",
     ),

    ("Decoherence", "#a78bfa",
     "When a qubit loses its quantum behaviour by interacting with its surroundings. "
     "It is the main reason quantum computers are hard to build.",
     "A spinning top slowly wobbling to a stop because of friction with the table.",
     ),

    ("Qiskit", "#7c3aed",
     "The free, open-source Python toolkit for building and running quantum circuits. "
     "It powers every experiment in this app.",
     "The programming language of quantum computing. Researchers use the same one.",
     ),
]

st.write("")

for term, accent, definition, analogy in TERMS:
    with st.container():
        st.markdown(f"""
        <div class="cosmic-card" style="border-left: 4px solid {accent}; border-radius: 22px;
                    padding: 1rem 1.2rem; margin-bottom: 0.8rem; overflow: hidden;">
          <div style="font-family:'Orbitron',sans-serif; font-size:1rem; color:{accent};
                      letter-spacing:0.05em; margin-bottom:0.45em;">{term}</div>
          <div style="color:#f8fafc; font-size:0.95rem; line-height:1.55;">{definition}</div>
          <div style="color:#a78bfa; font-size:0.88rem; line-height:1.5; margin-top:0.5em;
                      padding-left:0.8em; border-left:2px solid rgba(167,139,250,0.35);">
            <b style="color:#ffe066;">Think of it like:</b> {analogy}
          </div>
        </div>
        """, unsafe_allow_html=True)

# ── Wrap up ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cosmic-card" style="text-align:center; padding:1.1rem 1rem; color:#d4c5f9;">
  Want to see these ideas in action instead of reading about them?
  Every term above shows up in the missions, where you can click and experiment with it.
</div>
""", unsafe_allow_html=True)

st.page_link("Home.py", label="🚀 Return to Mission Control")
render_footer()
