from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from django.conf import settings


#importing models
from frontendapp.models import Accesslog,University,College,User,Courses_College_Map,Courses,StudyField
from .models import access_ticket

#College form
def index(request):
	if request.method == "GET":
		key = request.GET.get('key')
		if key is not None:
			try:
				ticket = access_ticket.objects.get(hash_key = key)
				course = Courses.objects.all()
				university = University.objects.all()
				if ticket.active:
					print("active")
				   	context = {
						'ticket' : ticket,
						'course' : course,
						'key':key,
						'university' : university,
					}
					return render(request, 'crwdsource/home.html', context)
				else:
					return HttpResponse("TICKET EXPIRED: Call support to grant you a access ticket. Your ticket is only valid for one access.")
			except:
				return HttpResponse("UNAUTHORISED ACCESS: Your link has either expired or is invalid. Contact campusjankari support")
	return HttpResponse("UNAUTHORISED ACCESS: Call support to grant you a access ticket. Your ticket is only valid for one access.")

#Form submit
def submit(request):
	if request.method == "POST":
		key = str(request.POST.get('hash'))
		name = str(request.POST.get('college'))
		university = str(request.POST.get('university'))
		modeofoperation = str(request.POST.get('modeofoperation'))
		student_strength = int(request.POST.get('student_strength'))
		courses = request.POST.getlist('courses')
		prof_num = int(request.POST.get('numprof'))
		prof = []
		prof_dept = []
		for i in range(1,prof_num+1):
			prof.append(str(request.POST.get('prof'+str(i))))
			prof_dept.append(str(request.POST.get('prof_dept'+str(i))))
		eligiblestud0 = int(request.POST.get('eligiblestud0'))
		placedstud0 = int(request.POST.get('placedstud0'))
		twoofferstud0 = int(request.POST.get('twoofferstud0'))
		eligiblestud1 = int(request.POST.get('eligiblestud1'))
		placedstud1 = int(request.POST.get('placedstud1'))
		twoofferstud1 = int(request.POST.get('twoofferstud1'))
		eligiblestud2 = int(request.POST.get('eligiblestud2'))
		placedstud2 = int(request.POST.get('placedstud2'))
		twoofferstud2 = int(request.POST.get('twoofferstud2'))
		company1 = str(request.POST.get('company1'))
		company2 = str(request.POST.get('company2'))
		company3 = str(request.POST.get('company3'))
		company4 = str(request.POST.get('company4'))
		company5 = str(request.POST.get('company5'))
		company6 = str(request.POST.get('company6'))
		company7 = str(request.POST.get('company7'))
		company8 = str(request.POST.get('company8'))
		company9 = str(request.POST.get('company9'))
		company10 = str(request.POST.get('company10'))
		activities= str(request.POST.get('activities'))
		club = str(request.POST.get('club'))
		recognition = str(request.POST.get('recognition'))
		association = str(request.POST.get('association'))
	 	special_achievement= str(request.POST.get('specialachievement'))
		others = str(request.POST.get('others'))

		#print("key "+key)
		#print("name "+name)
		#print("university "+university)
		#print("modeofoperation "+modeofoperation)
		#print("student_strength "+str(student_strength))
		print("courses "+ str(courses))
		#print("prof_num "+str(prof_num))
		print("prof "+str(prof))
		print("prof_dept "+str(prof_dept))
		#print("eligiblestud0 "+str(eligiblestud0))
		#print("placedstud0 "+str(placedstud0))
		#print("twoofferstud0 "+str(twoofferstud0))
		#print("eligiblestud1 "+str(eligiblestud1))
		#print("placedstud1 "+str(placedstud1))
		#print("twoofferstud1 "+str(twoofferstud1))
		#print("eligiblestud2 "+str(eligiblestud2))
		#print("placedstud2 "+str(placedstud2))
		#print("twoofferstud2 "+str(twoofferstud2))
		#print("company1 "+company1)
		#print("company2 "+company2)
		#print("company3 "+company3)
		#print("company4 "+company4)
		#print("company5 "+company5)
		#print("company6 "+company6)
		#print("company7 "+company7)
		#print("company8 "+company8)
		#print("company9 "+company9)
		#print("company10 "+company10)
		#print("activities "+str(activities))
		#print("club "+str(club))
		#print("recognition "+str(recognition))
		#print("association "+str(association))
		#print("special_achievement "+str(special_achievement))
		#print("others "+str(others))

		aticket = access_ticket.objects.get(hash_key=key)

		# updating the college model
		college = College.objects.get(id = aticket.college.id)
		college.name = name
		universityobj = University.objects.get(id = university)
		college.university = universityobj
		college.mode_of_operation = modeofoperation
		college.student_strength = student_strength
		college.placement_num_eligible = eligiblestud0
		college.placement_num_placed = placedstud0
		college.placement_num_with_two_offers = twoofferstud0
		college.placement_num_eligible1 = eligiblestud1
		college.placement_num_placed1 = placedstud1
		college.placement_num_with_two_offers1 = twoofferstud1
		college.placement_num_eligible2 = eligiblestud2
		college.placement_num_placed2 = placedstud2
		college.placement_num_with_two_offers2 = twoofferstud2
		college.placement_majorcompany1 = company1
		college.placement_majorcompany2 = company2
		college.placement_majorcompany3 = company3
		college.placement_majorcompany4 = company4
		college.placement_majorcompany5 = company5
		college.placement_majorcompany6 = company6
		college.placement_majorcompany7 = company7
		college.placement_majorcompany8 = company8
		college.placement_majorcompany9 = company9
		college.placement_majorcompany10 = company10
		college.activities = activities
		college.clubs = club
		college.recognition = recognition
		college.association = association
		college.special_achievement = special_achievement
		college.other_text = others
		college.save()

		#updating the courses of the college
		#removing the previously existing data of the college

		return HttpResponse("done")
	return HttpResponse("UNAUTHORISED ACCESS: Call Campusjankari Support");