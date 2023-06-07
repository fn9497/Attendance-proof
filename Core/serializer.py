from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from Collage.serializers import StudentSerializer


class AdminUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','password','email','first_name','last_name','gender','national_id','role'] 

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','password','email','first_name','last_name','gender','national_id','role'] 

class UserSerializer(serializers.ModelSerializer):
    student=StudentSerializer()
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','gender','national_id','role','student']
        read_only_fields = ['username','role']
