"""
Quantum Playground - Home
An interactive web app to teach quantum computing concepts.
Built by Ouarda Wilson, IBM Qiskit Advocate.
"""

import streamlit as st
from quantum_style import (
    inject_quantum_css, render_hero, cosmic_card, callout,
    render_sidebar, MODULES, AMBER_SOLID, img_b64, render_footer,
)

st.set_page_config(
    page_title="Quantum Playground",
    page_icon="⚛️",
    layout="centered",
    initial_sidebar_state="auto",
)

inject_quantum_css()
render_sidebar("home")

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown(
    f'<img src="{img_b64("assets/hero_home.jpg")}" '
    f'style="width:100%; border-radius:22px; margin-bottom:0.6rem; '
    f'box-shadow: 0 8px 32px rgba(124,58,237,0.45), 0 2px 18px rgba(255,224,102,0.20);" '
    f'alt="Quantum Playground: explore, experiment, understand. Learn the basics of '
    f'quantum computing through interactive simulations and fun experiments." />',
    unsafe_allow_html=True,
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
st.markdown('<div class="cosmic-section">Your mission map</div>', unsafe_allow_html=True)

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
            badge = '<span style="color:#9ca3af;">up next</span>'
        with col:
            art = img_b64(f"assets/card_{key}.jpg")
            st.markdown(f"""
            <div class="cosmic-card" style="border-left: 4px solid {accent}; border-radius: 22px;
                        padding: 0.9rem 1.05rem; margin-bottom: 0.55rem;">
              <img src="{art}" style="width:100%; aspect-ratio: 15/8; object-fit: cover; border-radius:14px; margin-bottom:0.6em;" alt="" />
              <div style="display:flex; justify-content:space-between; align-items:baseline; gap:0.4em;">
                <span style="font-family:'Orbitron',sans-serif; font-size:0.92rem; color:{title_color};
                             letter-spacing:0.05em;">{i}. {label}</span>
                <span style="font-size:0.82rem; white-space:nowrap;">{badge}</span>
              </div>
              <div style="color:#d4c5f9; font-size:0.87rem; margin-top:0.5em; line-height:1.45; min-height:3em;">{blurbs[key]}</div>
            </div>
            """, unsafe_allow_html=True)
            btn_label = "↺ REPLAY" if key in completed else "▶ START MISSION"
            if st.button(btn_label, key=f"map_{key}", use_container_width=True):
                st.switch_page(path)

# ── Footer ─────────────────────────────────────────────────────────────────────
render_footer()
