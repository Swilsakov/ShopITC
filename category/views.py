from django.shortcuts import render
from .serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication
from rest_framework.authentication import TokenAuthentication
from category.models import Category
from rest_framework import permissions


class CategoryListView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAdminUser]


class CategoryDetailView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]


class CategoryDeleteView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAdminUser]
    