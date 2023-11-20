from django.db import models

# Create your models here.


class cuisines(models.Model):
    cuisine = models.CharField(max_length=16)
    description = models.CharField(max_length=150, default='hi')
    bg = models.CharField(
        max_length=500, default='https://images.unsplash.com/photo-1603366615917-1fa6dad5c4fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80')


class dishes (models.Model):
    category = models.CharField(max_length=16)
    Name = models.CharField(max_length=150, default='hi')
    bg = models.CharField(
        max_length=500, default='https://images.unsplash.com/photo-1603366615917-1fa6dad5c4fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80')
