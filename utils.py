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

def QuickReply_CreatePayload(qk_payload):
        # this function constructs and returns a payload for the the quick reply button payload
        # pass in a tuple-of-list / list-of-lists
        # example : (['title1','payload'],['title2','payload'])
        quick_btns = []
        # constructs the payload 
        for i in range(len(qk_payload)):
            quick_btns.append(
                {
                    "content_type":"text",
                    "title":qk_payload[i][0],
                    "payload":qk_payload[i][1],
                }
            )
        return quick_btns

def QuickReply_Send(user_id,text,reply_payload):
        # quick reply for messenger
        # this method sends the request to fb
        params = {
            "access_token":access_token,
        }
        payload = {
          "recipient":{"id":user_id,},
          "message":{
            "text":"{}".format(text),
            "quick_replies":reply_payload,
          }
        }
        requests.post(
            "https://graph.facebook.com/v2.6/me/messages",
            params=params,
            data=payload,
            headers={
                'Content-type': 'application/json'
            }
        )

def send_quickreply(recipient_id,quick_reply_message,reply_options):
        # use this method to send quick replies
        # this method puts everything together
        # automatically constructs the payload for the buttons from the list
        reply_payload = QuickReply_CreatePayload(qk_payload=reply_options)
        QuickReply_Send(
                        user_id = recipient_id,
                        text = "{}".format(quick_reply_message),
                        reply_payload = reply_payload,
                    )
