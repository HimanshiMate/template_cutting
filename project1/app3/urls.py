from django.urls import path
from app3 import views
# from .views import home 

urlpatterns = [
     path('home/', views.home),
     
    # path('hame',home)
]