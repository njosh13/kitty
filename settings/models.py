from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Setting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    app = models.CharField(max_length=30)
    configkey = models.CharField(max_length=50)
    configvalue = models.TextField()