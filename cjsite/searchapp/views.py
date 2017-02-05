from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage


#importing models
from frontendapp.models import Accesslog,University,College,User,Courses_College_Map,Courses,StudyField,Professor


#College form
def field(request,fieldname):
    StudyFieldobj = StudyField.objects.get(name = fieldname)
    course = Courses.objects.filter(field = StudyFieldobj)
    college_list = Courses_College_Map.objects.filter(course__in = course).values("college")
    college_list = College.objects.filter(id__in = college_list)
    context = {
        "fieldname":fieldname,
        "college_list":college_list,
    }
    return render(request,"searchapp/stream.html",context)


# def viewcourse(request,course_id):
#     course= Courses.objects.get(id = course_id)
#     course.visit_count += 1
#     course.save()
#     college_list = Courses_College_Map.objects.filter(course__id = course_id).values("college")
#     college_list = College.objects.filter(id__in = college_list)
#     context = {
#         "college_list":college_list,
#         "course":course,
#     }
#     sessioncontext = getsessionvar(request)
#     context.update(sessioncontext)
#     return render(request,"frontendapp/viewcourse.html",context)
