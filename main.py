from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.reuters.com/news/archive/us-the-wire?view=page&page=2&pageSize=10').text
soup = BeautifulSoup(html_text, 'lxml')
articles = soup.find_all('article', class_ = 'story')


# Title
print(articles[0].h3.text.strip())

# News story
print(articles[0].p.text.strip())

# Link to story
# articles[0].find('div', class_ = 'story-content').a['href']

print(f"reuters.com{articles[0].find('div', class_ = 'story-content').a['href']}")