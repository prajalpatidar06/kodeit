from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Blog(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    category = models.CharField(max_length=150)
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add = True , null=True)
    url = models.URLField(max_length = 500)

    def __str__(self):
        return self.title
