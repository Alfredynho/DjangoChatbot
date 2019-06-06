from .actions import serialize

def typing(sender_id):
	message_data = {
			'recipient': { 'id' : sender_id },
			'sender_action': 'typing_on'
	}
	return serialize(message_data)


def send_text(sender_id,message):

	message_data = {
				'recipient':{
					'id':sender_id
				},
	  			'message':{
	  				'text':message
	  			}
	 		}

	return serialize(message_data)