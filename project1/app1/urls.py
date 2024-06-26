from django.urls import path
from app1 import views
# from .views import home 

urlpatterns = [
     path('home/', views.home),
     
    # path('hame',home)
]