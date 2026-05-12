import ollama


class SupervisorAgent:

    def evaluate(self, ticker, market_analysis, quant_analysis, risk_analysis,  news_analysis, reflection, previous_analysis):
        prompt = f"""
        You are a senior portfolio manager.

        Your role is to make the FINAL investment decision
        after reviewing all agent analyses.

        Ticker:
        {ticker}

        MARKET ANALYSIS:
        {market_analysis}

        QUANT ANALYSIS:
        {quant_analysis}

        RISK ANALYSIS:
        {risk_analysis}

        NEWS ANALYSIS:
        {news_analysis}

        REFLECTION:
        {reflection}

        PREVIOUS ANALYSIS:
        {previous_analysis}

        Tasks:
        - Decide:
            BUY / HOLD / SELL
        - Assign confidence score (0-100)
        - Suggest position sizing:
            Small / Moderate / Large
        - Decide if human review is needed
        - Provide concise reasoning
        - Professional tone
        """

        response = ollama.chat(
            model = 'mistral',
            messages = [
                {
                    'role' : 'user',
                    'content' : prompt
                }
            ]
        )

        return response['message']['content']

