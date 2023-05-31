from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


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
        fields = '__all__'


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