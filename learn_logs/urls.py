#app learn_logs自定义url
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^topics/$',views.topics,name='topics'),
    url(r'^addfile/$',views.addfile,name='addfile'),
    url(r'^write_cache/$',views.write_cache,name='write_cache'),
    url(r'^topics_json/$',views.topics_json,name='topics_json'),
    url(r'^titles/$',views.titles,name='titles'),
    url(r'^topic/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry,name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
    url(r'^delete_entry/(?P<entry_id>\d+)/$', views.delete_entry,name='delete_entry'),
    url(r'^delete_topic/(?P<topic_id>\d+)/$', views.delete_topic,name='delete_topic'),
]