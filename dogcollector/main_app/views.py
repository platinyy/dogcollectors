from django.shortcuts import render

dogs = [
  {'name': 'Duke', 'breed': 'bulldog', 'description': 'well-muscled bruiser', 'age': 3},
  {'name': 'Bailey', 'breed': 'Shiba Inu', 'description': 'favorite coin', 'age': 2},
  {'name': 'Luna', 'breed': 'Bichon Frise', 'description': 'Sweetiest puppy', 'age': 0},
]

# Create your views here.

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'dogs/index.html', {
    'dogs': dogs
  })