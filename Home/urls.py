from django.contrib import admin
from django.urls import path,include
from Home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('About',views.About, name='about'),
    path('Education',views.Education, name='education'),
    path('Experience',views.Experience,name="experience"),
    path('Projects', views.Projects, name='projects'),
    path('Contact',views.contactt, name="contact")
]