# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Slider.avatar'
        db.delete_column(u'app_slider_slider', 'avatar')

        # Adding field 'Slider.slide'
        db.add_column(u'app_slider_slider', 'slide',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Slider.avatar'
        db.add_column(u'app_slider_slider', 'avatar',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Slider.slide'
        db.delete_column(u'app_slider_slider', 'slide')


    models = {
        u'app_slider.slider': {
            'Meta': {'object_name': 'Slider'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slide': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'})
        }
    }

    complete_apps = ['app_slider']