from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class MessengerUser(models.Model):

	user_id = models.CharField(
		primary_key = True,
		max_length = 250
		
	)

	first_name = models.CharField(
		verbose_name=_('Nombre'),
		max_length = 250
	)

	last_name = models.CharField(
		verbose_name=_('Apellido'),
		max_length = 250
	)

	gender = models.CharField(
		verbose_name=_('Genero'),
		max_length = 250
	)

	timezone = models.CharField(
		verbose_name = _('Zona Horaria'),
		max_length = 255
	)


	image = models.CharField(
		verbose_name = _('image'),
		max_length = 255		
	)

	date = models.CharField(
		verbose_name = _('Fecha de Registro'),
		max_length = 255
	)


	class Meta:
		ordering = ['user_id']
		verbose_name_plural = "Usuarios"    

	def __str__(self):
		return self.first_name



class Dates(models.Model):

	name = models.CharField(max_length=255)
	date = models.DateTimeField()

	def __str__(self):
		return str(self.name)