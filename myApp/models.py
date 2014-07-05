__author__ = 'Hugh'

from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class House(models.Model):
    address = models.CharField(max_length=200)
    owner = models.OneToOneField(Owner, primary_key=True)
    # owners = models.ManyToManyField(Owner)

    def __unicode__(self):
        return self.address


