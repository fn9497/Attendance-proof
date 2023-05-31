from django.contrib import admin
from .models import *
# Register your models here.

#class LectureAdmin(admin.ModelAdmin):
    #readonly_fields = ('week',)
class AttendanceAdmin(admin.ModelAdmin):
    readonly_fields = ('count_attend','count_absent',)
admin.site.register(Lecture)
admin.site.register(Attendance,AttendanceAdmin)
