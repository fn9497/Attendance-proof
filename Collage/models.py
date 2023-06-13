from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class department(models.Model):
    name = models.CharField(max_length=100)
    head_of_department = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    



class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    level = models.IntegerField()
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    #encode=ArrayField(models.CharField(max_length=100))
    
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    def __str__(self):
        return self.user.username




class Course(models.Model):
    name = models.CharField(max_length=100)
    credit_hours = models.IntegerField()
    Teachering_hours = models.IntegerField()
    code = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.code + " " + self.name
    

class CourseInstance(models.Model):
    semesters = [
        ('Fall', 'Fall'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Winter', 'Winter')
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100, choices=semesters)
    year = models.IntegerField()

    def __str__(self):
        return  self.course.name
    
class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_instance = models.ForeignKey(CourseInstance, on_delete=models.CASCADE)
    def __str__(self):
        return  self.course.name + " " + str(self.student.user) + " " + str(self.course_instance.teacher.user) + " " + self.student.department.name
