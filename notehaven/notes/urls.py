from django.urls import path
from . import views

urlpatterns = [
    path('landing', views.landing, name='landing_page'),  # Landing page
]