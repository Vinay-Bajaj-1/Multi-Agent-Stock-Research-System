import numpy as np

class RiskAgent:


    def analyze(self, df):

        returns = df['Returns'].dropna()

        annual_volatility = (
            returns.std() * np.sqrt(252)
        )

        sharpe_ratio = (
            (returns.mean() / returns.std()) * np.sqrt(252)
        )


        cumulative_returns = (
            (1 + returns).cumprod()
        )

        rolling_max = cumulative_returns.cummax()
        

        drawdown = (
            cumulative_returns - rolling_max
        ) / rolling_max

        max_drawdown = drawdown.min()

        if annual_volatility > 0.35:
            risk_profile = 'high'
        elif annual_volatility > 0.20:
            risk_profile = 'moderate'
        else:
            risk_profile = 'low'

        result = {
            'annual_volatility': round(float(annual_volatility), 4),
            'sharpe_ratio': round(float(sharpe_ratio), 2),
            'max_drawdown': round(float(max_drawdown), 4),
            'risk_profile': risk_profile
        }

        return result