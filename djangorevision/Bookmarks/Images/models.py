from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
    '''Model definition for Image.'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images_created')
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(db_index=True, auto_now_add=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)
    
    
    def __str__(self):
        return self.title
    
    
# class Image(models.Model):
#     def save(self,*arg, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super().save(*arg, **kwargs)
    


# Create your models here.
