import feedparser
import ollama

class NewsAgent:

    def analyze(self, ticker) -> dict:
        url = (
            f'https://news.google.com/rss/search?q={ticker}&hl=en-US&gl=US&ceid=US:en'
        )

        feed = feedparser.parse(url)

        headlines = []
        for entry in feed.entries[:10]:
            headlines.append(
                entry.title
            )

        combined_news = '\n'.join(headlines)
        prompt = f"""
            You are a financial news analyst.

            Analyze the following headlines
            for overall market sentiment.

            Ticker: {ticker}

            HEADLINES:
            {combined_news}

            Tasks:
            - Determine sentiment:
                bullish / bearish / neutral
            - Summarize key themes
            - Keep response concise
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

        return {
            'headline_count' : len(headlines),
            'headlines': headlines,
            'analysis' : response['message']['content']

        }
