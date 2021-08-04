from django.contrib import admin
from .models import Folder, Sets

class FolderAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'words')

'''
class WordAdmin(admin.ModelAdmin):
    list_display = ('text', 'meaning', 'sets')

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'tags')
'''
# Register your models here.

admin.site.register(Folder, FolderAdmin)
admin.site.register(Sets, SetsAdmin)
'''
admin.site.register(Word, WordAdmin)
admin.site.register(Post, PostAdmin)
'''
