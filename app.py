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
# Custom CSS
# ─────────────────────────────────────────────

st.markdown("""
<style>
    /* ── Import Font ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ── Global ── */
    html, body, .stApp {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%);
    }

    /* ── Header ── */
    .hero-header {
        text-align: center;
        padding: 2rem 1rem 1rem;
        margin-bottom: 1.5rem;
    }

    .hero-header h1 {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00d2ff, #7b2ff7, #ff6ec7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.3rem;
        letter-spacing: -0.02em;
    }

    .hero-header p {
        color: #8892b0;
        font-size: 1.05rem;
        font-weight: 300;
        letter-spacing: 0.03em;
    }

    /* ── Metric Cards ── */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 1rem;
        margin-bottom: 1.5rem;
    }

    .metric-card {
        background: linear-gradient(145deg, rgba(30,30,60,0.8), rgba(20,20,45,0.9));
        border: 1px solid rgba(123,47,247,0.25);
        border-radius: 16px;
        padding: 1.2rem 1.4rem;
        text-align: center;
        backdrop-filter: blur(10px);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(123,47,247,0.2);
    }

    .metric-label {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #8892b0;
        margin-bottom: 0.4rem;
    }

    .metric-value {
        font-size: 1.6rem;
        font-weight: 700;
        color: #e6f1ff;
    }

    .metric-value.bullish { color: #00e676; }
    .metric-value.bearish { color: #ff5252; }
    .metric-value.neutral { color: #ffc107; }

    /* ── Analysis Sections ── */
    .section-card {
        background: linear-gradient(145deg, rgba(22,22,48,0.85), rgba(15,15,35,0.95));
        border: 1px solid rgba(123,47,247,0.15);
        border-radius: 16px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1.2rem;
        backdrop-filter: blur(12px);
    }

    .section-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ccd6f6;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .section-body {
        color: #a8b2d1;
        font-size: 0.92rem;
        line-height: 1.7;
    }

    /* ── Progress Steps ── */
    .step-tracker {
        background: rgba(22,22,48,0.7);
        border: 1px solid rgba(123,47,247,0.2);
        border-radius: 14px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.5rem;
    }

    .step-item {
        display: flex;
        align-items: center;
        gap: 0.7rem;
        padding: 0.45rem 0;
        font-size: 0.88rem;
        color: #8892b0;
    }

    .step-item.active {
        color: #7b2ff7;
        font-weight: 600;
    }

    .step-item.done {
        color: #00e676;
    }

    .step-time {
        margin-left: auto;
        font-size: 0.78rem;
        font-family: 'Courier New', monospace;
        color: #5a6785;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d0d1a, #1a1a2e) !important;
        border-right: 1px solid rgba(123,47,247,0.15);
    }

    section[data-testid="stSidebar"] .stMarkdown h2 {
        color: #ccd6f6;
    }

    /* ── Button ── */
    .stButton > button {
        background: linear-gradient(135deg, #7b2ff7, #00d2ff) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 0.7rem 2rem !important;
        letter-spacing: 0.03em !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(123,47,247,0.4) !important;
    }

    /* ── Expander ── */
    .streamlit-expanderHeader {
        font-weight: 600 !important;
        color: #ccd6f6 !important;
        background: rgba(22,22,48,0.6) !important;
        border-radius: 10px !important;
    }

    /* ── Footer ── */
    .footer-bar {
        text-align: center;
        padding: 1.5rem;
        color: #5a6785;
        font-size: 0.78rem;
        margin-top: 2rem;
        border-top: 1px solid rgba(123,47,247,0.1);
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────

st.markdown("""
<div class="hero-header">
    <h1>Agentic Stock Analyzer</h1>
    <p>Multi-Agent AI System &nbsp;·&nbsp; LangGraph Orchestration &nbsp;·&nbsp; Ollama Mistral</p>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────

with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    st.markdown("---")

    ticker = st.text_input(
        "🏷️ Ticker Symbol",
        value="AAPL",
        placeholder="e.g. AAPL, TSLA, RELIANCE.NS",
        help="Enter a valid Yahoo Finance ticker symbol."
    )

    st.markdown("")
    run_analysis = st.button("🚀 Run Analysis", use_container_width=True)

    st.markdown("---")
    st.markdown("### 🧩 Agent Pipeline")
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
        '<p style="color:#5a6785; font-size:0.8rem; text-align:center;">'
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


def render_metric_card(label: str, value, css_class: str = "") -> str:
    """Render a single metric card as HTML."""
    return f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value {css_class}">{value}</div>
    </div>
    """


def render_dict_as_table(data: dict) -> str:
    """Convert a dict into a clean markdown table."""
    rows = []
    for k, v in data.items():
        label = k.replace("_", " ").title()
        rows.append(f"| **{label}** | `{v}` |")
    header = "| Metric | Value |\n|:---|:---|\n"
    return header + "\n".join(rows)


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

    # ── Pipeline Steps ──
    steps = [
        ("🔍", "Market Analysis"),
        ("📐", "Quant Analysis"),
        ("📰", "News Analysis"),
        ("⚠️", "Risk Analysis"),
        ("🛡️", "Risk Review"),
        ("📝", "Report Generation"),
        ("🪞", "Reflection"),
        ("👨‍💼", "Supervisor Decision"),
    ]

    # ── Progress Container ──
    st.markdown(f"### Analyzing **{ticker_clean}**")

    progress_bar = st.progress(0)
    status_text = st.empty()
    step_container = st.empty()

    # ── Execute Graph ──
    total_start = time.time()
    status_text.info("⏳ Running multi-agent pipeline — this may take a few minutes...")

    try:
        result = graph.invoke(initial_state)
        total_elapsed = time.time() - total_start

        progress_bar.progress(100)
        status_text.success(
            f"✅ Analysis complete — Total time: **{format_time(total_elapsed)}**"
        )

    except Exception as e:
        progress_bar.progress(0)
        status_text.error(f"❌ Pipeline failed: {e}")
        st.exception(e)
        st.stop()

    # ─────────────────────────────────────────
    # Render Results
    # ─────────────────────────────────────────

    st.markdown("---")

    # ── Key Metrics Strip ──
    market = result.get("market_analysis", {})
    quant = result.get("quant_analysis", {})
    risk = result.get("risk_analysis", {})

    trend_cls = sentiment_class(market.get("trend", ""))
    signal_cls = sentiment_class(quant.get("signal", ""))
    risk_cls = "bearish" if risk.get("risk_profile") == "high" else (
        "neutral" if risk.get("risk_profile") == "moderate" else "bullish"
    )
    rec_cls = sentiment_class(quant.get("recommendation", ""))

    st.markdown(f"""
    <div class="metric-grid">
        {render_metric_card("Close Price", f'₹{market.get("close_price", "—")}')}
        {render_metric_card("Trend", market.get("trend", "—"), trend_cls)}
        {render_metric_card("RSI", market.get("rsi", "—"))}
        {render_metric_card("MACD Signal", market.get("macd_signal", "—"), sentiment_class(market.get("macd_signal", "")))}
        {render_metric_card("Quant Signal", quant.get("signal", "—").upper(), signal_cls)}
        {render_metric_card("Confidence", f'{quant.get("confidence_score", "—")}%')}
        {render_metric_card("Risk Profile", risk.get("risk_profile", "—").upper(), risk_cls)}
        {render_metric_card("Recommendation", quant.get("recommendation", "—"), rec_cls)}
    </div>
    """, unsafe_allow_html=True)

    # ─────────────────────────────────────────
    # Section: Market Analysis
    # ─────────────────────────────────────────

    col1, col2 = st.columns(2)

    with col1:
        with st.expander("🔍 Market Analysis", expanded=True):
            if isinstance(market, dict) and market:
                st.markdown(render_dict_as_table(market))
            else:
                st.info("No market analysis data available.")

    with col2:
        with st.expander("📐 Quant Analysis", expanded=True):
            if isinstance(quant, dict) and quant:
                st.markdown(render_dict_as_table(quant))
            else:
                st.info("No quant analysis data available.")

    # ─────────────────────────────────────────
    # Section: Risk & News
    # ─────────────────────────────────────────

    col3, col4 = st.columns(2)

    with col3:
        with st.expander("⚠️ Risk Analysis", expanded=True):
            if isinstance(risk, dict) and risk:
                st.markdown(render_dict_as_table(risk))
                review = result.get("risk_review", "")
                if review:
                    st.markdown("---")
                    st.markdown(f"**🛡️ Risk Review:** {review}")
            else:
                st.info("No risk analysis data available.")

    with col4:
        with st.expander("📰 News Analysis", expanded=True):
            news = result.get("news_analysis", {})
            if isinstance(news, dict) and news:
                st.markdown(f"**Headlines Scanned:** `{news.get('headline_count', 0)}`")
                st.markdown("---")

                headlines = news.get("headlines", [])
                if headlines:
                    for i, h in enumerate(headlines, 1):
                        st.markdown(f"{i}. {h}")
                    st.markdown("---")

                analysis_text = news.get("analysis", "")
                if analysis_text:
                    st.markdown("**LLM Sentiment Summary:**")
                    st.markdown(analysis_text)
            else:
                st.info("No news analysis data available.")

    # ─────────────────────────────────────────
    # Section: Report
    # ─────────────────────────────────────────

    with st.expander("📝 Full Report", expanded=True):
        report = result.get("report", "")
        if report:
            st.markdown(report)
        else:
            st.info("No report generated.")

    # ─────────────────────────────────────────
    # Section: Reflection
    # ─────────────────────────────────────────

    with st.expander("🪞 Reflection (Self-Critique)", expanded=True):
        reflection = result.get("reflection", "")
        if reflection:
            st.markdown(reflection)
        else:
            st.info("No reflection available.")

    # ─────────────────────────────────────────
    # Section: Supervisor Decision
    # ─────────────────────────────────────────

    with st.expander("👨‍💼 Supervisor Decision", expanded=True):
        decision = result.get("supervisor_decision", "")
        if decision:
            st.markdown(decision)
        else:
            st.info("No supervisor decision available.")

    # ─────────────────────────────────────────
    # Execution Timing
    # ─────────────────────────────────────────

    st.markdown("---")
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">⏱️ Execution Summary</div>
        <div class="section-body">
            <strong>Ticker:</strong> {ticker_clean}<br>
            <strong>Total Execution Time:</strong> {format_time(total_elapsed)}<br>
            <strong>Timestamp:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}<br>
            <strong>Agents Invoked:</strong> Market → Quant → Risk → News → Report → Reflection → Supervisor
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ─────────────────────────────────────────
    # Save to Memory
    # ─────────────────────────────────────────

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
        st.toast("💾 Analysis saved to memory.", icon="✅")
    except Exception as e:
        st.warning(f"⚠️ Could not save to memory: {e}")

else:
    # ─────────────────────────────────────────
    # Landing State
    # ─────────────────────────────────────────

    st.markdown("""
    <div style="text-align:center; padding: 4rem 2rem;">
        <p style="font-size: 4rem; margin-bottom: 0.5rem;">🤖</p>
        <h2 style="color: #ccd6f6; font-weight: 600; margin-bottom: 0.8rem;">
            Ready to Analyze
        </h2>
        <p style="color: #8892b0; font-size: 1rem; max-width: 500px; margin: 0 auto; line-height: 1.7;">
            Enter a ticker symbol in the sidebar and click
            <strong style="color:#7b2ff7;">Run Analysis</strong>
            to launch the multi-agent pipeline.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Feature cards
    st.markdown("")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size:2rem; margin-bottom:0.5rem;">📈</div>
            <div class="metric-label">Market Analysis</div>
            <div style="color:#a8b2d1; font-size:0.82rem; margin-top:0.3rem;">
                SMA, RSI, MACD, ATR & volatility signals
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size:2rem; margin-bottom:0.5rem;">🧠</div>
            <div class="metric-label">Multi-Agent AI</div>
            <div style="color:#a8b2d1; font-size:0.82rem; margin-top:0.3rem;">
                7 specialized agents with conditional routing
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size:2rem; margin-bottom:0.5rem;">🛡️</div>
            <div class="metric-label">Risk Management</div>
            <div style="color:#a8b2d1; font-size:0.82rem; margin-top:0.3rem;">
                Sharpe ratio, drawdown & volatility profiling
            </div>
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
