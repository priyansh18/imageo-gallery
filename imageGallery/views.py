from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import GalleryImage, Tags
from django.core.paginator import Paginator
from django.http.response import Http404

# Create your views here.
def gallery(request):
    tag = request.GET.get('tag')
    if tag == None:
        images = GalleryImage.objects.all()
    else:
        images = GalleryImage.objects.filter(tags__name=tag)

    alltags = Tags.objects.all()
    p = Paginator(images, 3)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)  # returns the desired page object
    context = {
        'images': images,
        'page_obj': page_obj,
        'mytags': alltags,
    }
    return render(request, 'index.html', context)


def specificImg(request, pk):

    try:
        spec = GalleryImage.objects.get(pk=pk)
    except:
        raise Http404

    context = {
        'specImage': spec
    }

    return render(request, 'specific.html', context)


def addImage(request):
    alltags = Tags.objects.all()

    if request.method == "POST":
        data = request.POST
        files = request.FILES.get('image')

        if data['tags'] != 'none':
            tag = Tags.objects.get(id=data['tags'])
        elif data['tag_new'] != '':
            tag, created = Tags.objects.get_or_create(name=data['tag_new'])
        else:
            tag = None

        photo = GalleryImage.objects.create(
            tags=tag,
            image=files,
        )

        return redirect('gallery')

    context = {
        'tags': alltags,
    }
    return render(request, 'add.html', context)
