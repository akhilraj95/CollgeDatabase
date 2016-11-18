from django.contrib import admin
from .models import Accesslog,User,University,College,StudyField,Courses,Courses_College_Map

admin.site.register(Accesslog)
admin.site.register(University)
admin.site.register(User)
admin.site.register(College)
admin.site.register(StudyField)
admin.site.register(Courses)
admin.site.register(Courses_College_Map)
