from wit import Wit
from gnewsclient import gnewsclient
import requests


access_token = '3WERRC4MUKO4UK4JHNNJ33YX7KBDNDAN'

client = Wit(access_token = access_token)

def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    value = None

    try:
        entity = resp['intents'][0]['name']
    except:
        entity = None
    return (entity)

def show_buttons():

    buttons = {
        "buttons":[
            {
                "type":"web_url",
                "url":"https://www.messenger.com",
                "title":"Make a request"
            },
            {
                "type":"web_url",
                "url":"https://www.messenger.com",
                "title":"Make a donation"
            },
            {
                "type":"web_url",
                "url":"https://www.messenger.com",
                "title":"Get informed"
            }
        ],
        "quick_replies":[ 
            { 
                "content_type":"text", 
                "title":"Yes", 
                "payload":"YES" 
            }, 
            { 
                "content_type":"text", 
                "title":"No", 
                "payload":"NO",
            } 
        ] 
    }
                
     
    return buttons

