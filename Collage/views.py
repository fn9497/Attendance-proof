from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
     queryset=Course.objects.all()
     serializer_class = StudentCourseSerializer

     def get_queryset(self):
        student_id = self.request.user.id
        student_course_vs = StudentCourseViewSet(student_id)
        courses = student_course_vs.get_courses()
        return courses


class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
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


class departmentViewSet(viewsets.ModelViewSet):
    queryset = department.objects.all()
    serializer_class = departmentSerializer
    
