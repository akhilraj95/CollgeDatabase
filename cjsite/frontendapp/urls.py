from django.conf.urls import url

from . import views

urlpatterns = [
	#/home/
    url(r'^$', views.home, name='home'),
    url(r'^search$',views.search, name='search'),

    #/home/result/
    #url(r'^college/(?P<question_id>+)$',views.college,name='college'),
   	
   	#/home/university/name or id
    url(r'^university/(?P<university>[\w\s]+)$',views.university,name='university'),

    #/home/college/name or id
    url(r'^college/(?P<college>[\w\s]+)$',views.college,name='college'),
]
