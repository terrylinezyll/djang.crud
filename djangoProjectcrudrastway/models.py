from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=30,blank=False,null=False)
    email=models.EmailField()
    age=models.IntegerField()
    phone=models.IntegerField(null=True)
    gender=models.CharField(max_length=30,blank=False,null=False)

def __str__(self):
    return self.name