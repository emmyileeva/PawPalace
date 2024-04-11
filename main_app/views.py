from django.shortcuts import render

puppies = [
    {'name': 'Buddy', 'breed': 'Golden Retriever', 'description': 'A friendly and loyal companion.', 'age': 0.50},
    {'name': 'Lucy', 'breed': 'Bulldog', 'description': 'A happy puppy with lots of energy.', 'age': 0.33},
    {'name': 'Daisy', 'breed': 'Poodle', 'description': 'A smart and friendly puppy.', 'age': 0.25},
    {'name': 'Rex', 'breed': 'German Shepherd', 'description': 'A strong and protective puppy.', 'age': 0.75},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def puppies_index(request):
    return render(request, 'puppies/index.html', {
        'puppies': puppies
    })