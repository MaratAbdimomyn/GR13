from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    engine = models.CharField(max_length=40)

    def __str__(self):
        return self.name