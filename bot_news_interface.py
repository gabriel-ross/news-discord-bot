from config import NEWS_QUERIES, LANGUAGE, NEWS_SOURCES
from news_query_helper import NewsQuery
from news_api_interface import NewsApi

class BotNewsInterface(object):

    def default_query(query: str):
        news_api_connection = NewsApi()
        return news_api_connection.get_news(NEWS_QUERIES[query])

