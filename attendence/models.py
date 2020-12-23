from django.db import models

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

