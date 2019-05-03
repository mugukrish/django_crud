from django.db import models

# Create your models here.
class Feeds(models.Model):
    id = models.AutoField(primary_key=True)
    feed = models.CharField(max_length=300)
