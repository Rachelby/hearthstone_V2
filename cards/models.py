from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

class Card(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)	
    active = models.BooleanField(default=True)
    owner = models.ManyToManyField('User', related_name='Card')

class Deck(models.Model):
	cards = models.ManyToManyField('Card', related_name = 'Deck')
	owner = models.ForeignKey('User', related_name='Deck', on_delete=models.CASCADE)

class Quantity(models.Model):
	Card = models.ForeignKey('Card', on_delete=models.CASCADE)
	Owner = models.ForeignKey('User', on_delete=models.CASCADE)
	Quantity = models.SmallIntegerField(1)
