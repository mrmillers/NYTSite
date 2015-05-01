from django.db import models

# Create your models here.


class News(models.Model):
    nid = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=128, default="")
    location = models.CharField(max_length=256, default="")
    news_date = models.DateField()
    title = models.CharField(max_length=128, default="")
    text = models.TextField()


class Location(models.Model):
    nid = models.ForeignKey('News', db_index=False, related_name='geo_info')
    location = models.CharField(max_length=128)
    type = models.IntegerField(default=0)


class People(models.Model):
    nid = models.ForeignKey('News', db_index=False, related_name='compose')
    name = models.CharField(max_length=128)
    type = models.IntegerField(default=0)


class NewsDate(models.Model):
    nid = models.ForeignKey('News', db_index=False, related_name='on_date')
    news_date = models.DateField()
    type = models.IntegerField(default=0)
