from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional fiels

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


# For cbv practice
class School(models.Model):

    name = models.CharField(max_length = 256)
    principal = models.CharField(max_length = 100)
    location = models.CharField(max_length = 256)

    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    School = models.ForeignKey(School,related_name='students',on_delete = models.CASCADE)

    def __str__(self):
        return self.name
