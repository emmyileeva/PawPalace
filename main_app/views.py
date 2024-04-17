from django.shortcuts import render, redirect
from .models import Puppy, Testimonial, Newsletter, Subscriber
from .forms import TestimonialForm, SubscriberForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
import random


# Create your views here.
def home(request):
    form = SubscriberForm()
    return render(request, 'home.html', {'form': form})

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
  testimonials = Testimonial.objects.all()
  random_testimonial = random.choice(testimonials)
  return render(request, 'puppies/detail.html', { 'puppy': puppy, 'random_testimonial': random_testimonial })

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials/testimonials.html', {'testimonials': testimonials})

def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm()
        testimonials = Testimonial.objects.all()
        return render(request, 'testimonials/submit_testimonials.html', {'form': form, 'testimonials': testimonials})

def testimonial_detail(request, testimonial_id):
    testimonial = Testimonial.objects.get(id=testimonial_id)
    return render(request, 'testimonials/detail.html', {'testimonial': testimonial})

class TestimonialUpdateView(UpdateView):
    model = Testimonial
    fields = ['name', 'message']
    template_name = 'testimonials/update_testimonial.html' 
    success_url = reverse_lazy('testimonials') 

class TestimonialDeleteView(DeleteView):
    model = Testimonial
    template_name = 'testimonials/delete_testimonial.html'
    success_url = reverse_lazy('testimonials')
    
def subscribe(request):
    newsletters = Newsletter.objects.all()  
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            selected_newsletters = Newsletter.objects.filter(pk__in=request.POST.getlist('newsletters'))
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            subscriber.newsletters.add(*selected_newsletters)
            messages.success(request, 'Thank you for subscribing!')
            return redirect('/')  
    else:
        form = SubscriberForm()
        
    return render(request, 'subscribe.html', {'form': form, 'newsletters': newsletters})

    
def tips_view(request):
    return render(request, 'tips.html')

