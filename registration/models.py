from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class Extended_User(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(default='', max_length=200)
    last_name = models.CharField(default='', max_length=200)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    score = models.IntegerField(default='0')
    forbidden = models.BooleanField(default=False)
    #email = models.EmailField(default='', blank=True)
    notifications = models.BooleanField(default=False)
    
    #def __str__(self):
        #return self.user
        
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

@receiver(post_save, sender=User)
def create_extended_user(sender, instance, created, **kwargs):
    if created:
        Extended_User.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_extended_user(sender, instance, **kwargs):
    instance.extended_user.save()
