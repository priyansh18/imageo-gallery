from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    tags = models.ForeignKey('Tags',blank=True,null=True,on_delete=SET_NULL)
    image = models.ImageField(upload_to='media')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)