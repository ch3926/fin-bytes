"""from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='01246e43061d4f3f981373160e2b4ec5')


# /v2/everything
all_articles = newsapi.get_everything(q='stocks',
                                      #sources='bbc-news,the-verge',
                                      #domains='bbc.co.uk,techcrunch.com',
                                      from_param='2023-12-01',
                                      to='2023-12-02',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)"""


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

# Make the News API request for the last week
all_articles = newsapi.get_everything(
    q='stocks',
    from_param=from_date_str,
    to=to_date_str,
    language='en',
    sort_by='relevancy',
    page=2
)

# Convert the articles to a JSON file
output_file_path = '/Users/namayjindal/Desktop/developer/fin-bytes/news_articles.json'
with open(output_file_path, 'w') as json_file:
    json.dump(all_articles, json_file, indent=2)

print(f'Articles saved to {output_file_path}')




