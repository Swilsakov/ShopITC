from django.urls import path
from .views import *

urlpatterns = [
    path('category/list', CategoryListView.as_view()),
    path('category/create', CategoryCreateView.as_view()),
    path('category/detail', CategoryDetailView.as_view()),
    path('category/delete', CategoryDeleteView.as_view())
]