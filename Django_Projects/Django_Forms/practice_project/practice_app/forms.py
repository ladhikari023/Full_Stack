from . import models
from django.forms import ModelForm


class AuthorForm(ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'
