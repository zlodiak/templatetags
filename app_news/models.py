from django.db import models
from datetime import datetime  

from sorl.thumbnail import ImageField


class News(models.Model):
	image = models.ImageField(
		upload_to='uploads/news/', 
		blank=True,
		null=True,
	)	
	title = models.CharField(
		'Заголовок',
		max_length=100, 
		blank=False,
	)		
	teaser = models.TextField(
		'Вступительный текст',
		max_length=500, 
		blank=True,
	)								
	text = models.TextField(
		'Основной текст',
		max_length=50000, 
		blank=False,
	)	
	date_create = models.DateTimeField(
		'Дата создания',
		#default=datetime.now(),
		auto_now=True,
	)	
	date_event = models.DateTimeField(
		'Дата События',
		blank=False,
	)		
	is_active = models.BooleanField(default=True)			

	@classmethod
	def get_all_entries(self):
		return self.objects.filter(is_active=True).order_by('-date_event')	

	@classmethod
	def get_last_entries(self):
		return self.objects.filter(is_active=True).order_by('-date_event')[:3]							
			
	

