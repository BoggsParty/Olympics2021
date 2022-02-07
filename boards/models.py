from django.db import models

class Comments(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    message = models.TextField(blank=True)
    
class Responses(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    message = models.TextField(blank=True)
    comment = models.ForeignKey('Comments', on_delete=models.CASCADE)
