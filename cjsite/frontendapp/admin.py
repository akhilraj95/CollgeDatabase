from django.contrib import admin
from .models import Accesslog,User,University,College

admin.site.register(Accesslog)
admin.site.register(University)
admin.site.register(User)
admin.site.register(College)