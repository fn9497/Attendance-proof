from rest_framework import serializers
from .models import *
from Core.serializer import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    user=UserSerializer()  
    class Meta:
        model = Teacher
        fields = ['id','user']


class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInstance
        fields = ['semester','course','teacher','department','semester','year']


class StudentCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    course_instance = CourseInstanceSerializer()
    class Meta:
        model = StudentCourse
        fields = ['course', 'course_instance']



class CreateStudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'
