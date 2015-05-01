from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search, name='search'),
    url(r'^advanced_search', views.advanced_search, name='advanced_search'),
    url(r'^mapTest/', views.map_test, name='mapTest'),
    url(r'^query', views.query, name='query'),
    #url(r'^newsList$', views.news_list, name="newsList"),
    url(r'^article/(?P<key>[0-9]+)/?$', views.article, name='article'),
    # url(r'^advanced_search/(?P<key>[^/]+)/(?P<location>[^/]+)/()/',views.advanced_search, name = 'advanced_search'),
]

