from django.urls import path
# from app import views
# from .views import home 
from .views import register

urlpatterns = [
    #  path('home/', views.home),
     path('registration/',register)
    # path('hame',home)
]
