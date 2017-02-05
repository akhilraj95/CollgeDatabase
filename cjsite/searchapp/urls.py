from django.conf.urls import url

from . import views

urlpatterns = [
	#/home/
 	url(r'^field/(?P<fieldname>[\w\s]+)$',views.field,name='field'),
]
