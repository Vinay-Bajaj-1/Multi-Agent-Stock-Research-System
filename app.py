"""
Streamlit Frontend for Agentic Stock Analyzer
=============================================
A multi-agent AI system that performs comprehensive
stock analysis using LangGraph orchestration.
"""

import streamlit as st
import time
import json
import warnings
from datetime import datetime

warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="Agentic Stock Analyzer",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# Compact CSS — Normal Theme
# ─────────────────────────────────────────────

st.markdown("""
<style>
    /* ── Import Font ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* ── Global ── */
    html, body, .stApp {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%);
    }

    /* ── Hide default Streamlit header/toolbar ── */
    header[data-testid="stHeader"] {
        display: none !important;
    }

    /* ── Reduce top padding ── */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0.5rem !important;
    }

    /* ── Compact Header ── */
    .compact-header {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        padding: 0.3rem 0 0.5rem;
        border-bottom: 1px solid rgba(123,47,247,0.25);
        margin-bottom: 0.8rem;
    }

    .compact-header h1 {
        font-size: 1.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00d2ff, #7b2ff7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        line-height: 1;
    }

    .compact-header .subtitle {
        font-size: 0.78rem;
        color: #8892b0;
        font-weight: 400;
    }

    /* ── Metric Strip ── */
    .metric-strip {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        margin-bottom: 0.7rem;
    }

    .m-card {
        flex: 1;
        min-width: 95px;
        background: linear-gradient(145deg, rgba(30,30,60,0.8), rgba(20,20,45,0.9));
        border: 1px solid rgba(123,47,247,0.2);
        border-radius: 8px;
        padding: 0.45rem 0.6rem;
        text-align: center;
        backdrop-filter: blur(10px);
    }

    .m-card .m-label {
        font-size: 0.6rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #8892b0;
        margin-bottom: 0.15rem;
    }

    .m-card .m-val {
        font-size: 1rem;
        font-weight: 700;
        color: #e6f1ff;
    }

    .m-val.bullish { color: #00e676; }
    .m-val.bearish { color: #ff5252; }
    .m-val.neutral { color: #ffc107; }

    /* ── Tab content area ── */
    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 0.5rem !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 0.3rem;
    }

    .stTabs [data-baseweb="tab"] {
        font-size: 0.82rem !important;
        padding: 0.35rem 0.7rem !important;
    }

    /* ── Compact data tables inside tabs ── */
    .compact-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 1.05rem;
    }

    .compact-table th {
        text-align: left;
        padding: 0.55rem 0.75rem;
        background: rgba(30,30,60,0.6);
        color: #ccd6f6;
        font-weight: 700;
        font-size: 1.1rem;
        border-bottom: 2px solid rgba(123,47,247,0.2);
    }

    .compact-table td {
        padding: 0.5rem 0.75rem;
        border-bottom: 1px solid rgba(123,47,247,0.08);
        color: #a8b2d1;
        font-size: 1.05rem;
    }

    .compact-table tr:hover {
        background: rgba(123,47,247,0.06);
    }

    /* ── Section text styling ── */
    .section-text {
        font-size: 1.05rem;
        line-height: 1.75;
        color: #a8b2d1;
    }

    /* ── Exec summary bar ── */
    .exec-bar {
        display: flex;
        gap: 1.5rem;
        flex-wrap: wrap;
        background: rgba(22,22,48,0.7);
        border: 1px solid rgba(123,47,247,0.15);
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-size: 0.8rem;
        color: #8892b0;
        margin-top: 0.5rem;
    }

    .exec-bar strong {
        color: #ccd6f6;
    }

    /* ── Footer ── */
    .footer-bar {
        text-align: center;
        padding: 0.6rem;
        color: #5a6785;
        font-size: 0.72rem;
        margin-top: 0.5rem;
        border-top: 1px solid rgba(123,47,247,0.1);
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d0d1a, #1a1a2e) !important;
        border-right: 1px solid rgba(123,47,247,0.15);
    }

    section[data-testid="stSidebar"] .stMarkdown h2 {
        font-size: 1.1rem;
        color: #ccd6f6;
    }

    /* ── Button ── */
    .stButton > button {
        background: linear-gradient(135deg, #7b2ff7, #00d2ff) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(123,47,247,0.4) !important;
    }

    /* ── Landing feature cards ── */
    .feature-card {
        background: linear-gradient(145deg, rgba(30,30,60,0.8), rgba(20,20,45,0.9));
        border: 1px solid rgba(123,47,247,0.2);
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
        backdrop-filter: blur(10px);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(123,47,247,0.2);
    }

    .feature-icon { font-size: 2rem; margin-bottom: 0.4rem; }
    .feature-label { font-size: 0.85rem; font-weight: 600; color: #ccd6f6; }
    .feature-desc { font-size: 0.78rem; color: #8892b0; margin-top: 0.2rem; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────

with st.sidebar:
    st.markdown("## Configuration")
    st.markdown("---")

    ticker = st.text_input(
        "Ticker Symbol",
        value="AAPL",
        placeholder="e.g. AAPL, TSLA, RELIANCE.NS",
        help="Enter a valid Yahoo Finance ticker symbol.",
    )

    st.markdown("")
    run_analysis = st.button("Run Analysis", use_container_width=True)

    st.markdown("---")
    st.markdown("### Agent Pipeline")
    st.markdown("""
    ```
    Market Agent
      ├─→ Quant Agent → Risk Agent
      │        ↓
      │    Risk Review (conditional)
      │        ↓
      └─→ News Agent
              ↓
         Report Agent
              ↓
        Reflection Agent
              ↓
       Supervisor Agent
    ```
    """)

    st.markdown("---")
    st.markdown(
        '<p style="color:#94a3b8; font-size:0.8rem; text-align:center;">'
        'Powered by LangGraph + Ollama</p>',
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────

def format_time(seconds: float) -> str:
    """Format seconds into a human-readable string."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes}m {secs:.1f}s"


def sentiment_class(text: str) -> str:
    """Return CSS class based on sentiment keywords."""
    lower = str(text).lower()
    if any(w in lower for w in ["bullish", "buy", "strong"]):
        return "bullish"
    if any(w in lower for w in ["bearish", "sell", "weak"]):
        return "bearish"
    return "neutral"


def render_metric(label: str, value, css_class: str = "") -> str:
    """Render a single compact metric card HTML."""
    return f"""<div class="m-card">
        <div class="m-label">{label}</div>
        <div class="m-val {css_class}">{value}</div>
    </div>"""


def render_compact_table(data: dict) -> str:
    """Convert dict into a compact HTML table."""
    rows = ""
    for k, v in data.items():
        label = k.replace("_", " ").title()
        rows += f"<tr><td><strong>{label}</strong></td><td>{v}</td></tr>\n"
    return f"""<table class="compact-table">
        <thead><tr><th>Metric</th><th>Value</th></tr></thead>
        <tbody>{rows}</tbody>
    </table>"""


# ─────────────────────────────────────────────
# Header (compact)
# ─────────────────────────────────────────────

st.markdown("""
<div class="compact-header">
    <h1>Agentic Stock Analyzer</h1>
    <span class="subtitle">Multi-Agent AI · LangGraph · Ollama Mistral</span>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Main Execution
# ─────────────────────────────────────────────

if run_analysis:

    if not ticker.strip():
        st.error("❌ Please enter a valid ticker symbol.")
        st.stop()

    ticker_clean = ticker.strip().upper()

    # ── Lazy imports (avoid slow startup) ──
    with st.spinner("🔧 Loading agent framework..."):
        from graph import graph
        from models.state import AgentState
        from tools.memory_manager import save_memory

    # ── Initialize State ──
    initial_state: AgentState = {
        "ticker": ticker_clean,
        "df": None,
        "previous_analysis": {},
        "market_analysis": {},
        "quant_analysis": {},
        "risk_analysis": {},
        "news_analysis": {},
        "risk_review": "",
        "report": "",
        "reflection": "",
        "supervisor_decision": "",
    }

    # ── Execute Graph ──
    progress_bar = st.progress(0)
    status_text = st.empty()
    status_text.info(f"Analyzing **{ticker_clean}** — running multi-agent pipeline...")

    total_start = time.time()

    try:
        result = graph.invoke(initial_state)
        total_elapsed = time.time() - total_start

        progress_bar.progress(100)

    except Exception as e:
        progress_bar.progress(0)
        status_text.error(f"Pipeline failed: {e}")
        st.exception(e)
        st.stop()

    # ─────────────────────────────────────────
    # Results
    # ─────────────────────────────────────────

    market = result.get("market_analysis", {})
    quant = result.get("quant_analysis", {})
    risk = result.get("risk_analysis", {})
    news = result.get("news_analysis", {})
    report = result.get("report", "")
    reflection = result.get("reflection", "")
    decision = result.get("supervisor_decision", "")

    # ── Metric Strip ──
    trend_cls = sentiment_class(market.get("trend", ""))
    signal_cls = sentiment_class(quant.get("signal", ""))
    risk_cls = "bearish" if risk.get("risk_profile") == "high" else (
        "neutral" if risk.get("risk_profile") == "moderate" else "bullish"
    )
    rec_cls = sentiment_class(quant.get("recommendation", ""))

    st.markdown(f"""
    <div class="metric-strip">
        {render_metric("Close", f'₹{market.get("close_price", "—")}')}
        {render_metric("Trend", market.get("trend", "—"), trend_cls)}
        {render_metric("RSI", market.get("rsi", "—"))}
        {render_metric("MACD", market.get("macd_signal", "—"), sentiment_class(market.get("macd_signal", "")))}
        {render_metric("Signal", quant.get("signal", "—").upper(), signal_cls)}
        {render_metric("Confidence", f'{quant.get("confidence_score", "—")}%')}
        {render_metric("Risk", risk.get("risk_profile", "—").upper(), risk_cls)}
        {render_metric("Action", quant.get("recommendation", "—").upper(), rec_cls)}
    </div>
    """, unsafe_allow_html=True)

    # ── Tabbed Sections ──
    tab_market, tab_quant, tab_risk, tab_news, tab_report, tab_reflect, tab_super = st.tabs([
        "🔍 Market",
        "📐 Quant",
        "⚠️ Risk",
        "📰 News",
        "📝 Report",
        "🪞 Reflection",
        "👨‍💼 Supervisor",
    ])

    with tab_market:
        if isinstance(market, dict) and market:
            st.markdown(render_compact_table(market), unsafe_allow_html=True)
        else:
            st.info("No market analysis data available.")

    with tab_quant:
        if isinstance(quant, dict) and quant:
            st.markdown(render_compact_table(quant), unsafe_allow_html=True)
        else:
            st.info("No quant analysis data available.")

    with tab_risk:
        if isinstance(risk, dict) and risk:
            st.markdown(render_compact_table(risk), unsafe_allow_html=True)
            review = result.get("risk_review", "")
            if review:
                st.markdown("---")
                st.markdown(f"**🛡️ Risk Review:** {review}")
        else:
            st.info("No risk analysis data available.")

    with tab_news:
        if isinstance(news, dict) and news:
            st.markdown(f"**Headlines Scanned:** `{news.get('headline_count', 0)}`")

            headlines = news.get("headlines", [])
            if headlines:
                for i, h in enumerate(headlines, 1):
                    st.markdown(f"{i}. {h}")
                st.markdown("---")

            analysis_text = news.get("analysis", "")
            if analysis_text:
                st.markdown("**LLM Sentiment Summary:**")
                st.markdown(f'<div class="section-text">{analysis_text}</div>', unsafe_allow_html=True)
        else:
            st.info("No news analysis data available.")

    with tab_report:
        if report:
            st.markdown(f'<div class="section-text">{report}</div>', unsafe_allow_html=True)
        else:
            st.info("No report generated.")

    with tab_reflect:
        if reflection:
            st.markdown(f'<div class="section-text">{reflection}</div>', unsafe_allow_html=True)
        else:
            st.info("No reflection available.")

    with tab_super:
        if decision:
            st.markdown(f'<div class="section-text">{decision}</div>', unsafe_allow_html=True)
        else:
            st.info("No supervisor decision available.")

    # ── Execution Summary (inline bar) ──
    st.markdown(f"""
    <div class="exec-bar">
        <span><strong>Ticker:</strong> {ticker_clean}</span>
        <span><strong>Time:</strong> {format_time(total_elapsed)}</span>
        <span><strong>Completed:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</span>
        <span><strong>Pipeline:</strong> Market → Quant → Risk → News → Report → Reflection → Supervisor</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Save to Memory ──
    try:
        save_memory({
            "ticker": result["ticker"],
            "market_analysis": result["market_analysis"],
            "quant_analysis": result["quant_analysis"],
            "risk_analysis": result["risk_analysis"],
            "news_analysis": result["news_analysis"],
            "report": result["report"],
            "reflection": result["reflection"],
            "supervisor_decision": result["supervisor_decision"],
        })
        st.toast("Analysis saved to memory.", icon="✅")
    except Exception as e:
        st.warning(f"Could not save to memory: {e}")

else:
    # ─────────────────────────────────────────
    # Landing State
    # ─────────────────────────────────────────

    st.markdown("""
    <div style="text-align:center; padding: 2.5rem 1rem 1rem;">
        <p style="font-size: 3rem; margin-bottom: 0.3rem;">🤖</p>
        <h2 style="color: #ccd6f6; font-weight: 600; margin-bottom: 0.5rem; font-size: 1.3rem;">
            Ready to Analyze
        </h2>
        <p style="color: #8892b0; font-size: 0.9rem; max-width: 450px; margin: 0 auto; line-height: 1.6;">
            Enter a ticker symbol in the sidebar and click
            <strong style="color:#7b2ff7;">Run Analysis</strong>
            to launch the multi-agent pipeline.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Feature cards
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <div class="feature-label">Market Analysis</div>
            <div class="feature-desc">SMA, RSI, MACD, ATR & volatility signals</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-label">Multi-Agent AI</div>
            <div class="feature-desc">7 specialized agents with conditional routing</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🛡️</div>
            <div class="feature-label">Risk Management</div>
            <div class="feature-desc">Sharpe ratio, drawdown & volatility profiling</div>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────

st.markdown("""
<div class="footer-bar">
    Agentic Stock Analyzer &nbsp;·&nbsp; Built with Streamlit + LangGraph + Ollama
</div>
""", unsafe_allow_html=True)
