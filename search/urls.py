from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$',views.index, name = 'index'),
	url(r'^search',views.search, name = 'search'),
	url(r'^advanced_search',views.advanced_search,name = 'advanced_search'),
	#url(r'^advanced_search/(?P<key>[^/]+)/(?P<location>[^/]+)/()/',views.advanced_search, name = 'advanced_search'),
]
