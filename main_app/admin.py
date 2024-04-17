from django.contrib import admin
from .models import Puppy, Testimonial, Subscriber, Newsletter


# Register your models here.
admin.site.register(Puppy)
admin.site.register(Testimonial)
admin.site.register(Subscriber)
admin.site.register(Newsletter)