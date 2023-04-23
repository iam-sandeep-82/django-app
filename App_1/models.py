from django.db import models
from .choice import *
from datetime import *
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User,AbstractUser
from .managers import *
current_date=datetime.now()
paid_upto = current_date + relativedelta(months=2)

'owner vechile_no common datefield'

class Officer(User):
    man_objects=CustomManager()
    class Meta:
        db_table = "Officer"

    def __str__(self):
        return self.first_name
  

class Moderator(User):
    man_objects=CustomManager()

    class Meta:
        db_table = "Moderator"

    def __str__(self):
        return self.username


class listRtoOffice(models.Model):
    name=models.CharField(max_length=255)
    rto_code=models.IntegerField(default=43)
    add=models.TextField()

    def __str__(self):
        return self.name

class LicenseRegistration(models.Model):
    dl=models.CharField(max_length=20,unique=True)
    owner=models.CharField(max_length=255,blank=False)
    surname=models.CharField(max_length=255,blank=False)
    doi=models.DateField(default=current_date)
    expiry=models.DateField()
    last_payment=models.ForeignKey(listRtoOffice,on_delete=models.CASCADE)
    vechile_class=models.CharField(choices=list_of_vech_class,max_length=20,blank=False)
    cov_issue=models.DateField()
    man_objects=CustomManager()
    objects = models.Manager()

    def __str__(self):
        return self.dl


class RCRegister(models.Model):
    vechile_no=models.CharField(max_length=10)
    rto_office=models.ForeignKey(listRtoOffice,on_delete=models.CASCADE)
    owner=models.CharField(max_length=25)
    fuel_type=models.CharField(choices=list_fuel_type, max_length=100)
    reg_date=models.DateField(default=current_date)
    insurance=models.DateField()
    permit_expiry=models.DateField()
    permit_no=models.CharField(max_length=20)
    
    fitness=models.CharField(max_length=10)
    

    man_objects=CustomManager()
    objects = models.Manager()

    def __str__(self):
        return self.vechile_no

class VechileFine(models.Model):
    vechile_no=models.CharField(max_length=12)
    fine=models.CharField(choices=list_fine_charge,max_length=100)
    charge=models.IntegerField()
    offence_on=models.DateField(default=current_date)
    paid_upto=models.DateField(default=paid_upto)
    state=models.CharField(choices=list_states,max_length=20)


    man_objects=CustomManager()
    objects = models.Manager()

    def __str__(self):
        return self.fine
        






