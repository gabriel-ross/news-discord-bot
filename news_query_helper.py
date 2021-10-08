

class NewsQuery(object):
    def __init__(self, query_name=None, query=None, sources=None, 
    category=None, country=None, language=None, article_limit=5):


        if sources is not None and (country is not None or category is not None):
            raise ValueError("Sources cannot be selected with country or with category")

        self.query_name = query_name
        self.query = query
        self.sources = ",".join(sources) if sources else None
        self.category = category
        self.country = country
        self.language = language
        self.article_limit = article_limit

    def __repr__(self):
        return f'''NewsQueryHelper(query_name={self.query_name}, query={self.query}, sources={self.sources}, 
        category={self.category}, country={self.country}, language={self.language}, article_limit={self.article_limit}'''