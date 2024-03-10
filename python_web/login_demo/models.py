from django.db import models

class Users(models.Model):
    
    username = models.CharField(max_length = 666)
    password = models.CharField(max_length= 666)
    mobile = models.CharField(max_length = 666)
    gender = models.CharField(max_length = 8)
    registerTime = models.DateTimeField(auto_now_add = True)
