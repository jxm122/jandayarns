from turtle import title
from xml.parsers.expat import model
from django.db import models

# Create your models here.
class Blog (models.Model):
    title=models.CharField(max_length=250)
    text=models.TextField()
    data=models.DateTimeField()
 

    def str(self):
        return self.title