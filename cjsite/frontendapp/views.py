from django.http import HttpResponse,Http404
from django.shortcuts import render


#importing models
from .models import Accesslog,University,College,User

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


searchTodo = """
->get req - return the top 10 searched colleges 
->post req - return the colleges similar to the search 
->bootstrap - beautify it 
"""
# Search result page
def search(request):
	#POST - searches the database for the requested collge
	if request.method == "POST":
		search_content = request.POST['collegename']
		college_list = College.objects.filter(name__icontains = search_content)
	#GET(empty)- gets the top 10 colleges in the database
	else:
		college_list = College.objects.all()

	context = {
		'college_list': college_list,
	}
	return render(request, 'frontendapp/search.html', context)



# College display
def college(request,college):
	if college.isdigit():
		try:
			obj_col = College.objects.get(id = college)
		except College.DoesNotExist:
			raise Http404("You seem to be lost!")
	else:
		try:
			obj_col = College.objects.get(name = college)
		except College.DoesNotExist:
			raise Http404("You seem to be lost!")
	return HttpResponse("University"+obj_col.website)

# University display
def university(request,university):
	if university.isdigit():
		try:
			obj_uni = University.objects.get(id = university)
		except University.DoesNotExist:
			raise Http404("You seem to be lost!")
	else:
		try:
			obj_uni = University.objects.get(name = university)
		except University.DoesNotExist:
			raise Http404("You seem to be lost!")
	return HttpResponse("University"+obj_uni.website)
