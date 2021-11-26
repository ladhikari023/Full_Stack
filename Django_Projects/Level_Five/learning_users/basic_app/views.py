from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
from . import models


#For login and logout helpers
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse

# For view class
from django.views.generic import (View,TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)

def index(request):
    return render(request,'basic_app/index.html')

class CBView(TemplateView):
    template_name = 'basic_app/cbv.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetaiView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name','principal','location')
    # Automatically searched for school_form.html school is lowercase of model name

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name','principal')
    # Automatically searched for school_form.html

class SchoolDeleteView(DeleteView):
    # context name covnention school
    model = models.School
    success_url = reverse_lazy("basic_app:school_list")
    # Expects school_confirm_delete.html for templates

def registration(request):

    registered = False

    if(request.method == "POST"):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{
            'registered':registered,
            'user_form':user_form,
            'profile_form':profile_form,
            })



def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Inactive")
        else:
            print("Authentication Failed!")
            return HttpResponse("Authentication Failed!")

    else:
        return render(request,'basic_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
