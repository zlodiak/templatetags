from django.db import models
from datetime import datetime  

from sorl.thumbnail import ImageField


class Slider(models.Model):
	slide = models.ImageField(
		upload_to='uploads/slider/', 
		blank=True,
		null=True,
	)							
	text = models.TextField(
		'Сопроводительнй текст',
		max_length=500, 
		blank=True,
	)	
	date = models.DateTimeField(
		'Дата создания',
		#default=datetime.now(),
		auto_now=True,
	)	
	is_active = models.BooleanField(default=True)			

	@classmethod
	def get_all_entries(self):
		return self.objects.filter(is_active=True).order_by('-date')				
			
	

