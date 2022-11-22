from django.shortcuts import render
from rest_framework import generics
from .models import Post,Employee,Organization,Department,Base,Channel
from .serializers import PostSerializer,OrganizaionSerializer,EmployeeSerializer,BaseSerializer,ChannelSerializer
from rest_framework.response import Response
from rest_framework import viewsets

#パーミッション設定
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class OrganizaionList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        user_obj = self.request.user
        queryset = user_obj.organization
        serializer_context = {}
        serializer_context["organization_obj"] = OrganizaionSerializer(queryset).data
        permission_classes = [IsAuthenticated]
        return Response(serializer_context)