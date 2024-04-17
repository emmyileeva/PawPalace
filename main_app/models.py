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
    newsletters = models.ManyToManyField('Newsletter')
    
    def __str__(self):
        return self.email
    
class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    subscribers = models.ManyToManyField('Subscriber', related_name='subscribed_newsletters')

    def __str__(self):
        return self.title
    
class Adoption(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name