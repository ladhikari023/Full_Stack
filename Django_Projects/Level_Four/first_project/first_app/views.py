from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':"Some Text",'number':100}
    return render(request,'first_app/index.html',context=context_dict)

def other(request):
    return render(request,'first_app/other.html')

def relative(request):
    return render(request,'first_app/relative_url_templates.html')
