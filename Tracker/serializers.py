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
        fields = '__all__'
        