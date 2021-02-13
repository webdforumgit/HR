from django.db import models
from structure.models import Employeess
import os
# Create your models here.
from datetime import datetime

def content_file_name(instance, filename):
    now = datetime.now()
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.emp_id.id,now, ext)
    return os.path.join('apprizal', filename)

class Apprizals(models.Model):
    submitted_time = models.DateTimeField(auto_now_add=True)
    emp_id = models.ForeignKey(Employeess, related_name='apprizal_emp_id',on_delete=models.CASCADE)
    date = models.DateField(null=True, editable=True)
    intime = models.TimeField(auto_now_add=False,null=True, blank=True)
    outtime = models.TimeField(auto_now_add=False,null=True, blank=True)
    title = models.CharField(max_length=225, blank=False)
    aim = models.TextField(blank=True)
    file = models.FileField(upload_to=content_file_name)
