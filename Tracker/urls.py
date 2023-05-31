from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register('lectures', LecturViewSet)
router.register('attendances', AttendanceViewSet)



urlpatterns = [
    path('', include(router.urls)),
]