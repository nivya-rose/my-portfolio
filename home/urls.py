from django.urls import path
from . import views
from .views import contact_view  # Import the view
from .views import download_resume

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', contact_view, name='contact'),  
    path('download-resume/', download_resume, name='download_resume'),
]
