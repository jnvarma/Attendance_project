from django.db import models





# Create your models here.




class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    #is_present = models.BooleanField()
    # Add more fields as per your requirements
    
    def __str__(self):
        return self.name

class Login(models.Model):
    username = models.CharField(max_length=100,default="default_username")
    password = models.CharField(max_length=100)
   # # Add more fields as per your requirements
    
    
    def __str__(self):
        return self.name
    
    
class Attendance(models.Model):
    SelectClass = models.CharField(max_length=20,default="default_RollNumber")
    RollNumber = models.CharField(max_length=50,default="default_RollNumber")
    StudentName = models.CharField(max_length=100,default="default_StudentName")
    DateTime = models.CharField(max_length=50,default="default_DateTime")
    Attendance = models.CharField(max_length=10,default="default_Attendance")
    
    
    def __str__(self):
        return "Attendance - Select Class :{self.SelectClass}, Roll Number: {self.RollNumber}, Student Name: {self.StudentName},Date Time: {self.DateTime}, Attendance: {self.Attendance}"