import json
from datetime import datetime, timedelta
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='01246e43061d4f3f981373160e2b4ec5')

# Calculate the date range for the last week
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

# Format dates in the required News API format (YYYY-MM-DD)
from_date_str = start_date.strftime('%Y-%m-%d')
to_date_str = end_date.strftime('%Y-%m-%d')

# List of relevant financial news domains
financial_news_domains = [
    'wsj.com',        # The Wall Street Journal
    'forbes.com',     # Forbes
    'bloomberg.com',  # Bloomberg
    'ft.com',         # Financial Times
    'cnbc.com',       # CNBC
    'reuters.com',    # Reuters
    'investopedia.com',  # Investopedia
    'marketwatch.com',  # MarketWatch
    'fool.com',       # The Motley Fool
    'seekingalpha.com'   # Seeking Alpha
]

# Make the News API request for the last week with domain filtering
all_articles = newsapi.get_everything(
    q='stocks | stock market',
    from_param=from_date_str,
    to=to_date_str,
    language='en',
    sort_by='relevancy',
    domains=','.join(financial_news_domains),  # Convert the list to a comma-separated string
    page=2
)

# Convert the articles to a JSON file
output_file_path = '/Users/namayjindal/Desktop/developer/fin-bytes/financial_news_articles.json'
with open(output_file_path, 'w') as json_file:
    json.dump(all_articles, json_file, indent=2)

print(f'Financial news articles saved to {output_file_path}')
