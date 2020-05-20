from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length= 30 , blank=True)
    email  = models.CharField(max_length= 30 , blank=True)
    dob = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
