from django.urls import path
# from resumes.views import create_resume
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('create/', create_resume, name='create_resume'),
    path('create/', views.create_resume, name='create_resume'),
]
