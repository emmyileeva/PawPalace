from django.urls import path
from . import views
 
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('puppies/', views.puppies_index, name='index'),
    path('puppies/<int:puppy_id>/', views.puppies_detail, name='detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('submit-testimonial/', views.submit_testimonial, name='submit_testimonials'),
    path('testimonials/<int:testimonial_id>/', views.testimonial_detail, name='testimonial_detail'),
    path('testimonials/<int:pk>/update/', views.TestimonialUpdateView.as_view(), name='update_testimonial'),
    path('testimonials/<int:pk>/delete/', views.TestimonialDeleteView.as_view(), name='delete_testimonial'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('tips/', views.tips_view, name='tips')
 ]