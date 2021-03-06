from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^addPost/$', views.addNewPost, name='addNewPost'),
]