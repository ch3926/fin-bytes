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

# Make the News API request for the last week with domain filtering and top 50 articles
all_articles = newsapi.get_everything(
    q='stocks | stock market',
    from_param=from_date_str,
    to=to_date_str,
    language='en',
    sort_by='popularity',  # You can change this to 'relevancy' if needed
    domains=','.join(financial_news_domains),  # Convert the list to a comma-separated string
    page_size=30  # Limit the number of articles to 30
)

# Remove unwanted fields from each article
cleaned_articles = []
for article in all_articles['articles']:
    cleaned_article = {
        'source': article['source'],
        'title': article['title'],
        'description': article['description'],
        'url': article['url']
    }
    cleaned_articles.append(cleaned_article)

# Create a dictionary with cleaned data
cleaned_data = {
    'status': all_articles['status'],
    'totalResults': all_articles['totalResults'],
    'articles': cleaned_articles
}

# Convert the cleaned data to a JSON file
output_file_path = '/Users/namayjindal/Desktop/developer/fin-bytes/financial_news_articles.json'
with open(output_file_path, 'w') as json_file:
    json.dump(cleaned_data, json_file, indent=2)

print(f'Cleaned financial news articles saved to {output_file_path}')
