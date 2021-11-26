from django.contrib import admin
from basic_app.models import UserProfileInfo, School, Students

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(School)
admin.site.register(Students)
