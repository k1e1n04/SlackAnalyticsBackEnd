from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets

#パーミッション設定
from rest_framework.permissions import IsAuthenticated

class CurrentUser(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        queryset = self.request.user
        serializer_context = {}
        serializer_context["user_obj"] = UserSerializer(queryset).data
        return Response(serializer_context)