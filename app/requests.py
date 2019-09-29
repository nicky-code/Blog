from app import app
import json
import requests
from .models import Quote 


base_url = Config.QUOTE_API_BASE_URL
def getQuotes():
    random_quote = requests.get(base_url)
    new_quote = random_quote.json()
    id = new_quote.get("id")
    author = new_quote.get("author")
    quote = new_quote.get("quote")
    quote_object = Quote(id,author,quote)
    
    return quote_object

    