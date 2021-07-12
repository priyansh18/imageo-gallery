from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def gallery(request):
    return render(request,'index.html',context={})
