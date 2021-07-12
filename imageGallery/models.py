from django.db import models

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    tags = models.ManyToManyField('Tags',blank=True)
    image = models.ImageField(upload_to='media')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)