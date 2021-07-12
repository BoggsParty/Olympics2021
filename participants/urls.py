from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'guess/(?P<sport>[\w-]+)/$', views.guess, name='guess'),
url(r'saved/$', views.guess_saved, name='guess_saved'),
url(r'guesses/all/$', views.all_guess_one_user, name='all_guess_one_user'),
url(r'guesses/all/(?P<sport>[\w-]+)', views.all_guess_all_users, name='all_guess_all_users'),
]