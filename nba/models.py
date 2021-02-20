""" NBA models."""

from django.db import models

class nbaPlayer(models.models):

    name = models.CharFIeld(max_length=255)
    team = models.CharFIeld(max_length=150)
    
    number = models.PositiveSmallIntegerField()
    position = models.CharFIeld(max_length=3)
    
    age = models.PositiveSmallIntegerField()
    date = models.DateField

    weight =  models.PositiveSmallIntegerField()
    college = models.CharFIeld(max_length=150, null=True, blank=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
        return self.name

