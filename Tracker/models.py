from django.db import models
from requests import Response
from Collage.models import *
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField




class Lecture(models.Model):
   
    course_instance = models.ForeignKey(CourseInstance, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    week = models.IntegerField(default=1)
    picture_1 = models.ImageField(upload_to=("images/"),null=True)
    picture_2 = models.ImageField(upload_to=("images/"),null=True)
    picture_3 = models.ImageField(upload_to=("images/"),null=True)
    attend = models.CharField(models.CharField(max_length=100))
    absent = models.CharField(models.CharField(max_length=100))
   # attend = ArrayField(models.CharField(max_length=100))
    # = ArrayField(models.CharField(max_length=100))

    def validate_field_value(value):
        int("max_value")
        max_value = 13
        if value > max_value:
            raise ValidationError("Weeks number cannot exceed {max_value}.")
    
    def __str__(self):
        return self.course_instance.course.name + " " + str(self.date) + " " + str(self.time)
   
    def attend(self,request):
        Attend = Student.objects.filter(Attendance.objects.attend == 1)
        serializer = self.get_serializer(Attend, many=True)
        return Response(serializer.data)
    

    def absent(self,request):
        Absent = Student.objects.filter(Attendance.objects.attend == 0)
        serializer = self.get_serializer(Absent, many=True)
        return Response(serializer.data)
    

class Attendance(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attend = models.IntegerField(default=0)
    count_attend= models.IntegerField(default=0)
    count_absent= models.IntegerField(default=0)
   
    def __str__(self):
        return self.student.user.first_name + str("'s attendance")
    
    def absent_n(self):
        self.count_absent = self.lecture.week - Attendance.objects.filter(attend=self.attend).count()
    

    def attend_n(self):
        self.count_attend = Attendance.objects.filter(attend=1).count()   
