from django.shortcuts import render
from django.contrib.auth.mixings import LoginRequiredMixin
from django.urls import reverse_lazy


from django.views import generic
from django.http import Http404

from braces.views import SelectRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


class PostList(SelectRelatedMixin,generic.ListView):
    model = models.POST
    select_related = ('user','group')

class UserPosts(generic.ListView):
    model = models.POST
    template_name = 'posts/user_post_list.html'


    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.POST
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        reutrn queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):

    fields = ('message','group')
    model = models.POST

    def form_valid(self):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        reutrn super().form_valid(form)


class DeltePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):

    model = models.POST
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        reutrn super().delete(*args,**kwargs)
