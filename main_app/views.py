from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bug, Agent, Photo
from .forms import TreatmentForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'collectorforme'

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

def add_photo(request, bug_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, bug_id=bug_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', bug_id=bug_id)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bugs_index(request):
  bugs = Bug.objects.all()
  return render(request, 'bugs/index.html', { 'bugs': bugs })

def bugs_detail(request, bug_id):
  bug = Bug.objects.get(id=bug_id)
  agents_bug_doesnt_have = Agent.objects.exclude(id__in = bug.agents.all().values_list('id'))
  treatment_form = TreatmentForm()
  return render(request, 'bugs/detail.html', {
    'bug': bug, 'treatment_form': treatment_form,
    'agents': agents_bug_doesnt_have
  })

def add_treatment(request, bug_id):
  form = TreatmentForm(request.POST)
  if form.is_valid():
    new_treatment = form.save(commit=False)
    new_treatment.bug_id = bug_id
    new_treatment.save()
  return redirect('detail', bug_id=bug_id)

def assoc_agent(request, bug_id, agent_id):
  Bug.objects.get(id=bug_id).agents.add(agent_id)
  return redirect('detail', bug_id=bug_id)

class BugCreate(CreateView):
  model = Bug
  fields = '__all__'

class BugUpdate(UpdateView):
  model = Bug
  fields = ['latin_name', 'description', 'lifespan']

class BugDelete(DeleteView):
  model = Bug
  success_url = '/bugs/'