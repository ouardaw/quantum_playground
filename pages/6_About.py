"""
Quantum Playground - About
Why the app exists, what it teaches, how it works, and who made it.
"""

import streamlit as st
from quantum_style import (
    inject_quantum_css, render_sidebar, render_footer, callout, render_hero_img,
)

st.set_page_config(page_title="About | Quantum Playground", page_icon="❓",
                   layout="centered", initial_sidebar_state="auto")
inject_quantum_css()
render_sidebar("about")

# ── Header ─────────────────────────────────────────────────────────────────────
render_hero_img("assets/hero_about.jpg",
                "About: why Quantum Playground exists.")

# ── Why ────────────────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">Why this exists</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="border-left: 4px solid #f59e0b; border-radius:22px;
            color:#d4c5f9; font-size:0.98rem; line-height:1.6;">
A few months ago I stumbled into quantum computing through free videos online.
I fully expected it to go over my head. Instead, I got completely hooked.<br><br>
What surprised me was how much of it made sense once someone
<b style="color:#ffe066;">showed</b> me an idea instead of just telling me about it.
When it finally clicked, it felt like magic I was allowed to understand.<br><br>
Quantum Playground is my attempt to pass that feeling along. It is not a replacement
for the wonderful courses and videos already out there. It is a first door: somewhere
to click, experiment, and get curious enough to go find them.
</div>
""", unsafe_allow_html=True)

# ── How it works ───────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">How it works</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="border-left: 4px solid #7c3aed; border-radius:22px;
            color:#d4c5f9; font-size:0.98rem; line-height:1.6;">
Nothing here is a pre-recorded animation. Every button you press builds a genuine
quantum circuit with <b style="color:#ffe066;">Qiskit</b>, the open-source toolkit
researchers and IBM engineers use every day.<br><br>
The probabilities in the charts come straight from the quantum statevector. The arrow
on the Bloch sphere is computed from that same state. When you measure, the result is
sampled from the real distribution, which is why it is different every time.<br><br>
The circuits are simulated exactly, so the numbers you see are the ideal, noise-free
answer. Running the same circuit on real hardware would give you nearly the same result,
plus a little noise, which is one of the biggest open challenges in the field.
</div>
""", unsafe_allow_html=True)

# ── Who it is for ──────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">Who it is for</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="border-left: 4px solid #3a86ff; border-radius:22px;
            color:#d4c5f9; font-size:0.95rem; line-height:1.7;">
<b style="color:#ffe066;">Curious beginners</b> of any age who have wondered what a qubit is.<br>
<b style="color:#ffe066;">Middle and high school students</b> meeting quantum ideas for the first time.<br>
<b style="color:#ffe066;">Teachers and STEM club leaders</b> who need a ready-made, install-free activity.
Each mission is a self-contained 10 to 15 minute lesson that works on a projector or on
students' own devices.<br>
<b style="color:#ffe066;">Parents</b> looking for something genuinely educational that still feels like play.<br><br>
No account, no downloads, no cost. It runs in any browser, including phones.
</div>
""", unsafe_allow_html=True)

# ── Built with ─────────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">Built with</div>', unsafe_allow_html=True)

TOOLS = [
    ("Qiskit", "Quantum circuits, statevectors and measurement sampling"),
    ("Streamlit", "The interactive web interface"),
    ("Plotly and Matplotlib", "The 3D Bloch sphere and probability charts"),
    ("Python", "Holding it all together"),
]
tcols = st.columns(2)
for i, (name, role) in enumerate(TOOLS):
    with tcols[i % 2]:
        st.markdown(f"""
        <div class="cosmic-card" style="padding:0.8rem 1rem; margin-bottom:0.6rem;
                    border-radius:18px;">
          <div style="font-family:'Orbitron',sans-serif; font-size:0.85rem; color:#a78bfa;
                      letter-spacing:0.04em; margin-bottom:0.3em;">{name}</div>
          <div style="color:#d4c5f9; font-size:0.85rem;">{role}</div>
        </div>
        """, unsafe_allow_html=True)

# ── Creator ────────────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">About the creator</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cosmic-card" style="border-left: 4px solid #ffe066; border-radius:22px;
            color:#d4c5f9; font-size:0.98rem; line-height:1.6;">
Hi, I'm <b style="color:#ffe066;">Ouarda Wilson</b>. I've worked in technology for more
than 17 years and have always enjoyed learning about new tools, ideas, and emerging
technologies.<br><br>
I recently became an IBM Qiskit Advocate, and I'm still learning more about quantum
computing every day. Quantum Playground is one way for me to practice what I'm learning,
contribute to the community, and help make some of these concepts easier to explore.<br><br>
I hope to keep improving the project and adding new missions over time. If you use it with
students, try it yourself, or notice something that could be better, I would genuinely love
to hear from you.
</div>
""", unsafe_allow_html=True)

callout(
    "<b style='color:#ffe066;'>A note on accuracy:</b> the physics in this app has been "
    "checked carefully, and the simplifications are the standard ones used by quantum "
    "educators. Where an analogy breaks down, the app says so rather than letting the "
    "wrong idea stick. If you find a genuine mistake, please tell me."
)

st.page_link("Home.py", label="🚀 Return to Mission Control")
render_footer()
