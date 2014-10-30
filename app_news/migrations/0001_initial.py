# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'app_news_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('teaser', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=50000)),
            ('date_create', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_event', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'app_news', ['News'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'app_news_news')


    models = {
        u'app_news.news': {
            'Image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'News'},
            'date_create': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_event': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '50000'})
        }
    }

    complete_apps = ['app_news']