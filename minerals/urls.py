from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'(?P<pk>\d+)/$', views.mineral_details, name='detail'),
    url(r'^$', views.minerals_list, name='list'),
]