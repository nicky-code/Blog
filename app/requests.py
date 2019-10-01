import urllib.request,json
from .models import Quote 


# base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']
    print(base_url)
def getQuotes():
    '''
    Function that gets the json response to our url request
    '''
    quote_object=None
    
    # get_quotes_url = base_url.format(Quote,base_url)
    
    with urllib.request.urlopen(base_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)
        
        if get_quote_response:
            
            id = get_quote_response.get("id")
            author = get_quote_response.get("author")
            quote = get_quote_response.get("quote")
            quote_object = Quote(id,author,quote)
    
    return quote_object

    