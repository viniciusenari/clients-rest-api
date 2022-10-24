from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, )
    ssn = models.CharField(max_length=9, unique=True)
    phone = models.CharField(max_length=15)
    active = models.BooleanField()

    def __str__(self):
        return self.name
