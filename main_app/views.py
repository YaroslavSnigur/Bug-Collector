from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bug

# class Bug:
#   def __init__(self, name, latin_name, description, lifespan):
#     self.name = name
#     self.latin_name = latin_name
#     self.description = description
#     self.lifespan = lifespan

# bugs = [
#   Bug('Honey Bee', 'Apis mellifera', 'Bees are winged insects closely related to wasps and ants.', '30-60 days'),
#   Bug('Ant', 'Formicidae', 'Ants form colonies that range in size', '4 years'),
#   Bug('Mosquito', 'Culicidae', 'The word "mosquito" is Spanish and Portuguese for "little fly"', '42-56 days')
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bugs_index(request):
  bugs = Bug.objects.all()
  return render(request, 'bugs/index.html', { 'bugs': bugs })

def bugs_detail(request, bug_id):
  bug = Bug.objects.get(id=bug_id)
  return render(request, 'bugs/detail.html', { 'bug': bug })

class BugCreate(CreateView):
  model = Bug
  fields = '__all__'

class BugUpdate(UpdateView):
  model = Bug
  fields = ['latin_name', 'description', 'lifespan']

class BugDelete(DeleteView):
  model = Bug
  success_url = '/bugs/'