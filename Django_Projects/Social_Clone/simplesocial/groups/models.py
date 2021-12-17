from django.db import models
from django.utils.text import slugify # remove any characters that is alpha numeric


import misaka # link embedding

from django.contrib.auth import get_user_model
User = get_user_model()
from django import template
register = template.Library() # This is how we can use custom template tags


class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToMany(User,through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['name']


    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})



class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships')
    user = models.ForeignKey(User,related_name='user_groups')

    def __str__(self):
        reutrn self.user.username

    class Meta:
        unique_together = ('group','user')
# Create your models here.
