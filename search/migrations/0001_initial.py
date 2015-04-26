# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=128)),
                ('type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('nid', models.IntegerField(serialize=False, primary_key=True)),
                ('author', models.CharField(default=b'', max_length=128)),
                ('location', models.CharField(default=b'', max_length=256)),
                ('news_date', models.DateField()),
                ('title', models.CharField(default=b'', max_length=128)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_date', models.DateField()),
                ('type', models.IntegerField(default=0)),
                ('nid', models.ForeignKey(related_name='on_date', to='search.News', db_index=False)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('type', models.IntegerField(default=0)),
                ('nid', models.ForeignKey(related_name='compose', to='search.News', db_index=False)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='nid',
            field=models.ForeignKey(related_name='geo_info', to='search.News', db_index=False),
        ),
    ]
