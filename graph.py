from langgraph.graph import StateGraph, END

from agents.market_agent import MarketAgent
from agents.quant_agent import QuantAgent
from agents.risk_agent import RiskAgent
from agents.report_agent import ReportAgent
from agents.reflection_agent import ReflectionAgent
from agents.news_agent import NewsAgent
from agents.supervisor_agent import SupervisorAgent

from models.state import AgentState

from tools.market_tools import (
    fetch_stock_data,
    add_indicators
)

from tools.memory_manager import (
    get_last_analysis
)


# =========================
# Agent Initialization
# =========================

market_agent = MarketAgent()

quant_agent = QuantAgent()

risk_agent = RiskAgent()

report_agent = ReportAgent()

reflection_agent = ReflectionAgent()

news_agent = NewsAgent()

supervisor_agent = SupervisorAgent()


# =========================
# Nodes
# =========================

def market_node(state: AgentState):

    ticker = state["ticker"]

    previous_analysis = (
        get_last_analysis(ticker)
    )

    df = fetch_stock_data(ticker)

    df = add_indicators(df)

    market_analysis = (
        market_agent.analyze(df, ticker)
    )

    return {
        "df": df,
        "previous_analysis": previous_analysis,
        "market_analysis": market_analysis
    }


def quant_node(state: AgentState):

    quant_analysis = (
        quant_agent.analyze(state["df"])
    )

    return {
        "quant_analysis": quant_analysis
    }


def news_node(state: AgentState):

    news_analysis = (
        news_agent.analyze(state["ticker"])
    )

    return {
        "news_analysis": news_analysis
    }


def risk_node(state: AgentState):

    risk_analysis = (
        risk_agent.analyze(state["df"])
    )

    return {
        "risk_analysis": risk_analysis
    }


def risk_review_node(state: AgentState):

    risk = state["risk_analysis"]

    if risk["annual_volatility"] > 0.35:

        review = (
            "High volatility detected. "
            "Aggressive position sizing "
            "is not advised."
        )

    else:

        review = (
            "Volatility remains within "
            "acceptable limits."
        )

    return {
        "risk_review": review
    }


def report_node(state: AgentState):

    report = report_agent.generate_report(
        state["ticker"],
        state["market_analysis"],
        state["quant_analysis"],
        state["risk_analysis"],
        state["previous_analysis"],
        state["news_analysis"]
    )

    return {
        "report": report
    }


def reflection_node(state: AgentState):

    reflection = (
        reflection_agent.reflect(
            state["ticker"],
            state["market_analysis"],
            state["quant_analysis"],
            state["risk_analysis"],
            state["report"]
        )
    )

    return {
        "reflection": reflection
    }

def supervisor_node(state:AgentState):
    decision = (
        supervisor_agent.evaluate(
            state["ticker"],
            state["market_analysis"],
            state["quant_analysis"],
            state["risk_analysis"],
            state["news_analysis"],
            state["reflection"],
            state["previous_analysis"]
        )
    )

    return {
        "supervisor_decision": decision
    }
# =========================
# Conditional Router
# =========================

def route_risk(state: AgentState):

    volatility = (
        state["risk_analysis"]
        ["annual_volatility"]
    )

    if volatility > 0.25:
        return "risk_review"

    return "report"


# =========================
# Graph Definition
# =========================

workflow = StateGraph(AgentState)


# =========================
# Add Nodes
# =========================

workflow.add_node(
    "market",
    market_node
)

workflow.add_node(
    "quant",
    quant_node
)

workflow.add_node(
    "news",
    news_node
)

workflow.add_node(
    "risk",
    risk_node
)

workflow.add_node(
    "risk_review",
    risk_review_node
)

workflow.add_node(
    "report",
    report_node
)

workflow.add_node(
    "reflection",
    reflection_node
)

workflow.add_node(
    "supervisor",
    supervisor_node
)


# =========================
# Entry Point
# =========================

workflow.set_entry_point("market")


# =========================
# Parallel Branches
# =========================

workflow.add_edge(
    "market",
    "quant"
)

workflow.add_edge(
    "market",
    "news"
)


# =========================
# Quant → Risk
# =========================

workflow.add_edge(
    "quant",
    "risk"
)


# =========================
# Conditional Risk Routing
# =========================

workflow.add_conditional_edges(
    "risk",
    route_risk
)


# =========================
# High Risk Path
# =========================

workflow.add_edge(
    "risk_review",
    "report"
)


# =========================
# News → Report
# =========================

workflow.add_edge(
    "news",
    "report"
)


# =========================
# Final Stages
# =========================

workflow.add_edge(
    "report",
    "reflection"
)

workflow.add_edge(
    "reflection",
    "supervisor"
)

workflow.add_edge(
    "reflection",
    END
)


# =========================
# Compile Graph
# =========================

graph = workflow.compile()