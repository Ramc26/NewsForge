import requests
from newsapi import NewsApiClient
import json
from dataclasses import dataclass

@dataclass
class ArticleData:
    source: str
    title: str
    # src_icon:str
    date:str
    desc: str
    url: str
    image: str
    # content: str

# newsapi = NewsApiClient(api_key='084ee06c24f0421b9fed397cb4b21d8f')
# query=input()
# url=f'https://newsdata.io/api/1/news?apikey=pub_40118922316862ca8ce45e8c136c1b24989c7&q=pizza&language=en'
#     # url = f'https://newsapi.org/v2/everything?q={query}&apiKey=084ee06c24f0421b9fed397cb4b21d8f'
# resp = requests.get(url).json()

# # Pretty-print the JSON response with indentation
# print(json.dumps(resp, indent=4))
# query=input()
def getNews(query,lang,category):
    query=query.replace(" ", "%20")
    if lang == "" and category == "":
        url=f'https://newsdata.io/api/1/news?apikey=pub_40118922316862ca8ce45e8c136c1b24989c7&q={query}'
    elif category=="":
        url=f'https://newsdata.io/api/1/news?apikey=pub_40118922316862ca8ce45e8c136c1b24989c7&q={query}&language={lang}'
    else:
        url=f'https://newsdata.io/api/1/news?apikey=pub_40118922316862ca8ce45e8c136c1b24989c7&q={query}&language={lang}&category={category}'

    # url = f'https://newsapi.org/v2/everything?q={query}&apiKey=084ee06c24f0421b9fed397cb4b21d8f'
    resp = requests.get(url).json()
    print(json.dumps(resp, indent=4))
    # print(resp.json(indent=4))
    if resp.get('status') == 'success' and resp.get('totalResults') > 0:
        articles = resp.get('results')[:10]
        news_data = []
        for article in articles:
            data = ArticleData(
                source=article.get('source_id'),
                # icon=article.get('source_icon'),
                title=article.get('title'),
                date=article.get('pubDate'),
                desc=article.get('description'),
                url=article.get('link'),
                image=article.get('image_url'),
                # content=article.get('content')
            )

            print(data)
            news_data.append(data)

            # print(news_data)
        return news_data
    elif resp.get('status') == 'error':
        return "No articles found"

def getNewsTe():
    url=f'https://newsdata.io/api/1/news?apikey=pub_40118922316862ca8ce45e8c136c1b24989c7&language=te'
    resp = requests.get(url).json()
    print(json.dumps(resp, indent=4))
    # print(resp.json(indent=4))
    if resp.get('status') == 'success' and resp.get('totalResults') > 0:
        articles = resp.get('results')[:10]
        news_data = []
        for article in articles:
            data = ArticleData(
                source=article.get('source_id'),
                # icon=article.get('source_icon'),
                title=article.get('title'),
                date=article.get('pubDate'),
                desc=article.get('description'),
                url=article.get('link'),
                image=article.get('image_url'),
                # content=article.get('content')
            )

            print(data)
            news_data.append(data)

            # print(news_data)
        return news_data
    elif resp.get('status') == 'error':
        return "No articles found"
    

def getNewsEn():
    url=f'https://newsdata.io/api/1/news?apikey=pub_40118922316862ca8ce45e8c136c1b24989c7&language=En'
    resp = requests.get(url).json()
    print(json.dumps(resp, indent=4))
    # print(resp.json(indent=4))
    if resp.get('status') == 'success' and resp.get('totalResults') > 0:
        articles = resp.get('results')[:10]
        news_data = []
        for article in articles:
            data = ArticleData(
                source=article.get('source_id'),
                # icon=article.get('source_icon'),
                title=article.get('title'),
                date=article.get('pubDate'),
                desc=article.get('description'),
                url=article.get('link'),
                image=article.get('image_url'),
                # content=article.get('content')
            )

            print(data)
            news_data.append(data)

            # print(news_data)
        return news_data
    elif resp.get('status') == 'error':
        return "No articles found"

