from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

PROCEDURES = (
    ('E', 'Extermination'),
    ('F', 'Feeding'),
    ('R', 'Reproduction')
)

class Agent(models.Model):
  name = models.CharField(max_length=50)
  usage = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('agents_detail', kwargs={'pk': self.id})

class Bug(models.Model):
    name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lifespan = models.TextField(max_length=250)
    agents = models.ManyToManyField(Agent)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bug_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for bug_id: {self.bug_id} @{self.url}"

class Treatment(models.Model):
    date = models.DateField()
    procedure = models.CharField(
        max_length=1,
        choices=PROCEDURES,
        default=PROCEDURES[0][0]
    )

    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_procedure_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']