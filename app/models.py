from django.db import models

# Create your models here.
class employedetails(models.Model):
     name = models.CharField(max_length=255)
     email = models.EmailField(max_length=255)
     created_on = models.DateTimeField(auto_now_add = True, auto_now = False)
