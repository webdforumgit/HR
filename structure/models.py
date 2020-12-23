from django.db import models
# from django.contrib.auth.models import (
#     AbstractBaseUser, BaseUserManager, PermissionsMixin)
# from django.utils.timezone import timezone
from datetime import datetime
STATUS_CHOICES = (
    ("ACTIVE", "active"),
    ("SUSPENDED", "suspend"),
    ("TRANSFERED", "transfered"),
    ("LEFT", "left"),
)

class Company_details(models.Model):
    now = datetime.now()
    company = models.CharField(max_length=100,blank=False,unique=True)
    company_name = models.CharField(max_length=500, blank=False,default=True)
    company_user_email=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=1000, blank=True)
    primary_uuid = models.TextField(max_length=360, blank=False)
    andriod_app_permisiion = models.CharField(max_length=200,blank=False,default=False)
    max_accesable_uuid_no=models.CharField(max_length=200,blank=False,default='1')
    logo = models.ImageField(upload_to='company_logo',default='default_company_logo.jpg')
    created_at = models.DateTimeField(default=now)

    class Meta:
        unique_together = (('company', 'company_user_email'))

    def __str__(self):
        return self.company
class Branches(models.Model):
    company_id=models.ForeignKey(Company_details,related_name='company_branch_id',on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=200, blank=False)
    address = models.TextField(max_length=1000, blank=False)
    primary_uuid = models.TextField(max_length=360, blank=False)
    max_accesable_uuid_no = models.CharField(max_length=200, blank=False, default='1')



class Company_uuids(models.Model):
    company_uuid=models.ForeignKey(Company_details,related_name='company_uuid',on_delete=models.CASCADE,default=True)
    uuid = models.CharField(max_length=100, blank=False,default=True)
    authenticated = models.BooleanField(max_length=100, blank=False,default=False)

class Branche_uuids(models.Model):
    branch_uuid=models.ForeignKey(Branches,related_name='branch_uuid',on_delete=models.CASCADE,default=True)
    uuid = models.CharField(max_length=100, blank=False,default=True)
    authenticated = models.BooleanField(max_length=100, blank=False,default=False)

class Departments(models.Model):
    branch_deparments=models.ForeignKey(Branches,related_name='branch_deparments',on_delete=models.CASCADE,default=True)
    name = models.CharField(max_length=100, blank=False)

class Designations(models.Model):
    department_wise_designation=models.ForeignKey(Departments,related_name='department_wise_designation',on_delete=models.CASCADE,default=True)
    name = models.CharField(max_length=100, blank=False)



class Employeess(models.Model):
    company_id = models.ForeignKey(Company_details, related_name='company_id', on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branches, related_name='branch_id', on_delete=models.CASCADE)
    deparment_id = models.ForeignKey(Departments, related_name='deparment_id', on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designations, related_name='designation_id', on_delete=models.CASCADE)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password=models.CharField(max_length=20,blank=False,default=True)
    firstname = models.CharField(max_length=255,blank=False,default='' )
    lastname = models.CharField(max_length=255,blank=False,default='' )
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    sample_taken = models.BooleanField(default=False)
    employee_id = models.CharField(max_length=255)
    status = models.CharField(max_length = 20,
        choices = STATUS_CHOICES,
        default = 'ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_photo = models.ImageField(upload_to='employee_photo', default='defalut_employee.jpg')
    class Meta:
        unique_together = (('username', 'email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']




