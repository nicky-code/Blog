import urllib.request,json
from .models import Quote 


# base_url = Config.QUOTE_API_BASE_URL

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']
    
def getQuotes():
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key)
    quote_object=None
    with urllib.request.urlopen(get_movies_url) as url:
        get_quote_data = url.read()
        new_quote = json.loads(get_quote_data)
    # random_quote = requests.get(base_url)
    # new_quote = random_quote.json()
        id = new_quote.get("id")
        author = new_quote.get("author")
        quote = new_quote.get("quote")
        quote_object = Quote(id,author,quote)
    
    return quote_object

    