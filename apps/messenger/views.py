from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.views import generic


from .templates import recived_message


import requests
import json


class BotView(generic.View):

	def get(self, request, *args, **kwargs):
		if self.request.GET['hub.verify_token'] == 'token':
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Error, invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)


	def post(self, request, *args, **kwargs):


		incoming_message = json.loads(self.request.body.decode('utf-8'))
		for entry in incoming_message['entry']:
			for message in entry['messaging']:

				if 'message' in message:
					recived_message(message)


		return HttpResponse()
