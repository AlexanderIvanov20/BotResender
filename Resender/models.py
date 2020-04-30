from django.db import models


class MessageGroup(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='photos')
    text = models.CharField(max_length=20000, blank=True)
    message_id = models.IntegerField()


class MessageChannel(models.Model):
    text = models.CharField(max_length=20000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    message_id = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='photos')
    url = models.URLField(blank=True)
