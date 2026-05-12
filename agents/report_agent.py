import ollama


class ReportAgent:

    def generate_report(
        self,
        ticker,
        market_data,
        quant_data,
        risk_data, 
        previous_analysis,
        news_analysis
    ):

        prompt = f"""
        You are a professional institutional equity research analyst.

        Analyze the following stock data and generate a concise report.

        Ticker: {ticker}

        Market Analysis:
        {market_data}

        Quant Analysis:
        {quant_data}

        Risk Analysis:
        {risk_data}

        PREVIOUS ANALYSIS:
        {previous_analysis}

        NEWS ANALYSIS:
        {news_analysis}

        Instructions:
        - Be concise and professional
        - Avoid generic explanations
        - Mention bullish/bearish signals clearly
        - Mention key risks
        - Give final outlook
        - Maximum 180 words
        - No disclaimer
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