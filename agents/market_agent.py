import pandas as pd

class MarketAgent:

    def analyze(self, df : pd.DataFrame, ticker: str) -> dict:

        

        latest = df.iloc[-1]

        trend = (
            "Bullish"
            if latest["SMA20"] > latest["SMA50"]
            else "Bearish"
        )

        macd_signal = (
            "Bullish"
            if latest["MACD"] > latest["MACD_SIGNAL"]
            else "Bearish"
        )

        result = {
            "ticker": ticker,
            "close_price": round(float(latest["Close"]), 2),
            "trend": trend,
            "rsi": round(float(latest["RSI"]), 2),
            "macd_signal": macd_signal,
            "atr": round(float(latest["ATR"]), 2),
            "volatility": round(float(latest["Volatility"]), 4)
        }

        return result