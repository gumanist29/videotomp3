from django.db import models

# Create your models here
class Utuber(models.Model):
    name=models.CharField(max_length=130)

    def __str__(self):
        return self.name


