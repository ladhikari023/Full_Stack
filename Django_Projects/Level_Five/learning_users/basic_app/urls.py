from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('user_login/',views.user_login,name='user_login'),
    path('registration/',views.registration,name='register'),
    path('cbv/', views.CBView.as_view(), name='cbv'),
    path('school/', views.SchoolListView.as_view(), name='school_list'),
    path("school/<int:pk>/",views.SchoolDetaiView.as_view(),name='detail'),
    path("create/",views.SchoolCreateView.as_view(),name='create'),
    path("school/update/<int:pk>/",views.SchoolUpdateView.as_view(),name='update'),
    path("school/delete/<int:pk>/",views.SchoolDeleteView.as_view(),name='delete'),
]
