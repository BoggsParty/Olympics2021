from django.conf.urls import include, url
from django.conf.urls import handler404, handler500
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
url(r'sports/$', views.sport_menu, name='sport_menu'),
url(r'faq/', views.FAQ, name='FAQ'),
url(r'detail/(?P<sport>[\w-]+)', views.sport_detail, name='sport-detail'),
url(r'^user/settings/$', views.edit_settings, name='edit-settings'),
url(r'^user/settings-saved/$', views.edit_settings_saved, name='edit-settings-saved'),
url(r'change-password/', auth_views.PasswordChangeView.as_view()),
url('^create-account/', CreateView.as_view(
        template_name='registration/createaccount.html',
        form_class=UserCreationForm,
        success_url='/user/settings/'
    )),
url(r'^logout/$', views.log_out, name='log-out'),
url(r'^calc_scores/$', views.score_calculation, name='score_calculation'),
url(r'^$', views.scores, name='scores'),
]
