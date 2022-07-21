from django.forms import ModelForm
from .models import Treatment

class TreatmentForm(ModelForm):
  class Meta:
    model = Treatment
    fields = ['date', 'procedure']