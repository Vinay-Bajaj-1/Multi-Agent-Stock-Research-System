# Multi-Agent Financial Research System

## Overview

A stateful multi-agent financial research system built using:

* Python
* LangGraph
* Ollama
* Mistral
* Streamlit
* yFinance

The system performs autonomous financial analysis by orchestrating multiple specialized AI agents through a graph-based workflow.

It combines:

* Technical analysis
* Quantitative analysis
* Risk evaluation
* Financial news sentiment
* Reflection-based critique
* Supervisory decision-making
* Persistent memory

The project demonstrates advanced agentic AI architecture using shared state orchestration, conditional routing, parallel execution, memory retrieval, and multi-agent reasoning.

---

# Architecture

```text
                ┌─────────► Quant Agent
                │
Market Agent ───┼─────────► News Agent
                │
                └─────────► Risk Agent
                                  │
                                  ▼
                          Reflection Agent
                                  │
                                  ▼
                         Supervisor Agent
                                  │
                                  ▼
                           Final Decision
```

---

# Features

## Multi-Agent Workflow

The system consists of specialized agents:

| Agent            | Responsibility                            |
| ---------------- | ----------------------------------------- |
| Market Agent     | Technical market analysis                 |
| Quant Agent      | Momentum and trend scoring                |
| Risk Agent       | Volatility and risk metrics               |
| News Agent       | News retrieval and sentiment analysis     |
| Reflection Agent | Critiques contradictions and hidden risks |
| Supervisor Agent | Final investment decision-making          |

---

## LangGraph Orchestration

The workflow is orchestrated using LangGraph with:

* Shared state architecture
* Dynamic routing
* Parallel execution
* Conditional execution paths
* Fan-out / fan-in workflow synchronization

---

## Persistent Memory

The system stores historical analyses using JSON-based memory.

Stored information includes:

* Previous reports
* Reflections
* Supervisor decisions
* Risk analysis
* Quantitative metrics

This enables historical retrieval and context-aware reasoning.

---

## Reflection-Based Critique

The Reflection Agent evaluates:

* Contradictions in reasoning
* Hidden risks
* Overconfidence
* Risk-adjusted concerns

Example:

* Bullish momentum
* High volatility
* Negative Sharpe ratio

The reflection layer critiques whether the final recommendation is justified.

---

## Supervisor Decision Layer

The Supervisor Agent acts as a portfolio manager.

It evaluates:

* Market analysis
* Quantitative signals
* Risk metrics
* News sentiment
* Reflection critique
* Historical memory

And generates:

* Final BUY/HOLD/SELL decision
* Confidence score
* Position sizing recommendation
* Human review requirement

---

# Tech Stack

| Technology | Usage                     |
| ---------- | ------------------------- |
| Python     | Core programming language |
| LangGraph  | Agent orchestration       |
| Ollama     | Local LLM inference       |
| Mistral    | LLM model                 |
| yFinance   | Market data retrieval     |
| TA Library | Technical indicators      |
| Feedparser | Financial news retrieval  |
| Streamlit  | Frontend interface        |
| JSON       | Persistent memory storage |

---

# Workflow

## Step 1 — Market Analysis

The Market Agent:

* Fetches OHLCV data
* Calculates indicators:

  * RSI
  * MACD
  * ATR
  * Volatility
* Determines market trend

---

## Step 2 — Parallel Execution

LangGraph executes:

* Quant Agent
* News Agent

in parallel.

This reduces workflow latency and demonstrates fan-out orchestration.

---

## Step 3 — Risk Analysis

The Risk Agent computes:

* Annual volatility
* Sharpe ratio
* Maximum drawdown
* Risk profile

---

## Step 4 — Conditional Routing

If volatility exceeds a threshold:

```python
if volatility > 0.25:
    return "risk_review"
```

LangGraph dynamically routes execution to:

* Risk Review Node

Otherwise it proceeds directly to reporting.

---

## Step 5 — Report Generation

The Report Agent synthesizes:

* Technical analysis
* Quantitative analysis
* Risk analysis
* News sentiment
* Historical context

into an institutional-style financial report.

---

## Step 6 — Reflection Layer

The Reflection Agent critiques:

* Contradictions
* Hidden risks
* Weak assumptions
* Recommendation quality

---

## Step 7 — Supervisor Decision

The Supervisor Agent generates:

* Final recommendation
* Confidence score
* Position sizing
* Human review escalation

---

# Example Output

## Supervisor Decision

```text
Decision: BUY

Confidence Score: 90

Position Sizing: Moderate

Human Review Needed: Yes

Reasoning:
The recommendation remains bullish based on favorable market conditions,
positive news sentiment, and strong quantitative momentum. However,
high volatility and downside risk require cautious position sizing.
```

---

# Folder Structure

```text
project/
│
├── agents/
│   ├── market_agent.py
│   ├── quant_agent.py
│   ├── risk_agent.py
│   ├── news_agent.py
│   ├── report_agent.py
│   ├── reflection_agent.py
│   └── supervisor_agent.py
│
├── models/
│   └── state.py
│
├── tools/
│   ├── market_tools.py
│   └── memory_manager.py
│
├── memory/
│   └── history.json
│
├── graph.py
├── main.py
├── app.py
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

Install Ollama:

[https://ollama.com/](https://ollama.com/)

Pull Mistral:

```bash
ollama pull mistral
```

Start Ollama:

```bash
ollama serve
```

---

# Run Project

## CLI Mode

```bash
python main.py
```

---

## Streamlit Frontend

```bash
streamlit run app.py
```

---

# Future Improvements

Potential future upgrades:

* Vector database memory
* Portfolio-level analysis
* Multi-stock screening
* Real-time streaming data
* Advanced RAG integration
* Earnings transcript analysis
* API deployment
* Cloud deployment
* Agent performance analytics

---

# Key Engineering Concepts Demonstrated

* Agentic AI workflows
* Shared state orchestration
* Reflection-based reasoning
* Dynamic graph routing
* Parallel execution
* Persistent memory systems
* Multi-agent collaboration
* Local LLM deployment
* Context-aware reasoning
* Supervisor decision architecture

---

# License

MIT License
