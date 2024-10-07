from django.db import models

# Create your models here.


class product(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField()
    cost = models.IntegerField()
    dot = models.DateTimeField(auto_now=True)
    pct = models.ImageField(upload_to="myapp/static/img", blank=True)


def __str__(self):
    return self.name


class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)

    def speak(self, a, b):
        return a+b
