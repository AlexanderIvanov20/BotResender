from django.db import models


class Message(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='photos')
    text = models.CharField(max_length=2000, blank=True)
