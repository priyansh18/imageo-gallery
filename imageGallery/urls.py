from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.gallery,name="gallery"),
    path('gallery/<int:pk>',views.specificImg,name="specificImg"),
    path('add',views.addImage,name="add"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)