

from newsapi import NewsApiClient
from traceback import print_exc
import config as cfg

class NewsApi(object):
    def __init__(self, api_key=cfg.NEWS_API_KEY):
        self.api_key = api_key
        self.api_client = NewsApiClient(self.api_key)

    def get_news(self, query):
        try:
            
            response = self.api_client.get_top_headlines(
                q=query.query,
                sources=query.sources,
                category=query.category,
                language=query.language,
                country=query.country,
                page_size=query.article_limit)
            print("Connecting to news API")
            print(f"Status: {response['status']}")
            return self.format_stories(response)

        except:
            print("Error fetching news from API")
            print_exc()
            return []

    def format_stories(self, raw_api_response):
        response = []
        for article in raw_api_response["articles"]:
            response.append(Story(article))
        return response

class Story(object):
    def __init__(self, raw_api_response):
        self.source = raw_api_response["source"]["name"]
        self.author = raw_api_response["author"]
        self.title = raw_api_response["title"]
        self.description = raw_api_response["description"]
        self.url = raw_api_response["url"]

    def get_json(self):
        return {
            "source":self.source,
            "author":self.author,
            "title":self.title,
            "description":self.description,
            "url":self.url
        }

    def __str__(self):
        return f'Title: {self.title}\nSource: {self.source}\nURL: {self.url}\nDescription: {self.description}'