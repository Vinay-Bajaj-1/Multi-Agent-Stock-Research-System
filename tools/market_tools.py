import yfinance as yf
import pandas as pd
import ta


def fetch_stock_data(ticker: str,
                     period: str = "2y",
                     interval: str = "1d") -> pd.DataFrame:

    df = yf.download(
        ticker,
        period=period,
        interval=interval,
        auto_adjust=True
    )
    if isinstance(df.columns, type(df.columns)):
        df.columns = df.columns.get_level_values(0)

    if df.empty:
        raise ValueError(f"No data found for {ticker}")

    return df


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:

    # Moving averages
    df["SMA20"] = ta.trend.sma_indicator(df["Close"], window=20)
    df["SMA50"] = ta.trend.sma_indicator(df["Close"], window=50)

    # RSI
    df["RSI"] = ta.momentum.rsi(df["Close"], window=14)

    # MACD
    macd = ta.trend.MACD(df["Close"])

    df["MACD"] = macd.macd()
    df["MACD_SIGNAL"] = macd.macd_signal()

    # ATR
    df["ATR"] = ta.volatility.average_true_range(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        window=14
    )

    # Daily returns
    df["Returns"] = df["Close"].pct_change()

    # Rolling volatility
    df["Volatility"] = (
        df["Returns"]
        .rolling(window=20)
        .std() * (252 ** 0.5)
    )

    df.dropna(inplace=True)

    return df