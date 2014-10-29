from django.contrib import admin
from app_slider.models import Slider

class SliderAdmin(admin.ModelAdmin):
	fields = ['slide', 'text', 'is_active', ]	
	list_display = ['date', 'slide', 'text', 'is_active', ]
	search_fields = ['text', ]
	
	class Meta:
		verbose_name = 'Слайд'
		verbose_name_plural = 'Слайды'		

	
admin.site.register(Slider, SliderAdmin)

