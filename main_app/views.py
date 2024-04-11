from django.shortcuts import render

puppies = [
    {'name': 'Buddy', 'breed': 'Golden Retriever'},
    {'name': 'Daisy', 'breed': 'Poodle'},
    {'name': 'Rex', 'breed': 'German Shepherd'}
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