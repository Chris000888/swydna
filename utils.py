from wit import Wit
from gnewsclient import gnewsclient

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

        "message":{
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"button",
                "text":"What do you want to do next?",
                "buttons":[
                    {
                        "type":"web_url",
                        "url":"",
                        "title":"Make a request"
                    },
                    {
                        "type":"web_url",
                        "url":"",
                        "title":"Make a donation"
                    },
                    {
                        "type":"web_url",
                        "url":"",
                        "title":"Get informed"
                    }
                ]
            }
            }
        }
    }
                
     
    return buttons
