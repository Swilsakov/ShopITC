from django.shortcuts import render
from .serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication
from rest_framework.authentication import TokenAuthentication
from category.models import Category
from rest_framework import permissions


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
