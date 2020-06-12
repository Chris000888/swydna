from wit import Wit

access_token = 'UGMCYQAPLYNFMI5UIWV4DP4IDSGDZHU7'

client = Wit(access_token = access_token)

def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    value = None

    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
    except:
        pass
    return (entity, value)
