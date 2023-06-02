from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from blog.serializers import BlogSerializer, CategorySerializer
from rest_framework import generics


# Create your views here.
class BlogList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
