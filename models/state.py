from typing import TypedDict
import pandas as pd


class AgentState(TypedDict):

    ticker : str
    market_analysis : dict
    quant_analysis : dict
    risk_analysis : dict
    report : str
    reflection : str
    df : pd.DataFrame
    risk_review : str
    previous_analysis : dict
    news_analysis : dict
    supervisor_decision : str