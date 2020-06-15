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
        "quick_replies":[
            {
                "content_type":"text",
                "title":"Red",
                "payload":"<POSTBACK_PAYLOAD>",
                "image_url":"http://example.com/img/red.png"
            },
            {
                "content_type":"text",
                "title":"Green",
                "payload":"<POSTBACK_PAYLOAD>",
                "image_url":"http://example.com/img/green.png"
            }
        ]
    }

    """ buttons = {
        "buttons":[
            {
                "text":"Make a request",
                "value":"request"
            },
            {
                "text":"Make a donation",
                "value":"donation"
            },
            {
                "text":"Get informed",
                "value":"info"
            }
        ]
    } """
                
     
    return buttons
