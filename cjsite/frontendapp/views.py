from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.db.models import Q


#importing models
from .models import Accesslog,University,College,User

#TEMP
def index(request):
	context = {
	}
	return render(request, 'frontendapp/index.html', context)

# Landing page of frontendapp
def home(request):
	context = {}
	return render(request, 'frontendapp/home.html', context)


#TEMP
def results(request):
	return HttpResponse("Results")

# Search result page
def search(request):
	college_list = []
	university_list = []
	#POST - searches the database for the requested collge
	if request.method == "POST":
		search_content = request.POST['collegename']
		search_type = request.POST['search_type']
		if search_type == 'college':
			college_list = College.objects.filter(Q(name__icontains = search_content) | Q(alias__icontains = search_content))[:10]
		else:
			university_list = University.objects.filter(Q(name__icontains = search_content) | Q(alias__icontains = search_content))[:10]
	else:
		search_type = request.GET.get('search_type','college')
		if search_type == 'university':
			university_list = University.objects.all()[:10]
		else:
			college_list = College.objects.all()[:10]

	context = {
		'college_list': college_list,
		'university_list':university_list,
	}
	return render(request, 'frontendapp/search.html', context)


# College display
def college(request,college):
	if college.isdigit():
		try:
			obj_col = College.objects.get(id = college)
			obj_col.visit_count += 1
			obj_col.save()
		except College.DoesNotExist:
			raise Http404("You seem to be lost!")
	else:
		try:
			obj_col = College.objects.get(name = college)
			obj_col.visit_count += 1
			obj_col.save()
		except College.DoesNotExist:
			raise Http404("You seem to be lost!")
	context = {
		'college' : obj_col,
	}
	return render(request, 'frontendapp/college.html', context)

# University display
def university(request,university):
	if university.isdigit():
		try:
			obj_uni = University.objects.get(id = university)
			obj_uni.visit_count = obj_uni.visit_count+ 1
			obj_uni.save()
			college_list = College.objects.filter(university = obj_uni)
		except University.DoesNotExist:
			raise Http404("You seem to be lost!")
	else:
		try:
			obj_uni = University.objects.get(name = university)
			obj_uni.visit_count = obj_uni.visit_count+ 1
			college_list = College.objects.filter(university = obj_uni)
		except University.DoesNotExist:
			raise Http404("You seem to be lost!")
	context = {
		'university' : obj_uni,
		'college_list': college_list,
	}
	return render(request, 'frontendapp/university.html', context)
