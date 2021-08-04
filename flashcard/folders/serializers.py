from rest_framework import serializers
from .models import Folder,Sets

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ('id', 'name', 'folder_owned_sets')

class SetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sets
        fields = ('id', 'name','folder', 'words')

"""
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'text', 'meaning', 'sets')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'name', 'tags')
"""
