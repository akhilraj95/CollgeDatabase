from django.db import models

class Accesslog(models.Model):
    user_addr = models.CharField(max_length=50)
    acs_date = models.DateTimeField('date accessed')
    def __str__(self):
        return self.user_addr

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    reg_date = models.DateTimeField('date registered',auto_now=True)
    bdate = models.DateTimeField('bdate')
    location = models.CharField(max_length=30)
    field = models.CharField(max_length=30)
    def __str__(self):
        return self.email

class StudyField(models.Model):
    name = models.CharField(max_length=40,unique = True)
    def __str__(self):
        return self.name

class Courses_College_Map(models.Model):
    course = models.ForeignKey('Courses', default = None , blank = True)
    college = models.ForeignKey('College' , default = None , blank = True)
    def __str__(self):
        return  self.college.name +" - "+self.course.name


class Courses(models.Model):
    name = models.CharField(max_length=100,unique = True)
    field = models.ForeignKey('StudyField', default = None , blank = True)
    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=150, unique = True)
    date_founded = models.DateField('date founded')
    country = models.CharField(max_length=50)
    website = models.URLField(default=None)
    brief = models.CharField(max_length = 250, default = "We are working on the brief.")
    model_pic = models.ImageField(upload_to = "profile_pic/university/" , default="profile_pic/not_available.jpg" ,null=True)
    visit_count = models.IntegerField(default = 0)
    def __str__(self):
        return self.name

class College(models.Model):
    university = models.ForeignKey('University', on_delete=models.CASCADE , default = None , blank = True)
    name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=300)
    website = models.URLField()
    date_founded = models.DateField('date founded')
    brief = models.CharField(max_length = 250, default = "We are working on the brief.")
    model_pic = models.ImageField(upload_to = "profile_pic/college/" , default="profile_pic/not_available.jpg" ,null=True)
    visit_count = models.IntegerField(default = 0)
    def __str__(self):
        return self.name
