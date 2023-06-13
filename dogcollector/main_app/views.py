from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Dog


# Create your views here.

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  # We pass data to a template very much like we did in Express!
  return render(request, 'dogs/index.html', {
    'dogs': dogs
  })

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  return render(request, 'dogs/detail.html', { 'dog': dog })

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'