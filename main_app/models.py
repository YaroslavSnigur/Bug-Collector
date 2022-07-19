from django.db import models

class Bug(models.Model):
    name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lifespan = models.TextField(max_length=250)

    def __str__(self):
        return self.name
