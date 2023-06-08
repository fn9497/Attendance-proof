from rest_framework import serializers
from .models import *
from Collage.models import *
from django.contrib.auth.models import User
from rest_framework.relations import StringRelatedField

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','user', 'first_name', 'last_name']

    user = StringRelatedField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')



class LecturSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'


    
class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    total_attendance = serializers.SerializerMethodField()
    class Meta:
        model = Attendance
        fields = ['id','student','lecture','attend','total_attendance']

    def get_total_attendance(self, obj):
        student = obj.student
        attend = obj.attend
       # week=Lecture.week
        attendance_count = Attendance.objects.filter(student=student, attend=attend).count()
       # absent_percintage=100-(((attendance_count)/week)*100)
        return attendance_count
