from rest_framework import serializers
from .models import *
from Collage.models import *
from django.contrib.auth.models import User
from rest_framework.relations import StringRelatedField

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','user', 'first_name', 'last_name','department']

    user = StringRelatedField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    department = serializers.CharField()

class LecturSerializer(serializers.ModelSerializer):
    #date = serializers.DateField(required=False)
    #time = serializers.TimeField(required=False)
    class Meta:
        model = Lecture
        fields = '__all__'


    
class AttendanceSerializer(serializers.ModelSerializer):
    lecture_week = serializers.SerializerMethodField()
    student = StudentSerializer()
    total_attendance = serializers.SerializerMethodField()
    attendance_percentage = serializers.SerializerMethodField()
    absent_percentage = serializers.SerializerMethodField()
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'lecture', 'attend', 'total_attendance', 'attendance_percentage', 'absent_percentage','lecture_week']

    def get_total_attendance(self, obj):
        student = obj.student
        attend = obj.attend
        lecture_count = Lecture.objects.filter(course_instance=obj.lecture.course_instance).count()
        attendance_count = Attendance.objects.filter(student=student, attend=attend).count()
        return attendance_count
    
    def get_attendance_percentage(self, obj):
        student = obj.student
        lecture_count = Lecture.objects.filter(course_instance=obj.lecture.course_instance).count()
        attendance_count = Attendance.objects.filter(student=student, attend=1).count()
        if lecture_count > 0:
            percentage = (attendance_count / lecture_count) * 100
            return percentage
        return 0

    def get_absent_percentage(self, obj):
        student = obj.student
        lecture_count = Lecture.objects.filter(course_instance=obj.lecture.course_instance).count()
        absence_count = Attendance.objects.filter(student=student, attend=0).count()
        if lecture_count > 0:
            percentage = (absence_count / lecture_count) * 100
            return percentage
        return 0
    
    def get_lecture_week(self, obj):
        return obj.lecture.week
    
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
