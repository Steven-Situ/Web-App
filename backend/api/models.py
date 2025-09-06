from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    Content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")


def _str_(self):
        return self.title