from django.db import models
from datetime import datetime  


class Feedback(models.Model):
	author = models.CharField(
		'Автор',
		max_length=100, 
		blank=False,
	)	
	subject = models.CharField(
		'Тема',
		max_length=100, 
		blank=False,
	)			
	message = models.TextField(
		'Сообщение',
		max_length=500, 
		blank=True,
	)								
	date_create = models.DateTimeField(
		'Дата создания',
		#default=datetime.now(),
		auto_now=True,
	)			

					
			