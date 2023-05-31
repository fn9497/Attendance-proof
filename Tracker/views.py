from django.shortcuts import render
from rest_framework import viewsets

from Collage.serializers import StudentSerializer
from .models import *
from .serializers import *

# Create your views here.




class LecturViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LecturSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    