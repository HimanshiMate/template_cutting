from django.db import models

# Create your models here.
#object relational mapper- responsible for convert the code into query
# query generate on the app
#python code convert into query -->make migrate
#migrate is used to create table
class Student(models.Model):
    Name= models.CharField(max_length=50)
    Password=models.EmailField()
    Contact=models.IntegerField()