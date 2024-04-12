from django.shortcuts import render, redirect
from .models import Puppy
from .models import Testimonial
from .forms import TestimonialForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def puppies_index(request):
    puppies = Puppy.objects.all() 
    return render(request, 'puppies/index.html', 
    { 
        'puppies': puppies 
    }
)
    
def puppies_detail(request, puppy_id):
  puppy = Puppy.objects.get(id=puppy_id)
  return render(request, 'puppies/detail.html', { 'puppy': puppy })

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})

def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'submit_testimonial.html', {'form': form})