from django.http import HttpResponse
from django.template import loader
from .models import Accesslog
from django.shortcuts import render


def index(request):
	latest_access_list = Accesslog.objects.order_by('-acs_date')[:5]
	template = loader.get_template('frontendapp/index.html')
	context = {
		'latest_access_list': latest_access_list,
	}
	return render(request, 'frontendapp/index.html', context)

def results(request):
	return HttpResponse("Results")

