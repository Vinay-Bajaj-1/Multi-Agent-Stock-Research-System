import ollama

class ReflectionAgent:

    def reflect(self, ticker, market_data, quant_data, risk_data, report):
        prompt = f"""
        You are a senior hedge fund risk reviewer.

        Your job is to critically evaluate the stock analysis report.

        Ticker: {ticker}

        MARKET DATA:
        {market_data}

        QUANT DATA:
        {quant_data}

        RISK DATA:
        {risk_data}

        INITIAL REPORT:
        {report}

        Tasks:
        - Identify contradictions
        - Identify hidden risks
        - Check if recommendation is justified
        - Provide balanced final assessment
        - Keep response under 120 words
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

        
