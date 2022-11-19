from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Post,Employee,Organization,Department,Base,Channel
from .serializers import PostSerializer,OrganizaionSerializer,EmployeeSerializer,BaseSerializer,ChannelSerializer
from rest_framework.response import Response

# Create your views here.
class OrganizaionList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        user_obj = self.request.user
        queryset = user_obj.organization
        serializer_context = {}
        serializer_context["organization_obj"] = OrganizaionSerializer(queryset).data
        return Response(serializer_context)
    # queryset = Organization.objects.all()
    # serializer_class = OrganizaionSerializer