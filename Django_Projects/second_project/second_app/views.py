from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    my_dict2 = {'insert_second':"I am coming from views.py"}
    return render(request,'second_app/index.html',context=my_dict2)

def home(request):
    my_dict2 = {'insert_second2':"I am coming from views.py Second"}
    return render(request,'second_app/index.html',context=my_dict2)
