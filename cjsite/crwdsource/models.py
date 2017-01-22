import time
import hashlib
from django.db import models

def _createHash():
    """This function generate 10 character long hash"""
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return  hash.hexdigest()[:-10]


class access_ticket(models.Model):
    acs_date = models.DateTimeField('date created')
    active = models.BooleanField(default=True)
    college = models.ForeignKey('frontendapp.College', default = None , blank = True)
    hash_key = models.CharField(max_length=30,default=_createHash(),unique=True)
    def save(self, *args, **kwargs):
        self.hash_key=_createHash()
        super(access_ticket, self).save(*args, **kwargs)
    def __str__(self):
        return "www.campusjankari.com/collegeform?key="+self.hash_key
