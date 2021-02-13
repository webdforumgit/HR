from django.db import models
from datetime import datetime
import os
# Create your models here.
from structure.models import Employeess


class Attendence(models.Model):
    employee_id=models.ForeignKey(Employeess,related_name='employee_id_wise_attendence',on_delete=models.CASCADE,default=True)
    date = models. DateField(auto_now=True,editable=False)
    intime = models.TimeField(auto_now_add=True,auto_now=False,blank=True)
    in_time_recorded= models.BooleanField(default=True)
    outtime = models.TimeField(auto_now_add=False,auto_now=True,blank=True,null=True)
    out_time_recorded =  models.BooleanField(default=False)

    class Meta:
        unique_together = (('employee_id', 'date'))

def content_file_name(instance, filename):
    now = datetime.now()
    ext = filename.split('.')[-1]
    filename = "%s_.%s" % (instance.employee_id.id,ext)
    return os.path.join('facesamplecollection', filename)

class Attendence_sample_video(models.Model):
    employee_id=models.ForeignKey(Employeess,related_name='employee_id_wise_video',on_delete=models.CASCADE,default=True)
    file = models.FileField(upload_to=content_file_name)

    # class Meta:
    #     unique_together = (('employee_id', 'date'))

