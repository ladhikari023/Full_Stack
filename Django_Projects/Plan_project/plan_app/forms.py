from plan_app.models import Plan,Comment
from django.contrib.auth.models import User
from django import forms

# Creating form using ModelForm
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')


class PlanForm(forms.ModelForm):
    class Meta():
        model = Plan
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass black-text'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass black-text'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
