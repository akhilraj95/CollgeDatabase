from django.conf.urls import url

from . import views

urlpatterns = [
	#/home/
    url(r'^submit$',views.submit,name='submit'),
    url(r'^$', views.index, name='index'),
]
