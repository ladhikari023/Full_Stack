from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Plan(models.Model):
    author = models.ForeignKey('auth.User',related_name='plans',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text =  models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse('plan_detail',kwargs={'pk':self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Comment(models.Model):
    plan = models.ForeignKey('Plan',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
