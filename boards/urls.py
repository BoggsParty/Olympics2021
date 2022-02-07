from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'message-board/$', views.messages_first_page, name='messages-first-page'),
url(r'message-board/(?P<num>[0-9]+)', views.messages, name='messages'),
url(r'message-board/comment/$', views.new_comment, name='new-comment'),
url(r'message-board/response/(?P<pk>[0-9]+)/$' , views.new_response, name='new-response'),
url(r'message-board/comment/edit/(?P<pk>[0-9]+)/$', views.edit_comment, name='edit-comment'),
url(r'message-board/response/edit/(?P<pk>[0-9]+)/$' , views.edit_response, name='edit-response'),
]