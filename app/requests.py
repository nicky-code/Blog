from app import app
import json
import requests
from .models import Quote 


base_url = None

def config_request(app):
    global base_url
    
    # Getting the quote base url
base_url = app.config["QUOTE_API_BASE_URL"]