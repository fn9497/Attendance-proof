from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)
router.register('studentcourses', StudentCourseViewSet)
router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)
router.register('departments', departmentViewSet)
    

urlpatterns = [
    path('', include(router.urls)),
]
