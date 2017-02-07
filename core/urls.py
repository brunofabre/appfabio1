from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^sobre/$', views.about, name='about'),
    url(r'^jogos/$', views.games, name='games'),
    url(r'^ranking/$', views.ranking, name='ranking'),
    url(r'^historico/$', views.history, name='history'),
    url(r'^time/$', views.team, name='team'),
]
