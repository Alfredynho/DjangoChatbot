from django.conf import settings
from .users import userfb, user_save

import apiai
import json


from .actions import send_message
from .messages import typing, send_text


AI = apiai.ApiAI(settings.CLIENT_ACCESS_TOKEN_DIALOG_FLOW)    
MAX_TIME = 5
        

def recived_message(message):

    sender_id = message['sender']['id']
    
    message_text = message['message']['text']

    request = AI.text_request()

    request.query = message_text

    response = json.loads(request.getresponse().read().decode('utf-8'))
    
    print("SENDER_ID ", sender_id)
    speech = response['result']['fulfillment']['speech']

    _user_data = userfb(sender_id)
    print(_user_data)

    user_save(_user_data)

    # _action = response['result']['action']    
    send_message(typing(sender_id))
    send_message(send_text(sender_id, speech))  
