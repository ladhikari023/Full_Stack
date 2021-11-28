from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from plan_app.models import Plan,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from plan_app.forms import PlanForm,CommentForm,UserForm
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,
                                    UpdateView,DeleteView)

# Create your views here.


class AboutView(TemplateView):
    template_name = 'plan_app/about.html'


class PlanListView(ListView):
    model = Plan

    def get_queryset(self):
        return Plan.objects.filter(published_date__lte=timezone.now(),
        published_date__isnull=False).order_by('-published_date')

class PlanDraftListView(LoginRequiredMixin,ListView):
    template_name = 'plan_app/plan_draft_list.html'
    login_url = '/login/'
    redirect_field_name = 'plan_app/plan_detail.html'
    model = Plan

    def get_queryset(self):
        return Plan.objects.filter(published_date__isnull=True).order_by('-created_date')


class PlanDetailView(DetailView):
    model = Plan


class PlanCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    # redirect_field_name = 'plan_app/plan_detail.html'
    form_class = PlanForm
    model = Plan

class PlanUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name = 'plan_app/plan_detail.html'
    form_class = PlanForm
    model = Plan

class PlanDeleteView(LoginRequiredMixin,DeleteView):
    model = Plan
    success_url = reverse_lazy('plan_list')


@login_required
def plan_publish(request,pk):
    plan = get_object_or_404(Plan,pk=pk)
    plan.publish()
    return redirect('plan_list')


def register_user(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'plan_app/registration.html',{
        'registered':registered,
        'user_form':user_form
    })


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('plan_list'))
            else:
                return HttpResponse("Account Inactive")
        else:
            return HttpResponse("Authentication Failed!")
    else:
        return render(request,'registration/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('plan_list'))
