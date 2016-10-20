from django.conf.urls import url

from . import views

urlpatterns = [
	#/home/
    url(r'^$', views.home, name='home'),
    url(r'^search$',views.search, name='search'),
    #/home/result
    url(r'^colleges$',views.results,name='results'),
]
