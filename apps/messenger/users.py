import requests
import json

from django.conf import settings

import datetime
import time
from django.utils import timezone

from apps.messenger.models import MessengerUser


def userfb(sender_id):
	res = requests.get('https://graph.facebook.com/v2.6/' + sender_id,
					params = {'access_token': settings.FB_PAGE_ACCESS_TOKEN } )



	data = json.loads(res.text)
	return data


def user_save(user):

	_user = MessengerUser()

	_user.user_id = user['id']
	_user.first_name = user['first_name']
	_user.last_name = user['last_name']
	_user.gender = "masculino"
	_user.timezone = "zona horaria"
	_user.image = "imagen"
	_user.date = datetime.datetime.now()
	_user.suscription = True

	_user.save()