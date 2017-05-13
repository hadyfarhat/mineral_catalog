from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<pk>\d+)/$', views.mineral_details, name='detail'),
    url(r'random/$', views.random_mineral, name='random'),
    url(r'^$', views.minerals_list, name='list'),
]
