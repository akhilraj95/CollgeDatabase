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
    is_post_graduate = models.BooleanField(default=False)
    visit_count = models.IntegerField(default = 0)
    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=150, unique = True)
    date_founded = models.DateField('date founded')
    country = models.CharField(max_length=50)
    website = models.URLField(default=None)
    brief = models.CharField(max_length = 250, default = "We are working on the brief.")
    model_pic = models.ImageField(upload_to = "university/" , default="not_available.jpg" ,null=True)
    visit_count = models.IntegerField(default = 0)
    alias = models.CharField(max_length=40, null=True)
    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=150)
    college = models.ForeignKey('College', on_delete=models.CASCADE , default = None , blank = True)
    field = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class College(models.Model):
    university = models.ForeignKey('University', on_delete=models.CASCADE , default = None , blank = True)
    name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=300)
    alias = models.CharField(max_length=40, null=True)
    website = models.URLField()
    date_founded = models.DateField('date founded')
    brief = models.CharField(max_length = 250, default = "We are working on the brief.")
    logo = models.ImageField(upload_to = "college/" , default="not_available.jpg" ,null=True)
    model_pic = models.ImageField(upload_to = "college/" , default="not_available.jpg" ,null=True)
    model_pic_1 = models.ImageField(upload_to = "college/" , default="not_available.jpg" ,null=True)
    model_pic_2 = models.ImageField(upload_to = "college/" , default="not_available.jpg" ,null=True)
    model_pic_3 = models.ImageField(upload_to = "college/" , default="not_available.jpg" ,null=True)
    visit_count = models.IntegerField(default = 0)
    placement_text = models.CharField(max_length=3000,default = "No data available. We are working towards bring you the information you requrie.")
    activity_text = models.CharField(max_length=3000,default = "No data available. We are working towards bring you the information you requrie.")
    student_strength = models.IntegerField(default = 0)
    MODE_OF_OPERATION_CHOICES = (
        ('a', 'Private'),
        ('b', 'Government'),
        ('c', 'Government Aided'),
        ('d', 'Trust'),
    )
    mode_of_operation = models.CharField(max_length=1, choices=MODE_OF_OPERATION_CHOICES,default='a')
    clubs = models.CharField(max_length=2000,default="No Data available")
    recognition = models.CharField(max_length=1000,default="None")
    association = models.CharField(max_length=1000,default="None")
    placement_num_eligible   = models.IntegerField(default = 0)          # record for the current year
    placement_num_placed = models.IntegerField(default = 0)
    placement_num_with_two_offers = models.IntegerField(default = 0)
    placement_num_eligible1 = models.IntegerField(default = 0)          # record for the last year
    placement_num_placed1 = models.IntegerField(default = 0)
    placement_num_with_two_offers1 = models.IntegerField(default = 0)   # record for two years before
    placement_num_eligible2 = models.IntegerField(default = 0)
    placement_num_placed2 = models.IntegerField(default = 0)
    placement_num_with_two_offers2 = models.IntegerField(default = 0)
    placement_majorcompany1 = models.CharField(max_length=150,default="None")
    placement_majorcompany2 = models.CharField(max_length=150,default="None")
    placement_majorcompany3 = models.CharField(max_length=150,default="None")
    placement_majorcompany4 = models.CharField(max_length=150,default="None")
    placement_majorcompany5 = models.CharField(max_length=150,default="None")
    placement_majorcompany6 = models.CharField(max_length=150,default="None")
    placement_majorcompany7 = models.CharField(max_length=150,default="None")
    placement_majorcompany8 = models.CharField(max_length=150,default="None")
    placement_majorcompany9 = models.CharField(max_length=150,default="None")
    placement_majorcompany10 = models.CharField(max_length=150,default="None")
    special_achievement = models.CharField(max_length=150,default="None")
    other_text = models.CharField(max_length=3000,default="no data")
    def __str__(self):
        return self.name
