from rest_framework import serializers
from .models import *
#from Collage.serializers import StudentSerializer




class LecturSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'
       
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['lecture' ,'student','attend']
        read_only_fields = ['count_attend','count_absent']
        
