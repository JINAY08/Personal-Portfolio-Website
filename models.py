from django.db import models

# Create your models here.

class BookReview(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'gallery')
    link = models.URLField(null=True)

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    technology = models.CharField(max_length= 100)
    image = models.ImageField(upload_to = 'gallery' ,blank = "True")
    link = models.URLField(null=True,blank="True")

