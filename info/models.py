from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    repository = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.date(2021,3,3))
    end_date = models.DateField(default=datetime.date(2021,3,3))
    image = models.ImageField(upload_to='images/')
    done_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="list_project")

    def __str__(self):
        return "Project Name: "+str(self.name)+" Link: "+str(self.repository)

class Award(models.Model):
    name = models.CharField(max_length=70)
    sponsor = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="list_award")

    def __str__(self):
        return str(self.name)+" awarded by "+str(self.sponsor)