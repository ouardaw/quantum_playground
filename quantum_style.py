"""
quantum_style.py - Shared cosmic styling for Quantum Playground.
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
    html { font-size: 17.5px !important; }
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

    /* ── Sidebar navigation: quiet ghost buttons by default ─────── */
    section[data-testid="stSidebar"] button {
        background: rgba(26,26,46,0.55) !important;
        color: #d4c5f9 !important;
        font-family: 'Orbitron', sans-serif !important;
        border: 1.5px solid rgba(124,58,237,0.50) !important;
        border-radius: 16px !important;
        font-size: 1.02rem !important;
        margin-bottom: 0.55em !important;
        font-weight: 700 !important;
        letter-spacing: 0.07em !important;
        padding: 0.8em 0.5em !important;
        box-shadow: none !important;
        transform: translateY(0) !important;
        transition: all 0.18s ease !important;
        text-transform: uppercase !important;
        position: relative !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        width: 100% !important;
    }
    section[data-testid="stSidebar"] button:hover {
        border-color: rgba(245,158,11,0.75) !important;
        color: #ffe066 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 0 14px rgba(245,158,11,0.25) !important;
    }
    section[data-testid="stSidebar"] button:active {
        transform: translateY(1px) !important;
    }

    /* ── Page-body buttons, purple/blue 3-D ───────────────────── */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed 0%, #3a86ff 100%) !important;
        color: #fff !important;
        font-family: 'Orbitron', sans-serif !important;
        border: none !important;
        border-radius: 14px !important;
        font-size: 1.02rem !important;
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
        border-radius: 14px 14px 0 0;
        pointer-events: none;
    }

    /* ── Hero banner ──────────────────────────────────────────────── */
    #quantum-hero {
        background: linear-gradient(135deg,
            rgba(124,58,237,0.25) 0%,
            rgba(15,15,35,0.85) 50%,
            rgba(58,134,255,0.18) 100%);
        border: 1.5px solid rgba(255,255,255,0.12);
        border-radius: 22px;
        padding: 1.2rem 1.2rem 1rem 1.2rem;
        margin: 0.3rem auto 1.1rem auto;
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
        font-size: clamp(1.4rem, 3.4vw, 2rem);
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
        font-size: clamp(0.72rem, 1.6vw, 0.9rem);
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
    /* Force link label color regardless of the viewer's browser theme */
    a[data-testid="stPageLink-NavLink"] p,
    a[data-testid="stPageLink-NavLink"] span {
        color: #d4c5f9 !important;
    }
    a[data-testid="stPageLink-NavLink"]:hover p,
    a[data-testid="stPageLink-NavLink"]:hover span {
        color: #ffe066 !important;
    }

    /* ── Expander, prominent glowing panel ───────────────────────── */
    div[data-testid="stExpander"] {
        margin-bottom: 1em !important;
    }
    div[data-testid="stExpander"] details {
        background: linear-gradient(120deg, rgba(245,158,11,0.12), rgba(124,58,237,0.18)) !important;
        border: 2px solid rgba(245,158,11,0.45) !important;
        border-radius: 18px !important;
        padding: 0.35em 0.7em !important;
        box-shadow:
            0 4px 20px rgba(124,58,237,0.30),
            0 0 14px rgba(245,158,11,0.20),
            inset 0 1px 0 rgba(255,255,255,0.08) !important;
        transition: all 0.25s ease !important;
    }
    div[data-testid="stExpander"] details:hover {
        border-color: rgba(255,224,102,0.75) !important;
        box-shadow:
            0 6px 28px rgba(124,58,237,0.45),
            0 0 24px rgba(245,158,11,0.40),
            inset 0 1px 0 rgba(255,255,255,0.12) !important;
        transform: translateY(-2px);
    }
    div[data-testid="stExpander"] summary {
        color: #ffe066 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.02rem !important;
        letter-spacing: 0.05em !important;
        padding: 0.55em 0.3em !important;
    }
    div[data-testid="stExpander"] summary:hover {
        color: #fbbf24 !important;
    }
    div[data-testid="stExpander"] summary p {
        font-family: 'Orbitron', sans-serif !important;
        font-size: 1.02rem !important;
        color: #ffe066 !important;
    }
    div[data-testid="stExpander"] summary svg {
        fill: #f59e0b !important;
        width: 1.4em !important;
        height: 1.4em !important;
    }
    /* fallback for plain details/summary */
    details {
        background: linear-gradient(120deg, rgba(245,158,11,0.12), rgba(124,58,237,0.18)) !important;
        border: 2px solid rgba(245,158,11,0.45) !important;
        border-radius: 18px !important;
        padding: 0.35em 0.7em !important;
        margin-bottom: 0.9em !important;
        box-shadow: 0 4px 20px rgba(124,58,237,0.30), 0 0 14px rgba(245,158,11,0.20) !important;
    }
    summary { color: #ffe066 !important; font-family: 'Orbitron', sans-serif !important; font-weight: 700 !important; }

    /* ── Code blocks ──────────────────────────────────────────────── */
    .stCodeBlock, pre {
        border: 1px solid rgba(124,58,237,0.35) !important;
        border-radius: 14px !important;
        background: rgba(15,15,35,0.85) !important;
    }

    /* ── Quantum coins: silver H / dark purple T ──────────────────── */
    .qcoin {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        vertical-align: middle;
        line-height: 1;
    }
    .qcoin-h {
        background: #d6d9e0;
        border: 3px solid #f0f2f5;
        box-shadow: inset 0 0 0 4px #b8bcc6, 0 0 18px rgba(214,217,224,0.35);
        color: #26215c;
    }
    .qcoin-t {
        background: #26215c;
        border: 3px solid #534ab7;
        box-shadow: inset 0 0 0 4px #3c3489, 0 0 18px rgba(124,58,237,0.45);
        color: #cecbf6;
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


# ── Module registry (single source of truth for nav, stepper, mission map) ────
MODULES = [
    ("superposition", "🪙", "SUPERPOSITION", "The quantum coin",       "pages/1_Superposition.py"),
    ("two_qubits",    "🎲", "TWO QUBITS",    "Possibilities multiply", "pages/2_Two_Qubits.py"),
    ("entanglement",  "🔗", "ENTANGLEMENT",  "Spooky action",          "pages/3_Entanglement.py"),
    ("gates_lab",     "🎛️", "GATES LAB",     "Build your own circuits","pages/4_Gates_Lab.py"),
]
MODULE_KEYS = [m[0] for m in MODULES]

AMBER_SOLID = """
    background: linear-gradient(135deg, #f59e0b 0%, #fb923c 55%, #ea580c 100%) !important;
    color: #fff !important;
    border: none !important;
    box-shadow:
        0 5px 0 #dc2626,
        0 7px 10px rgba(0,0,0,0.40),
        0 0 18px rgba(251,146,60,0.35) !important;
"""


def mark_complete(module_key: str):
    """Mark a module complete; rerun so the sidebar checkmark updates instantly."""
    completed = st.session_state.setdefault("completed", set())
    if module_key not in completed:
        completed.add(module_key)
        st.rerun()


def next_module_button(label: str, path: str, key: str):
    """Big forward-navigation button at the bottom of a module page."""
    if st.button(f"➡️ NEXT: {label}", key=key, use_container_width=True):
        st.switch_page(path)


# ── Sidebar renderer ───────────────────────────────────────────────────────────
def render_sidebar(active: str = "home"):
    """
    Render the Stellaris-style sidebar nav with amber/orange 3-D buttons,
    completion checkmarks, and a mission progress bar.
    """
    completed = st.session_state.setdefault("completed", set())

    with st.sidebar:
        # ── Compact wordmark ──────────────────────────────────────
        st.markdown("""
        <div style="text-align:center; margin: 0.2em 0 0.9em 0;">
          <div style="font-size:1.7rem; margin-bottom:0.1em;">⚛️</div>
          <div style="font-family:'Orbitron',sans-serif; font-size:0.98rem;
                      font-weight:700; letter-spacing:0.16em; line-height:1.5;
                      background: linear-gradient(90deg, #ffe066 0%, #f59e0b 50%, #a78bfa 100%);
                      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                      background-clip: text;">
            QUANTUM<br>PLAYGROUND
          </div>
        </div>
        <div style="border-top:1px solid rgba(124,58,237,0.30); margin:0 0 0.9em 0;"></div>
        """, unsafe_allow_html=True)

        # ── Active page gets the full amber 3-D treatment ─────────
        st.markdown(f"""
        <style>
        section[data-testid="stSidebar"] .st-key-nav_{active} button {{
            {AMBER_SOLID}
        }}
        section[data-testid="stSidebar"] .st-key-nav_{active} button:hover {{
            color: #fff !important;
            transform: translateY(2px) !important;
            box-shadow:
                0 3px 0 #dc2626,
                0 5px 8px rgba(0,0,0,0.40),
                0 0 24px rgba(251,146,60,0.55) !important;
        }}
        </style>
        """, unsafe_allow_html=True)

        # ── Navigation buttons (✅ = module completed) ─────────────
        pages = [("home", "🌌", "HOME", "", "Home.py")] + [
            (key, icon, label, sub, path) for key, icon, label, sub, path in MODULES
        ]
        for key, icon, label, _sub, path in pages:
            check = "  ✅" if key in completed else ""
            if st.button(f"{icon}  {label}{check}", key=f"nav_{key}", use_container_width=True):
                st.switch_page(path)

        # ── Mission progress bar ───────────────────────────────────
        done = len(completed & set(MODULE_KEYS))
        total = len(MODULE_KEYS)
        pct = int(done / total * 100)
        trophy = " 🏆" if done == total else ""
        st.markdown(f"""
        <div style="margin-top:0.9em;">
          <div style="font-family:'Orbitron',sans-serif; font-size:0.8rem;
                      letter-spacing:0.14em; text-align:center; margin-bottom:0.35em;
                      background: linear-gradient(90deg, #ffe066 0%, #f59e0b 50%, #a78bfa 100%);
                      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                      background-clip: text;">
            MISSION PROGRESS: {done}/{total}{trophy}
          </div>
          <div style="background:rgba(124,58,237,0.18); border-radius:10px; height:13px;
                      overflow:hidden; border:1px solid rgba(124,58,237,0.45);
                      box-shadow: inset 0 2px 4px rgba(0,0,0,0.4);">
            <div style="width:{pct}%; height:100%;
                        background:linear-gradient(90deg,#f59e0b,#fb923c,#7c3aed);
                        border-radius:10px; transition:width 0.6s ease;
                        box-shadow: 0 0 10px rgba(245,158,11,0.6);"></div>
          </div>
        </div>
        """, unsafe_allow_html=True)


# ── Mission stepper (top of every module page; mobile-friendly nav) ────────────
def render_stepper(active: str):
    """Horizontal 1-2-3-4 progress chips. Click any chip to jump to that module."""
    completed = st.session_state.setdefault("completed", set())

    rules = []
    for key, _icon, _label, _sub, _path in MODULES:
        sel = f".st-key-step_{key} button"
        if key == active:
            rules.append(f"""
            {sel} {{
                {AMBER_SOLID}
                font-size: 0.76rem !important;
                padding: 0.55em 0.2em !important;
                border-radius: 10px !important;
                letter-spacing: 0.04em !important;
            }}""")
        elif key in completed:
            rules.append(f"""
            {sel} {{
                background: rgba(29,158,117,0.14) !important;
                color: #7ee2b0 !important;
                border: 1px solid rgba(126,226,176,0.45) !important;
                box-shadow: none !important;
                font-size: 0.76rem !important;
                padding: 0.55em 0.2em !important;
                border-radius: 10px !important;
                letter-spacing: 0.04em !important;
            }}
            {sel}:hover {{
                background: rgba(29,158,117,0.25) !important;
                color: #7ee2b0 !important;
                border-color: rgba(126,226,176,0.9) !important;
                box-shadow: none !important;
                transform: translateY(-1px) !important;
            }}""")
        else:
            rules.append(f"""
            {sel} {{
                background: rgba(34,42,82,0.55) !important;
                color: #aab3d8 !important;
                border: 1px solid rgba(124,58,237,0.30) !important;
                box-shadow: none !important;
                font-size: 0.76rem !important;
                padding: 0.55em 0.2em !important;
                border-radius: 10px !important;
                letter-spacing: 0.04em !important;
            }}
            {sel}:hover {{
                background: rgba(34,42,82,0.85) !important;
                color: #ffe066 !important;
                border-color: rgba(245,158,11,0.7) !important;
                box-shadow: none !important;
                transform: translateY(-1px) !important;
            }}""")

    st.markdown(f"<style>{''.join(rules)}</style>", unsafe_allow_html=True)

    cols = st.columns(4)
    for col, (i, (key, _icon, label, _sub, path)) in zip(cols, enumerate(MODULES, 1)):
        prefix = "✓ " if key in completed and key != active else f"{i} · "
        with col:
            if st.button(f"{prefix}{label}", key=f"step_{key}", use_container_width=True):
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


# ── Ket notation explainer (shared by modules that show |0⟩ states) ───────────
def ket_explainer():
    with st.expander("🔤 What do those |00⟩ brackets mean?"):
        st.markdown("""
        <div style="color:#d4c5f9;">
        Those angle brackets are called <b style="color:#ffe066;">ket notation</b>, and they are
        how real physicists write quantum states. The notation was invented by
        <b style="color:#a78bfa;">Paul Dirac</b>, one of the founders of quantum mechanics.<br><br>
        • <b>|0⟩</b> means "the qubit is heads" and <b>|1⟩</b> means "the qubit is tails"<br>
        • With two qubits, each digit is one coin: <b>|10⟩</b> means one came out tails
        and the other heads<br>
        • So <b>|00⟩: 3</b> in your tally means "both heads happened 3 times"<br><br>
        And here is the secret behind the secret: every ket is just
        <b style="color:#f59e0b;">math you can learn</b>. A qubit's state is really a short
        list of numbers called <b>amplitudes</b>, and every gate is a small grid of numbers
        called a <b>matrix</b>. The subject that covers them is called
        <b style="color:#ffe066;">linear algebra</b> (vectors and matrices), and once you know
        the basics, you can calculate everything this app shows you with pen and paper.<br><br>
        Congratulations: you can now read the same notation used in actual research papers.
        This is not a toy version. It is the real thing.
        </div>
        """, unsafe_allow_html=True)


# ── Chart renderer (closes figures to prevent memory leaks on the server) ─────
def show_fig(fig):
    """Render a Matplotlib figure and immediately free its memory.
    Without plt.close, every rerun leaks a figure and the Streamlit Cloud
    container eventually runs out of memory and dies."""
    st.pyplot(fig)
    plt.close(fig)


# ── Quantum coin icon ──────────────────────────────────────────────────────────
def coin_html(side, size: int = 64) -> str:
    """
    Inline HTML for a coin icon. side: 'Heads'/'H'/'0' or 'Tails'/'T'/'1'.
    Silver coin with H for heads, dark purple coin with T for tails.
    """
    is_heads = str(side)[0] in ("H", "h", "0")
    letter, cls = ("H", "qcoin-h") if is_heads else ("T", "qcoin-t")
    return (
        f'<span class="qcoin {cls}" style="width:{size}px;height:{size}px;'
        f'font-size:{int(size * 0.42)}px;">{letter}</span>'
    )


# ── Helpers ────────────────────────────────────────────────────────────────────
def cosmic_card(html_body: str):
    st.markdown(f'<div class="cosmic-card">{html_body}</div>', unsafe_allow_html=True)


def callout(html_body: str):
    st.markdown(f'<div class="callout-quantum">{html_body}</div>', unsafe_allow_html=True)


# ── Interactive 3-D Bloch sphere (Plotly) ─────────────────────────────────────
def bloch_sphere_fig(statevector, title="Your qubit on the Bloch sphere"):
    """
    Build an interactive dark-themed Plotly Bloch sphere for a 1-qubit Statevector.
    The gold arrow is the qubit state; drag to rotate, scroll to zoom.
    """
    import numpy as np
    import plotly.graph_objects as go

    a, b = statevector.data[0], statevector.data[1]
    # Bloch vector: <X>, <Y>, <Z>
    bx = 2 * (np.conj(a) * b).real
    by = 2 * (np.conj(a) * b).imag
    bz = abs(a) ** 2 - abs(b) ** 2

    fig = go.Figure()

    # Translucent sphere surface
    u, v = np.mgrid[0 : 2 * np.pi : 60j, 0 : np.pi : 30j]
    fig.add_surface(
        x=np.cos(u) * np.sin(v),
        y=np.sin(u) * np.sin(v),
        z=np.cos(v),
        opacity=0.16,
        showscale=False,
        colorscale=[[0, PURPLE], [1, BLUE]],
        hoverinfo="skip",
    )

    # Equator ring (superposition zone)
    t = np.linspace(0, 2 * np.pi, 120)
    fig.add_scatter3d(
        x=np.cos(t), y=np.sin(t), z=np.zeros_like(t),
        mode="lines", line=dict(color=GOLD, width=4),
        hoverinfo="skip", showlegend=False,
    )

    # Vertical axis |0> to |1>
    fig.add_scatter3d(
        x=[0, 0], y=[0, 0], z=[-1.15, 1.15],
        mode="lines", line=dict(color="#6b7280", width=2, dash="dash"),
        hoverinfo="skip", showlegend=False,
    )

    # State arrow (shaft + cone tip)
    fig.add_scatter3d(
        x=[0, bx], y=[0, by], z=[0, bz],
        mode="lines", line=dict(color=GOLD2, width=10),
        hoverinfo="skip", showlegend=False,
    )
    fig.add_cone(
        x=[bx], y=[by], z=[bz],
        u=[bx * 0.25], v=[by * 0.25], w=[bz * 0.25],
        sizemode="absolute", sizeref=0.18, anchor="tip",
        colorscale=[[0, GOLD2], [1, GOLD2]], showscale=False,
        hoverinfo="skip",
    )

    # Pole + equator labels
    fig.add_scatter3d(
        x=[0, 0, 1.25], y=[0, 0, 0], z=[1.3, -1.3, 0],
        mode="text",
        text=["|0⟩  Heads", "|1⟩  Tails", "superposition"],
        textfont=dict(size=13, color=[GOLD2, MUTED, GOLD]),
        hoverinfo="skip", showlegend=False,
    )

    axis_off = dict(visible=False, showgrid=False, zeroline=False)
    fig.update_layout(
        title=dict(text=title, font=dict(color=GOLD, size=14), x=0.5),
        paper_bgcolor="rgba(0,0,0,0)",
        scene=dict(
            xaxis=axis_off, yaxis=axis_off, zaxis=axis_off,
            aspectmode="cube",
            bgcolor="rgba(0,0,0,0)",
            camera=dict(eye=dict(x=1.4, y=1.4, z=0.6)),
        ),
        margin=dict(l=0, r=0, t=40, b=0),
        height=420,
    )
    return fig


# ── 2-D Bloch view (Matplotlib fallback for browsers without WebGL) ───────────
def bloch_2d_fig(statevector, title="Your qubit (2D view)"):
    """
    Flat X-Z slice of the Bloch sphere drawn with Matplotlib.
    Complete (not a projection) for X, H, Z, and RY gates: their real-valued
    matrices keep the Bloch vector in this plane.
    """
    import numpy as np

    a, b = statevector.data[0], statevector.data[1]
    bx = 2 * (np.conj(a) * b).real
    bz = abs(a) ** 2 - abs(b) ** 2

    fig, ax = plt.subplots(figsize=(4.4, 4.4), facecolor=BG_MID)
    ax.set_facecolor(BG_DEEP)

    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(t), np.sin(t), color=PURPLE2, lw=1.6)
    ax.axhline(0, color=GOLD, lw=1.1, ls="--", alpha=0.65)
    ax.axvline(0, color="#6b7280", lw=0.8, ls=":", alpha=0.6)

    ax.annotate(
        "", xy=(bx, bz), xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=GOLD2, lw=3.2, mutation_scale=24),
    )

    ax.text(0, 1.14, "|0⟩  Heads", ha="center", color=GOLD2, fontsize=11, fontweight="bold")
    ax.text(0, -1.24, "|1⟩  Tails", ha="center", color=MUTED, fontsize=11, fontweight="bold")
    ax.text(1.04, 0.05, "superposition", color=GOLD, fontsize=8, alpha=0.9)

    ax.set_xlim(-1.4, 1.55)
    ax.set_ylim(-1.4, 1.35)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, color=GOLD, fontsize=11, fontweight="bold", pad=8)
    fig.tight_layout()
    return fig


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
