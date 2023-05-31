from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(department)
admin.site.register(Course)
admin.site.register(CourseInstance)
admin.site.register(StudentCourse)
