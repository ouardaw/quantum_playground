"""
quantum_style.py — Shared cosmic styling for Quantum Playground.
Matches the Stellaris app: dark space background, Orbitron font,
glowing cosmic-card, 3-D sidebar nav buttons (amber/orange) and
3-D page-body buttons (purple/blue).
"""

import streamlit as st
import matplotlib.pyplot as plt


# ── colour palette ─────────────────────────────────────────────────────────────
BG_DEEP   = "#0f0f23"
BG_MID    = "#16213e"
BG_LIGHT  = "#1a1a2e"
PURPLE    = "#7c3aed"
PURPLE2   = "#8b5cf6"
GOLD      = "#f59e0b"
GOLD2     = "#ffe066"
BLUE      = "#3a86ff"
TEXT      = "#f8fafc"
MUTED     = "#a78bfa"

CHART_COLORS = [PURPLE, PURPLE2, BLUE, "#60a5fa"]


# ── CSS injection ──────────────────────────────────────────────────────────────
def inject_quantum_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600&family=Orbitron:wght@700&display=swap');

    /* ── Global base ──────────────────────────────────────────────── */
    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #f8fafc !important;
    }
    .stApp {
        background: radial-gradient(ellipse at 60% 40%, #1a1a2e 0%, #16213e 40%, #0f0f23 100%) !important;
    }
    .block-container { padding-top: 12px; }
    footer, #MainMenu { visibility: hidden; }
    div[data-testid="stStatusWidget"] { display: none !important; }
    a[data-testid="stDecoration"] { display: none !important; }

    /* ── Hide the auto-generated Streamlit page nav ─────────────── */
    [data-testid="stSidebarNav"] { display: none !important; }

    /* ── Sidebar background ─────────────────────────────────────── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(160deg, #1a1a2e 0%, #16213e 60%, #0f0f23 100%) !important;
        border-right: 1px solid rgba(124,58,237,0.30) !important;
    }

    /* ── Sidebar navigation buttons — amber/orange 3-D (Stellaris style) */
    section[data-testid="stSidebar"] button {
        background: linear-gradient(135deg, #f59e0b 0%, #fb923c 50%, #ea580c 100%) !important;
        color: #fff !important;
        font-family: 'Orbitron', sans-serif !important;
        border: none !important;
        border-radius: 0px !important;
        font-size: 1rem !important;
        margin-bottom: 0.65em !important;
        font-weight: 700 !important;
        letter-spacing: 0.08em !important;
        padding: 1em 0.5em !important;
        box-shadow:
            0 7px 0 #dc2626,
            0 7px 1px #b91c1c,
            0 10px 12px rgba(0,0,0,0.40),
            0 0 18px rgba(251,146,60,0.30) !important;
        transform: translateY(0) !important;
        transition: all 0.15s ease !important;
        text-transform: uppercase !important;
        position: relative !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        width: 100% !important;
    }
    section[data-testid="stSidebar"] button:hover {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 50%, #fb923c 100%) !important;
        transform: translateY(3px) !important;
        box-shadow:
            0 4px 0 #dc2626,
            0 4px 1px #b91c1c,
            0 7px 10px rgba(0,0,0,0.40),
            0 0 26px rgba(251,146,60,0.55) !important;
    }
    section[data-testid="stSidebar"] button:active {
        background: linear-gradient(135deg, #ea580c 0%, #dc2626 50%, #b91c1c 100%) !important;
        transform: translateY(6px) !important;
        box-shadow:
            0 1px 0 #991b1b,
            0 2px 4px rgba(0,0,0,0.40),
            inset 0 2px 5px rgba(0,0,0,0.20) !important;
    }
    /* Shine on sidebar buttons */
    section[data-testid="stSidebar"] button::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 46%;
        background: linear-gradient(to bottom, rgba(255,255,255,0.28), rgba(255,255,255,0.05));
        border-radius: 0;
        pointer-events: none;
    }

    /* ── Page-body buttons — purple/blue 3-D ───────────────────── */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed 0%, #3a86ff 100%) !important;
        color: #fff !important;
        font-family: 'Orbitron', sans-serif !important;
        border: none !important;
        border-radius: 0px !important;
        font-weight: 700 !important;
        letter-spacing: 0.07em !important;
        padding: 0.75em 1.5em !important;
        box-shadow:
            0 6px 0 #5b21b6,
            0 8px 12px rgba(0,0,0,0.45),
            0 0 18px rgba(124,58,237,0.30) !important;
        transform: translateY(0) !important;
        transition: all 0.15s ease !important;
        text-transform: uppercase !important;
        position: relative !important;
        overflow: hidden !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #8b5cf6 0%, #60a5fa 100%) !important;
        transform: translateY(2px) !important;
        box-shadow:
            0 4px 0 #5b21b6,
            0 6px 10px rgba(0,0,0,0.45),
            0 0 26px rgba(124,58,237,0.50) !important;
    }
    .stButton > button:active {
        transform: translateY(5px) !important;
        box-shadow: 0 1px 0 #4c1d95, 0 2px 4px rgba(0,0,0,0.40) !important;
    }
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 45%;
        background: linear-gradient(to bottom, rgba(255,255,255,0.22), rgba(255,255,255,0.05));
        pointer-events: none;
    }

    /* ── Hero banner ──────────────────────────────────────────────── */
    #quantum-hero {
        background: linear-gradient(135deg,
            rgba(124,58,237,0.25) 0%,
            rgba(15,15,35,0.85) 50%,
            rgba(58,134,255,0.18) 100%);
        border: 1.5px solid rgba(255,255,255,0.12);
        border-radius: 28px;
        padding: 2rem 1.5rem 1.6rem 1.5rem;
        margin: 0.4rem auto 1.4rem auto;
        text-align: center;
        box-shadow:
            0 8px 32px rgba(124,58,237,0.4),
            0 2px 18px rgba(255,224,102,0.25),
            inset 0 1px 0 rgba(255,255,255,0.12);
        position: relative;
        overflow: hidden;
        animation: heroFloat 6s ease-in-out infinite;
    }
    @keyframes heroFloat {
        0%,100% { transform: perspective(1000px) rotateX(1.5deg) translateY(0); }
        50%      { transform: perspective(1000px) rotateX(1.5deg) translateY(-5px); }
    }

    /* ── Typography ───────────────────────────────────────────────── */
    .cosmic-title {
        font-family: 'Orbitron', sans-serif !important;
        font-size: clamp(1.8rem, 4.5vw, 2.7rem);
        letter-spacing: 0.16em;
        text-align: center;
        background: linear-gradient(90deg, #ffe066 0%, #7c3aed 55%, #3a86ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.3em;
        filter: drop-shadow(0 0 6px rgba(245,158,11,0.3));
    }
    .cosmic-subtitle {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(0.85rem, 2vw, 1.05rem);
        letter-spacing: 0.25em;
        text-transform: uppercase;
        color: #a78bfa;
        margin-top: 0.2em;
    }
    .cosmic-section {
        font-family: 'Orbitron', sans-serif !important;
        font-size: 1.35rem;
        letter-spacing: 0.1em;
        margin: 1.8rem 0 0.9rem 0;
        background: linear-gradient(90deg, #f59e0b 0%, #7c3aed 80%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* ── Cards ────────────────────────────────────────────────────── */
    .cosmic-card {
        background: linear-gradient(120deg, rgba(131,56,236,0.20), rgba(59,134,255,0.13));
        border: 2px solid rgba(255,255,255,0.10);
        border-radius: 28px;
        box-shadow:
            0 8px 32px rgba(124,58,237,0.35),
            0 2px 18px rgba(255,224,102,0.18),
            inset 0 3px 18px rgba(255,255,255,0.04),
            inset 0 -8px 32px rgba(124,58,237,0.10);
        padding: 1.4rem 1.3rem;
        margin-bottom: 1.2rem;
        transition: box-shadow 0.25s;
    }
    .cosmic-card:hover {
        box-shadow:
            0 12px 48px rgba(124,58,237,0.55),
            0 2px 32px rgba(255,224,102,0.30),
            inset 0 6px 26px rgba(255,255,255,0.07),
            inset 0 -12px 44px rgba(124,58,237,0.18);
    }

    /* ── Callout ──────────────────────────────────────────────────── */
    .callout-quantum {
        background: linear-gradient(120deg, rgba(124,58,237,0.15), rgba(58,134,255,0.09));
        border-left: 4px solid #7c3aed;
        border-radius: 0 20px 20px 0;
        padding: 1rem 1.25rem;
        margin: 1rem 0 1.2rem 0;
        box-shadow: 0 2px 16px rgba(124,58,237,0.18);
        font-size: 1.02rem;
        color: #f8fafc;
    }

    /* ── Result display ───────────────────────────────────────────── */
    .result-display {
        font-size: clamp(3rem, 8vw, 5rem);
        text-align: center;
        margin: 1rem 0;
        animation: resultGlow 2s ease-in-out infinite;
    }
    @keyframes resultGlow {
        0%,100% { filter: drop-shadow(0 0 16px rgba(124,58,237,0.5)); }
        50%      { filter: drop-shadow(0 0 32px rgba(245,158,11,0.8)); }
    }

    /* ── Page links ───────────────────────────────────────────────── */
    a[data-testid="stPageLink-NavLink"] {
        background: linear-gradient(90deg, rgba(124,58,237,0.25), rgba(58,134,255,0.18)) !important;
        border: 1px solid rgba(124,58,237,0.40) !important;
        border-radius: 14px !important;
        padding: 0.6em 1.2em !important;
        color: #a78bfa !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        transition: all 0.2s !important;
        display: inline-block !important;
        margin-top: 0.4em !important;
    }
    a[data-testid="stPageLink-NavLink"]:hover {
        background: linear-gradient(90deg, rgba(139,92,246,0.45), rgba(96,165,250,0.30)) !important;
        color: #ffe066 !important;
        box-shadow: 0 0 18px rgba(124,58,237,0.50) !important;
    }

    /* ── Expander ─────────────────────────────────────────────────── */
    details {
        background: rgba(124,58,237,0.07) !important;
        border: 1px solid rgba(124,58,237,0.28) !important;
        border-radius: 16px !important;
        padding: 0.3em 0.6em !important;
        margin-bottom: 0.8em !important;
    }
    summary { color: #a78bfa !important; font-family: 'Space Grotesk', sans-serif !important; font-weight: 600 !important; }

    /* ── Code blocks ──────────────────────────────────────────────── */
    .stCodeBlock, pre {
        border: 1px solid rgba(124,58,237,0.35) !important;
        border-radius: 14px !important;
        background: rgba(15,15,35,0.85) !important;
    }

    /* ── Orb blobs for hero ───────────────────────────────────────── */
    .orb { position:absolute; border-radius:50%; filter:blur(38px); opacity:0.55; pointer-events:none; }
    .orb1 { width:80px; height:80px; background:radial-gradient(circle,#ffb800,transparent); top:10%; left:8%; animation:orbFloat1 15s ease-in-out infinite; }
    .orb2 { width:60px; height:60px; background:radial-gradient(circle,#7c3aed,transparent); top:55%; right:8%; animation:orbFloat2 20s ease-in-out infinite; }
    .orb3 { width:90px; height:90px; background:radial-gradient(circle,#3a86ff,transparent); bottom:8%; left:48%; animation:orbFloat3 25s ease-in-out infinite; }
    @keyframes orbFloat1 { 0%,100%{transform:translate(0,0) scale(1)} 33%{transform:translate(28px,-28px) scale(1.1)} 66%{transform:translate(-18px,18px) scale(0.9)} }
    @keyframes orbFloat2 { 0%,100%{transform:translate(0,0) scale(1)} 50%{transform:translate(-36px,36px) scale(1.2)} }
    @keyframes orbFloat3 { 0%,100%{transform:translate(0,0) scale(1)} 25%{transform:translate(18px,-18px) scale(0.85)} 50%{transform:translate(-28px,-8px) scale(1.1)} 75%{transform:translate(8px,28px) scale(0.9)} }
    </style>
    """, unsafe_allow_html=True)


# ── Sidebar renderer ───────────────────────────────────────────────────────────
def render_sidebar(active: str = "home"):
    """
    Render the Stellaris-style sidebar nav with amber/orange 3-D buttons.
    active: one of 'home', 'superposition', 'two_qubits', 'entanglement'
    """
    with st.sidebar:
        # ── Info card (mirrors "Stargazer!" in Stellaris) ─────────
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(124,58,237,0.35), rgba(245,158,11,0.25));
            border: 1.5px solid rgba(255,255,255,0.14);
            border-radius: 18px;
            padding: 1rem 0.9rem 0.85rem 0.9rem;
            margin-bottom: 1.1em;
            box-shadow: 0 4px 24px rgba(124,58,237,0.30), 0 0 12px rgba(245,158,11,0.15);
            text-align: center;
        ">
          <div style="font-size:2rem; margin-bottom:0.15em;">⚛️</div>
          <div style="font-family:'Orbitron',sans-serif; font-size:1.05rem;
                      font-weight:700; letter-spacing:0.12em; color:#f59e0b;
                      margin-bottom:0.4em;">QUANTUM EXPLORER</div>
          <div style="font-size:0.82rem; color:#d4c5f9; line-height:1.45;">
            Explore superposition, entanglement &amp; real Qiskit circuits.
            Choose a module to begin your quantum journey! 🚀
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            "<div style='border-top:1px solid rgba(124,58,237,0.30); margin:0.4em 0 0.9em 0;'></div>",
            unsafe_allow_html=True,
        )

        # ── Navigation buttons ────────────────────────────────────
        pages = [
            ("🌌", "HOME",          "home",          "Home.py"),
            ("🪙", "SUPERPOSITION", "superposition", "pages/1_Superposition.py"),
            ("🎲", "TWO QUBITS",    "two_qubits",    "pages/2_Two_Qubits.py"),
            ("🔗", "ENTANGLEMENT",  "entanglement",  "pages/3_Entanglement.py"),
        ]

        for icon, label, key, path in pages:
            # Highlight active page with slightly brighter button
            btn_label = f"{icon}  {label}"
            if st.button(btn_label, key=f"nav_{key}", use_container_width=True):
                st.switch_page(path)


# ── Hero banner ────────────────────────────────────────────────────────────────
def render_hero(title: str, subtitle: str):
    st.markdown(f"""
    <div id="quantum-hero">
      <div class="orb orb1"></div>
      <div class="orb orb2"></div>
      <div class="orb orb3"></div>
      <div style="position:relative;z-index:2">
        <div class="cosmic-title">{title}</div>
        <div class="cosmic-subtitle">{subtitle}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── Helpers ────────────────────────────────────────────────────────────────────
def cosmic_card(html_body: str):
    st.markdown(f'<div class="cosmic-card">{html_body}</div>', unsafe_allow_html=True)


def callout(html_body: str):
    st.markdown(f'<div class="callout-quantum">{html_body}</div>', unsafe_allow_html=True)


# ── Dark-themed Matplotlib bar chart ──────────────────────────────────────────
def dark_bar_chart(probs: dict, title: str, figsize=(5.5, 3.2)):
    labels = list(probs.keys())
    values = [probs[k] * 100 for k in labels]
    colors = CHART_COLORS[: len(labels)]

    fig, ax = plt.subplots(figsize=figsize, facecolor=BG_MID)
    ax.set_facecolor(BG_DEEP)

    bars = ax.bar(labels, values, color=colors, edgecolor=MUTED, linewidth=0.6, width=0.55)
    ax.set_ylim(0, 115)
    ax.set_ylabel("Chance (%)", color=MUTED, fontsize=10)
    ax.set_title(title, color=GOLD, fontsize=11, fontweight="bold", pad=10)
    ax.tick_params(colors="#d4c5f9", labelsize=9)

    for spine in ax.spines.values():
        spine.set_edgecolor(f"{PURPLE}55")

    for bar, v in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            v + 4,
            f"{v:.0f}%",
            ha="center",
            fontweight="bold",
            fontsize=9,
            color=GOLD2,
        )

    fig.tight_layout()
    return fig
