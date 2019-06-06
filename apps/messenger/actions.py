from django.conf import settings

import requests
import json
import datetime
import time
from django.utils import timezone


def send_message(message):
	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token={}' .format(settings.FB_PAGE_ACCESS_TOKEN) 
	status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=message)


def serialize(message):
	return json.dumps(message)


def userfb(sender_id):
	res = requests.get('https://graph.facebook.com/v2.6/' + sender_id,
					params = {'access_token': settings.FB_PAGE_ACCESS_TOKEN } )

	data = json.loads(res.text)
	return data
