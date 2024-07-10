from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializers
from rest_framework.views import APIView


class BlogPostlistCreate(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    lookup_field = "pk"

class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.querry_params.get("title", "")

        if title:
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            blog_posts = BlogPost.objects.all()

        serializers = BlogPostSerializers(blog_posts, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

# Create your views here.
