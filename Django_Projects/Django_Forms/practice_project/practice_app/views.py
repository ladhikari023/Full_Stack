from django.shortcuts import render
from django.http import HttpResponse
from practice_app.models import User
from . import forms

# Create your views here.

def index(request):
    my_dict = {'insert_me':"Thank You!!"}
    return render(request,"practice_app/index.html",context=my_dict)

def signup(request):
    form = forms.AuthorForm

    if request.method == "POST":
        form = forms.AuthorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)


    return render(request,'practice_app/users.html',{'form':form})
