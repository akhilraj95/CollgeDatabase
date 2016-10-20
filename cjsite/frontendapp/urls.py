from django.conf.urls import url

from . import views

urlpatterns = [
	#/home/
    url(r'^$', views.index, name='index'),
    #/home/result
    url(r'^colleges/$',views.results,name='results'),
]
