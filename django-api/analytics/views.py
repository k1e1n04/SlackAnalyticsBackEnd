from django.shortcuts import render
from rest_framework import generics
from .models import Post,Employee,Organization,Department,Base,Channel
from .serializers import PostSerializer,OrganizationSerializer,EmployeeSerializer,BaseSerializer,ChannelSerializer
from rest_framework.response import Response
from rest_framework import viewsets

#パーミッション設定
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
class OrganizaionList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, *args, **kwargs):
        user_obj = self.request.user
        queryset = user_obj.organization
        # queryset = Organization.objects.all
        serializer_context = {}
        serializer_context["organization_obj"] = OrganizationSerializer(queryset).data
        return Response(serializer_context)

class BaseList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        user_obj = self.request.user
        user_organization = user_obj.organization
        queryset = Base.objects.filter(organization=user_organization)
        serializer_context = {}
        serializer_context["base_obj"] = BaseSerializer(queryset,many=True).data
        return Response(serializer_context)