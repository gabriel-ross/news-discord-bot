import os
from news_query_helper import NewsQuery

BOT_TOKEN = os.getenv('BOT_TOKEN')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

if (BOT_TOKEN is None):
    print("No bot token provided. Exiting.")
    exit()

if (NEWS_API_KEY is None):
    print("No news API key found. Exiting.")
    exit()

UNITS = "imperial"
LANGUAGE = "en"

NEWS_SOURCES = [
"abc-news",
"al-jazeera-english",
"ars-technica",
"breitbart-news",
"business-insider",
"cbs-news",
"cnn",
"crypto-coins-news",
"fox-news",
"google-news",
"hacker-news",
"medical-news-today",
"msnbc",
"national-geographic",
"nbc-news",
"new-scientist",
"next-big-future",
"reuters",
"techcrunch",
"the-american-conservative",
"the-verge",
"the-wall-street-journal",
"usa-today"]


NEWS_QUERIES = {
    "business":NewsQuery(
        query_name="business",
        query=None,
        sources=None,
        category="business",
        country=None,
        language=LANGUAGE
    ),
    "science":NewsQuery(
        query_name="science",
        query=None,
        sources=None,
        category="science",
        country=None,
        language=LANGUAGE
    ),
    "sports":NewsQuery(
        query_name="sports",
        query=None,
        sources=None,
        category="sports",
        country=None,
        language=LANGUAGE
    ),
    "technology":NewsQuery(
        query_name="technology",
        query=None,
        sources=None,
        category="technology",
        country=None,
        language=LANGUAGE
    )
}