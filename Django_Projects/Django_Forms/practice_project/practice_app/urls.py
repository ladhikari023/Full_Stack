from django.urls import path
from practice_app import views


urlpatterns = [
    path('',views.signup,name='signup')
]
