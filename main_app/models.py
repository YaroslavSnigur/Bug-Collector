from django.db import models
from django.urls import reverse

class Bug(models.Model):
    name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lifespan = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bug_id': self.id})
