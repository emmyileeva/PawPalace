# main_app/forms.py
from django import forms
from .models import Testimonial, Subscriber, Adoption

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'message']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        
class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ['name', 'email', 'message'] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }