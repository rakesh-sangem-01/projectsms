from django.db import models
from holoviews import render


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.contrib.auth.models import User
class StudentList(models.Model):
    Register_Number = models.CharField(max_length=10,unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Register_Number

# def student_list(request):
#     students = StudentList.objects.all()
#     return render(request,'adminapp/student_list.html',{'students':students})

from django.db import models


class feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=10)
    textfield = models.TextField(max_length=150)

    def str(self):
        return self.name

