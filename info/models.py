from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    repository = models.CharField(max_length=100)
    image = models.ImageField(upload_to='p_images')

    def __str__(self):
        return "Project Name: "+str(name)+" Link: "+str(repository)

class Award(models.Model):
    name = models.CharField(max_length=70)
    sponsor = models.CharField(max_length=100)
    description = models.CharField(max_length=400)

    def __str__(self):
        return str(name)+" awarded by "+str(sponsor)