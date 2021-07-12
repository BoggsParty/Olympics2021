from django.db import models

class Flat_Page(models.Model):
    title = models.CharField(max_length=200, default='', unique=True, blank=True)
    slug = models.SlugField(default='', unique=True, blank=True)
    content = models.TextField(default='', blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Flat Page"
        verbose_name_plural = "Flat Pages"