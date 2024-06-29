from django.urls import path
# from app import views
# from .views import home 
from .views import home1 
from .views import register
from .views import registerdata
urlpatterns = [
    #  path('home/', views.home),
     path('registration/',register),
     path('home1/',home1),
     path('register/',register, name='register'),
     path('registerdata/', registerdata, name='register')

    # path('hame',home)
]
