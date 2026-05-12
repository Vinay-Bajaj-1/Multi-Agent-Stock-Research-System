from graph import graph
from tools.memory_manager import save_memory
from models.state import AgentState

import warnings

warnings.filterwarnings("ignore")

if __name__ == "__main__":

    state: AgentState = {

        "ticker": "E2E.NS",
        "df": None,
        "previous_analysis": {},
        "market_analysis": {},
        "quant_analysis": {},
        "risk_analysis": {},
        "news_analysis": {},
        "risk_review": "",
        "report": "",
        "reflection": "",
        "supervisor_decision": ""
    }

    # Run Graph
    result = graph.invoke(state)

    # Outputs
    print("\nFINAL REPORT:\n")
    print(result["report"])
    print("\nFINAL REFLECTION:\n")
    print(result["reflection"])
    print("\nSUPERVISOR DECISION:\n")
    print(result["supervisor_decision"])

    # Save Memory
    save_memory({
        "ticker": result["ticker"],
        "market_analysis":
            result["market_analysis"],
        "quant_analysis":
            result["quant_analysis"],
        "risk_analysis":
            result["risk_analysis"],
        "news_analysis":
            result["news_analysis"],
        "report":
            result["report"],
        "reflection":
            result["reflection"],
        "supervisor_decision":
            result["supervisor_decision"]
    })