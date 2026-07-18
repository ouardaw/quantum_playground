"""
Quantum Playground - Home
An interactive web app to teach quantum computing concepts.
Built by Ouarda Wilson, IBM Qiskit Advocate.
"""

import streamlit as st
from quantum_style import (
    inject_quantum_css, render_hero, cosmic_card, callout,
    render_sidebar, MODULES, AMBER_SOLID,
)

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
<div class="cosmic-card" style="border-left: 4px solid #f59e0b; border-radius: 22px;
            padding: 1rem 1.25rem; color:#d4c5f9; font-size:0.98rem; line-height:1.55;">
  Quantum computing sounds like magic. It is not. But it is genuinely strange, and once
  you see it for yourself, you will never look at the universe the same way again.
  Everything here is built with <b style="color:#ffe066;">real quantum circuits</b> in Qiskit,
  the same open-source toolkit researchers use. No equations required.
  Just click, explore, and let yourself be amazed.
</div>
""", unsafe_allow_html=True)

# ── Mission map ────────────────────────────────────────────────────────────────
st.markdown('<div class="cosmic-section">🗺️ Your mission map</div>', unsafe_allow_html=True)

completed = st.session_state.setdefault("completed", set())
target = next((k for k, *_ in MODULES if k not in completed), None)

blurbs = {
    "superposition": "A coin that is <b style='color:#ffe066;'>both at once</b> until you look. Meet the Hadamard gate.",
    "two_qubits":    "One coin gives 2 possibilities. Two give <b style='color:#ffe066;'>4 at the same time</b>.",
    "entanglement":  "Two linked coins that can <b style='color:#ffe066;'>never disagree</b>. Einstein called it spooky.",
    "gates_lab":     "Stack real gates, spin the 3D sphere, beat the <b style='color:#ffe066;'>lab challenges</b>.",
}

# Per-status styling for the map buttons (hover states pin dark backgrounds
# so labels stay readable over the global button hover)
map_rules = []
for key, *_ in MODULES:
    sel = f".st-key-map_{key} button"
    if key == target:
        map_rules.append(f"""
        {sel} {{ {AMBER_SOLID} }}
        {sel}:hover {{
            background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 55%, #fb923c 100%) !important;
            color: #fff !important;
        }}""")
    elif key in completed:
        map_rules.append(f"""
        {sel} {{
            background: rgba(29,158,117,0.14) !important;
            color: #7ee2b0 !important;
            border: 1px solid rgba(126,226,176,0.45) !important;
            box-shadow: none !important;
        }}
        {sel}:hover {{
            background: rgba(29,158,117,0.28) !important;
            color: #7ee2b0 !important;
            border-color: rgba(126,226,176,0.9) !important;
            box-shadow: none !important;
        }}""")
    else:
        map_rules.append(f"""
        {sel} {{
            background: rgba(34,42,82,0.55) !important;
            color: #a78bfa !important;
            border: 1px solid rgba(124,58,237,0.35) !important;
            box-shadow: none !important;
        }}
        {sel}:hover {{
            background: rgba(34,42,82,0.9) !important;
            color: #ffe066 !important;
            border-color: rgba(245,158,11,0.7) !important;
            box-shadow: none !important;
        }}""")
st.markdown(f"<style>{''.join(map_rules)}</style>", unsafe_allow_html=True)

# 2x2 map grid, old-style cards with a left accent border
accents = {
    "superposition": ("#f59e0b", "#f59e0b"),
    "two_qubits":    ("#7c3aed", "#a78bfa"),
    "entanglement":  ("#3a86ff", "#60a5fa"),
    "gates_lab":     ("#ffe066", "#ffe066"),
}
idx = {k: n for n, (k, *_rest) in enumerate(MODULES, 1)}
for row in (MODULES[:2], MODULES[2:]):
    cols = st.columns(2)
    for col, (key, icon, label, sub, path) in zip(cols, row):
        i = idx[key]
        accent, title_color = accents[key]
        if key in completed:
            badge = '<span style="color:#7ee2b0;">✓ done</span>'
        elif key == target:
            badge = '<span style="color:#f59e0b;">▶ up now</span>'
        else:
            badge = '<span style="color:#6b7280;">up next</span>'
        with col:
            st.markdown(f"""
            <div class="cosmic-card" style="border-left: 4px solid {accent}; border-radius: 22px;
                        padding: 0.9rem 1.05rem; margin-bottom: 0.55rem; min-height: 128px;">
              <div style="display:flex; justify-content:space-between; align-items:baseline; gap:0.4em;">
                <span style="font-family:'Orbitron',sans-serif; font-size:0.92rem; color:{title_color};
                             letter-spacing:0.05em;">{icon} {i}. {label}</span>
                <span style="font-size:0.76rem; white-space:nowrap;">{badge}</span>
              </div>
              <div style="color:#d4c5f9; font-size:0.87rem; margin-top:0.5em; line-height:1.45;">{blurbs[key]}</div>
            </div>
            """, unsafe_allow_html=True)
            btn_label = "↺ REPLAY" if key in completed else ("▶ CONTINUE" if key == target else "OPEN")
            if st.button(btn_label, key=f"map_{key}", use_container_width=True):
                st.switch_page(path)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.write("")
st.markdown("""
<div style="text-align:center; color:#6b7280; font-size:0.85rem; margin-top:1rem; letter-spacing:0.05em;">
  Built by <b style="color:#a78bfa;">Ouarda Wilson</b>, IBM Qiskit Advocate ·
  Powered by Qiskit + Streamlit
</div>
""", unsafe_allow_html=True)
