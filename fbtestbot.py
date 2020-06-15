from flask import Flask, request
import requests
import sys
import os
import json
from Credentials import * 
from utils import wit_response, show_buttons
from pymessenger import Bot

app = Flask(__name__)

bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def handle_verification():
    if request.args.get('hub.verify_token', '') == VERIFY_TOKEN:
        return request.args.get('hub.challenge', 200)
    else:
        return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def handle_messages():
    data = request.get_json()
    log(data)
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                if messaging_event.get('message'):
                    sender_id = messaging_event['sender']['id']
                    recipient_id = messaging_event['recipient']['id']
                    message_text = messaging_event['message']['text']

                    entity = wit_response(message_text)
                    log('Entity equals to ' + str(entity))
                    if entity == 'Welcome':
                        log(messaging_event['sender'])
                        response = 'Welcome ! I am SWYDNA O:) , your guide throughout this conversation.'
                        task = 'What do you want to do?'
                        send_message(sender_id, response)
                        send_message(sender_id, task)
                        buttons = show_buttons()
                        log(buttons)
                        bot.send_generic_message(sender_id, buttons['buttons'])
                    elif entity == 'asking':
                        task = 'What do you want?'
                        send_message(sender_id, task)
                    else:
                        send_message(sender_id, 'Sorry but I didn\'t understand what you are telling to me...')

                if messaging_event.get('delivery'):
                    pass

                if messaging_event.get('optin'):
                    pass

                if messaging_event.get('postback'):
                    pass

    return 'ok', 200

def send_message(recipient_id, message_text):
    log('Sending message to {recipient}: {text}'.format(recipient=recipient_id, text=message_text))
    params = {
        'access_token': PAGE_ACCESS_TOKEN
    }
    headers = {
        'Content-type': 'application/json'
    }
    data = json.dumps({
        'recipient':{
            'id': recipient_id
        },
        'message':{
            'text':message_text
        }
    })
    r = requests.post('https://graph.facebook.com/v2.6/me/messages', params=params, headers=headers, data=data)
    if r.status_code == 200:
        log(r.status_code)
    log(r.text)

def log(message):
    print(str(message))
    sys.stdout.flush()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
                