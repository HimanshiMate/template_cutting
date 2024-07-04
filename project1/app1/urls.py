from django.urls import path
from app1 import views
# from .views import home 
from .views import home

urlpatterns = [
    #  path('home/', views.home),
    # path('',views.home, name="home")
    path("home/",views.home,name='home')
     
    # path('hame',home)
]