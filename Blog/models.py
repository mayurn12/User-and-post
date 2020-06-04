from django.db import models                                                                                                                             
from django.contrib.auth.models import User

class Post(models.Model):
    username = models.ForeignKey(User,null=True,on_delete= models.CASCADE)
    text = models.TextField(max_length=2000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
