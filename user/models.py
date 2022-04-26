from distutils.text_file import TextFile
from django.db import models

# Create your models here.
class userDetail(models.Model):
    userID = models.CharField(max_length=4)
    userName = models.TextField()