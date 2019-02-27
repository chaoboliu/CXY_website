from django.conf.urls import url
from YOU1 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^write/$', views.write, name='write'),
    url(r'^details/(\d+)$', views.details, name='details'),
    url(r'^list/$', views.list, name='list'),
    url(r'^c_login/$', views.c_login, name='c_login'),
    url(r'^dlu/$', views.dlu, name='dlu'),
    url(r'^yes/$', views.yes, name='yes'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^forum/$', views.luntan, name='forum'),
    url(r'^problem/$', views.problem, name='problem'),
    url(r'^yes2/$', views.yes2, name='yes2'),
    url(r'^fplun/(\d+)$', views.fplun, name='fplun'),
    url(r'^yes3/$', views.yes3, name='yes3'),
    url(r'^yes4/$', views.yes4, name='yes4'),
    url(r'^music/$', views.music, name='music'),
    url(r'^musicjs/$', views.musicjs, name='musicjs'),

]