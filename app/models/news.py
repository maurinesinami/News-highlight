class News:
    '''
    News class to define News Objects
    '''
     def __init__(self, name, description, url, language, country):
        self.name = name
        self.description = description
        self.url = url
        self.language = language
        self.country = country
class Article:
    '''
    Article class to define article Objects
    '''

    def __init__(self,author, title, description, url, urlToImage,publishedAt ):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedA        