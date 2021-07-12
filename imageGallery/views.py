from django.shortcuts import render
from django.views.generic import TemplateView
from .models import GalleryImage,Tags
from django.core.paginator import Paginator


# Create your views here.

def gallery(request):
    images = GalleryImage.objects.all()
    p = Paginator(images, 2)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)  # returns the desired page object
    context={
        'images':images,
        'page_obj': page_obj
    }
    return render(request,'index.html',context)
