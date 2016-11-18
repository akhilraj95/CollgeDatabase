from django.conf.urls import url

from . import views

urlpatterns = [
	#/home/
    url(r'^$', views.home, name='home'),
    url(r'^search$',views.search, name='search'),
    url(r'^tokensignin$',views.tokensignin, name='tokensignin'),
    url(r'^logout$',views.logout, name='logout'),
    url(r'^viewcourse/(?P<course_id>[\w\s]+)$',views.viewcourse, name='viewcourse'),
    url(r'^course$',views.courses, name='courses'),

    #home/test
    url(r'^test$',views.index, name='test'),
   	#/home/university/name or id
    url(r'^university/(?P<university>[\w\s]+)$',views.university,name='university'),
    #/home/college/name or id
    url(r'^college/(?P<college>[\w\s]+)$',views.college,name='college'),
]
