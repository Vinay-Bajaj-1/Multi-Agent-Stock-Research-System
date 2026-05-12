import pandas as pd


class QuantAgent():


    def analyze(self, df: pd.DataFrame):


        latest = df.iloc[-1]
        score = 0

        if latest['RSI'] > 55:
            score += 20

        if latest['SMA20'] > latest['SMA50']:
            score += 30


        if latest['MACD'] > latest['MACD_SIGNAL']:
            score += 30


        if latest['Returns'] > 0:
            score += 20

        
        sma_distance = (
            abs(latest['SMA20'] - latest['SMA50'] / latest['Close'])
        )

        if sma_distance > 0.05:
            trend_strength = 'strong'
        elif sma_distance > 0.02:
            trend_strength = 'moderate'
        else:
            trend_strength = 'weak'

        if latest['Volatility'] > 0.35:
            volatility_regime = 'high'

        elif latest['Volatility'] > 0.20:
            volatility_regime = 'moderate'
        else:
            volatility_regime = 'low'


        if score >= 70:
            signal = "bullish"
        elif score >= 40:
            signal = "neutral"
        else:
            signal = "bearish"


        if score >= 70:
            recommendation = "BUY"
        elif score >= 40:
            recommendation = "HOLD"
        else:
            recommendation = "SELL"

        confidence_score = min(score, 100)

        return {
            'confidence_score' : float(confidence_score),
            'momentum_score' : score,
            'signal' : signal,
            'trend_strength' : trend_strength,
            'volatility_regime' : volatility_regime,
            'recommendation' : recommendation
        }

        
        

        
        
        
        
        