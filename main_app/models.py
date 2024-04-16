from django.db import models

# Create your models here.
class Puppy(models.Model):
    name = models.CharField(max_length=100)
    age_in_months = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email