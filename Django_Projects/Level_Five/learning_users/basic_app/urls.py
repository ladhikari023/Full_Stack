from django.urls import path
from basic_app import views


app_name = 'basic_app'

urlpatterns = [
    path('user_login/',views.user_login,name='user_login'),
    path('registration/',views.registration,name='register'),
    path('cbv/', views.CBView.as_view(), name='cbv')
]
