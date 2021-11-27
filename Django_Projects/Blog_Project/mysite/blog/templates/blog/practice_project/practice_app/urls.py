from django.urls import path
from practice_app import views


urlpatterns = [
    path('',views.users,name='users')
]
