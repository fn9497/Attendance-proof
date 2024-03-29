from django.shortcuts import render
from rest_framework import viewsets

from Collage.serializers import StudentSerializer
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.




class LecturViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LecturSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['attend','lecture','student','lecture__course_instance']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Attendance.objects.create(lecture=serializer.validated_data['lecture'],student=serializer.validated_data['student'],attend=serializer.validated_data['attend'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
