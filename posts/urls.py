from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'create/$', views.add_post, name='add_post'),
    url(r'^(?P<post_id>[0-9]+)/$', views.show_post, name='show_post'),
    url(r'^(?P<post_id>[0-9])/delete/$', views.post_delete, name='post_delete'),
    url(r'^(?P<post_id>[0-9])/update/$', views.UpdateView.as_view(), name='post_update'),
]
