from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FolderSerializer, SetsSerializer
from .models import Folder, Sets

class FolderView(viewsets.ModelViewSet):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()

class SetsView(viewsets.ModelViewSet):
    serializer_class = SetsSerializer
    queryset = Sets.objects.all()

"""
class WordView(viewsets.ModelViewSet):
    serializer_class = WordSerializer
    queryset = Word.objects.all()
class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
"""
