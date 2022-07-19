from django.shortcuts import render

from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Bug:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, latin_name, description, lifespan):
    self.name = name
    self.latin_name = latin_name
    self.description = description
    self.lifespan = lifespan

bugs = [
  Bug('Honey Bee', 'Apis mellifera', 'Bees are winged insects closely related to wasps and ants.', '30-60 days'),
  Bug('Ant', 'Formicidae', 'Ants form colonies that range in size', '4 years'),
  Bug('Mosquito', 'Culicidae', 'The word "mosquito" is Spanish and Portuguese for "little fly"', '42-56 days')
]

def home(request):
    return HttpResponse('<h1>Hello Bugs!</h1>')

def about(request):
    return render(request, 'about.html')

def bugs_index(request):
  return render(request, 'bugs/index.html', { 'bugs': bugs })
