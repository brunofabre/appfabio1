from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^entrar/$', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^registro/$', views.register, name='register'),
]
