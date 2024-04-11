from django.shortcuts import render

puppies = [
    {'name': 'Buddy', 'breed': 'Golden Retriever', 'description': 'A friendly and loyal companion.', 'age_in_months': 6},
    {'name': 'Lucy', 'breed': 'Bulldog', 'description': 'A happy puppy with lots of energy.', 'age_in_months': 8},
    {'name': 'Daisy', 'breed': 'Poodle', 'description': 'A smart and friendly puppy.', 'age_in_months': 4},
    {'name': 'Rex', 'breed': 'German Shepherd', 'description': 'A strong and protective puppy.', 'age_in_months': 10},
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