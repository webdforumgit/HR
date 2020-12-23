from django.db import models
from structure.models import Branches,Employeess
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import datetime
STATUS_CHOICES = (
    ("PENDING", "PENDING"),
    ("PROCESSING", "PROCESSING"),
    ("COMPLETED", "COMPLETED"),
)
import os
class Work_flow(models.Model):
    branch_wise_workflow = models.ForeignKey(Branches, related_name='branch_wise_workflow', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    dead_line = models.DateField(null=True,editable=True)
    is_done=models.BooleanField(default=False)
    status=models.CharField(max_length=100,blank=False,default="PROCESSING",choices = STATUS_CHOICES,)

class Work_flow_employee_detail(models.Model):
    workflow_id = models.ForeignKey(Work_flow, related_name='workflow_id',
                                             on_delete=models.CASCADE)
    emp_id = models.ForeignKey(Employeess, related_name='emp_id',
                                    on_delete=models.CASCADE)
    role = models.CharField(max_length=100, blank=False)
    assignment = models.TextField(max_length=1000, blank=False)
    progress = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)],default=0)
    status = models.CharField(max_length=100, blank=False, default="PROCESSING",choices = STATUS_CHOICES,)



def content_file_name(instance, filename):
    now = datetime.now()
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.workflow_id_uplodaed_file.id,now, ext)
    return os.path.join('uploads', filename)

class Uplodaed_file(models.Model):

    workflow_id_uplodaed_file = models.ForeignKey(Work_flow_employee_detail, related_name='workflow_id_uplodaed_file',
                                    on_delete=models.CASCADE)
    remarks = models.CharField(max_length=100, default='')
    file = models.FileField(upload_to=content_file_name)

