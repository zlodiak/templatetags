# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flash',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, to='cms.CMSPlugin', primary_key=True)),
                ('file', models.FileField(help_text='use swf file', upload_to=cms.models.pluginmodel.get_plugin_media_path, verbose_name='file')),
                ('width', models.CharField(verbose_name='width', max_length=6)),
                ('height', models.CharField(verbose_name='height', max_length=6)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
