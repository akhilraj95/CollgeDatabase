from django.db import models


class Accesslog(models.Model):
    user_addr = models.CharField(max_length=50)
    acs_date = models.DateTimeField('date accessed')
    def __str__(self):
    	return self.user_addr

