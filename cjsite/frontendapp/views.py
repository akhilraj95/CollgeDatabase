from django.http import HttpResponse
from .models import Accesslog
from django.shortcuts import render


#TEMP
def index(request):
	latest_access_list = Accesslog.objects.order_by('-acs_date')[:5]
	context = {
		'latest_access_list': latest_access_list,
	}
	return render(request, 'frontendapp/index.html', context)

# Landing page of frontendapp
def home(request):
	context = {}
	return render(request, 'frontendapp/home.html', context)


#TEMP
def results(request):
	return HttpResponse("Results")


#Todo:
	#get req - return the top 10 searched colleges
	#post req - return the colleges similar to the search
	#bootstrap - beautify it
def search(request):
	search_content = ""
	#POST - searches the database for the requested collge
	if request.method == "POST":
		search_content = request.POST['collegename']
	#GET(empty)- gets the top 10 colleges in the database
	else:
		search_content = ""

	Todo = "Todo: Post req handling, search list<br><hr>"
	return HttpResponse(Todo + search_content)