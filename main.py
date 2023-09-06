from bs4 import BeautifulSoup
import requests
import openai

openai.api_key_path = '.env'

html_text = requests.get('https://www.reuters.com/news/archive/us-the-wire?view=page&page=2&pageSize=10').text
soup = BeautifulSoup(html_text, 'lxml')
articles = soup.find('div', class_ = 'news-headline-list').find_all('article')

last_ten = []

for article in articles:
    info = {}
    info['title'] = article.h3.text.strip()
    info['content'] = article.p.text.strip()
    info['link'] = f"reuters.com{article.find('div', class_ = 'story-content').a['href']}"
    last_ten.append(info)

print(last_ten[0])

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(chat_completion)
