from django.urls import path
from . import views

# Assigning a view called post_list to the root URL
urlpatterns = [
    path('', views.post_list, name='post_list'),
]