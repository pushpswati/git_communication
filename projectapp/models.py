
from django.db import models

class Post(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      username = models.CharField(max_length=100, blank=True,default='')
      password = models.CharField(max_length=10, blank=True,default='')
      
      class Meta:
            ordering = ('created',)
