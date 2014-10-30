from django.contrib import admin
from app_news.models import News

class NewsAdmin(admin.ModelAdmin):
	fields = ['image', 'title', 'teaser', 'text', 'date_event', 'is_active', ]	
	list_display = ['date_event', 'title', 'is_active', ]
	search_fields = ['title', ]
	
	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'		

	
admin.site.register(News, NewsAdmin)

