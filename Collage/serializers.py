from rest_framework import serializers

from Tracker.models import Attendance
from .models import * 
from Core.serializer import UserSerializer
from Tracker.serializers import LecturSerializer

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
    attendance_rate = serializers.SerializerMethodField()
    class Meta:
        model = CourseInstance
        fields = ['semester', 'course', 'teacher', 'department', 'semester', 'year', 'attendance_rate']

    def get_attendance_rate(self, obj):
        total_lectures = obj.lecture_set.count()
        total_attendance = Attendance.objects.filter(lecture__course_instance_id=obj.id, attend=1).count()
        total_attendance = min(total_attendance, total_lectures)  # Limit attendance to total lectures count
        if total_lectures > 0:
            attendance_rate = (total_attendance / total_lectures) * 100
            return attendance_rate
        return 0

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
