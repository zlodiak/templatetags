# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.title'
        db.add_column(u'app_news_news', 'title',
                      self.gf('django.db.models.fields.TextField')(default='---', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.title'
        db.delete_column(u'app_news_news', 'title')


    models = {
        u'app_news.news': {
            'Meta': {'object_name': 'News'},
            'date_create': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_event': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '50000'}),
            'title': ('django.db.models.fields.TextField', [], {'default': "'---'", 'max_length': '100'})
        }
    }

    complete_apps = ['app_news']