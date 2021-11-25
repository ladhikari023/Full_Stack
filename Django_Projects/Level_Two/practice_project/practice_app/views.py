from django.shortcuts import render
from django.http import HttpResponse
from practice_app.models import User

# Create your views here.

def index(request):
    my_dict = {'insert_me':"I am inseted here"}
    return render(request,"practice_app/index.html",context=my_dict)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'practice_app/users.html',context=user_dict)
