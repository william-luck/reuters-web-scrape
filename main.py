from bs4 import BeautifulSoup
import requests
import openai

openai.api_key_path = '.env'

html_text = requests.get('https://www.reuters.com/news/archive/us-the-wire?view=page&page=2&pageSize=10').text
soup = BeautifulSoup(html_text, 'lxml')
articles = soup.find('div', class_ = 'news-headline-list').find_all('article')

last_ten = []

prompt_message = 'The following is a list, that repeats three sets of information related to a news story, containing title, the content, and link to the news story, int that order. Condense this information into a briefing format to be read by someone in five minutes or less. When necessary, provide the links or further information for context on specific stories. Think about: What should the reader know about to better understand these stories? What information should they read more about if they are interested it? What could be the impact of these new stories? Why is this news important?' 

for article in articles:
    article_info = {}

    article_info['title'] = article.h3.text.strip()
    article_info['content'] = article.p.text.strip()
    article_info['link'] = f"reuters.com{article.find('div', class_ = 'story-content').a['href']}"
    # last_ten.append(article.h3.text.strip())
    # last_ten.append(article.p.text.strip())
    # last_ten.append(f"reuters.com{article.find('div', class_ = 'story-content').a['href']}")
    last_ten.append(article_info)


# last_ten.insert(0, prompt_message)



for article in last_ten: 
    print(article)
    print('')
    requests.post('http://localhost:3000/posts', json = article)



# chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ', '.join(last_ten)}])
# print(chat_completion)
