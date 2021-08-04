#from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

#User = get_user_model()

class Folder(models.Model):
    name = models.CharField(max_length=200)
#    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
class Sets(models.Model):
    name = models.CharField(max_length=200)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE,
            related_name='folder_owned_sets', null=True)
    words = ArrayField(models.JSONField(default=dict), blank=True,
            default=list)

    def __str__(self):
        return self.name

"""
class Word(models.Model):
    text = models.CharField(max_length=50)
#    phonetics = JSONField(blank=True, null=True)
    meaning = models.TextField()
    sets = models.ForeignKey(Sets, on_delete=models.CASCADE,
            related_name='set_owned_words', null=True)

#    examples = JSONField(blank=True, null=True)

    def __str__(self):
        return self.text
class Post(models.Model):
#    phonetics = JSONField(blank=True, null=True)
    name = models.CharField(max_length=200)
    tags = ArrayField(models.JSONField(default=dict), blank=True)

    def __str__(self):
        return self.name
"""
