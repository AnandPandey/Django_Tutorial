from django.urls import path
from . import views
#localhost:8000/project1
#localhost:8000/project1/order
urlpatterns = [
    path('', views.all_project, name='all_project'),
    
]
