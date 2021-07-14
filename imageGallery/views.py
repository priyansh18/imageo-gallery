from django.shortcuts import render
from django.views.generic import TemplateView
from .models import GalleryImage,Tags
from django.core.paginator import Paginator
from django.http.response import Http404


# Create your views here.

def gallery(request):
    print(request.POST)
    images = GalleryImage.objects.all()
    alltags = Tags.objects.all()
    p = Paginator(images, 4)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)  # returns the desired page object
    context={
        'images':images,
        'page_obj': page_obj,
        'imageTags':alltags,
    }
    return render(request,'index.html',context)


def specificImg(request,pk):
    try:
        spec = GalleryImage.objects.get(pk=pk)
    except:
        raise Http404

    context = {
        'specImage': spec
    }

    return render(request, 'specific.html', context)