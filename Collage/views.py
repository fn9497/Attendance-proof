from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
     queryset=Course.objects.all()
     serializer_class = StudentCourseSerializer
   


class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['student__user__username']
    def get(self,request):
        student=Student.objects.get(id=self.student_id)
        return student.course.all()


    def get_serializer_class(self):
        if self.action == 'create':
            return CreateStudentCourseSerializer
        return StudentCourseSerializer
    

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['user']




class departmentViewSet(viewsets.ModelViewSet):
    queryset = department.objects.all()
    serializer_class = departmentSerializer
    
