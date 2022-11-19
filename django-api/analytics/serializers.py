from rest_framework import serializers
from .models import Post,Organization,Base,Department,Employee,Channel


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('organization', 'base', 'channel', 'employee', 'created_at')

class OrganizaionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('id','name','created_at')

class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Base
        fields = ('name','created_at')

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('name','base','created_at')

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('name','base','department','created_at','updated_at')

class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = ('name','base','department','created_at')

