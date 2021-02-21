""" NBA models."""

from django.db import models

class nbaPlayer(models.Model):

    name = models.CharField(max_length=255)
    team = models.CharField(max_length=150)
    
    number = models.PositiveSmallIntegerField()
    position = models.CharField(max_length=3)
    
    age = models.PositiveSmallIntegerField()
    date = models.DateTimeField()

    weight =  models.PositiveSmallIntegerField()
    college = models.CharField(max_length=150, null=True, blank=True)
    salary = models.DecimalField(max_digits=8, decimal_places=0, null=True, blank=True)


    def __str__(self):
        return self.name

