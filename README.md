from bs4 import BeautifulSoup
import requests
from datetime import datetime

def scrape_the_verge():
    url = 'https://www.theverge.com/tech'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    for headline in soup.find_all('h2', class_='c-entry-box--compact__title'):
        title = headline.a.text.strip()
        link = headline.a['href']
        # Check if the article was published after January 1, 2022
        date_str = headline.find('time')['datetime']
        article_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
        if article_date >= datetime(2022, 1, 1):
            headlines.append({'title': title, 'link': link})
    return headlines
