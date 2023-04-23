from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(LicenseRegistration)
class model1_register(admin.ModelAdmin):
    list_display=['id','dl','owner','doi','expiry','vechile_class','cov_issue','last_payment']
    list_filter=['expiry']

@admin.register(RCRegister)
class model2_register(admin.ModelAdmin):
    list_display=['id','vechile_no','rto_office','fuel_type','owner','reg_date','insurance','permit_no','permit_expiry','fitness']
    list_filter=['permit_expiry']

@admin.register(VechileFine)
class model4_register(admin.ModelAdmin):
    list_display=['id','vechile_no','offence_on','fine','charge','paid_upto','state']

@admin.register(listRtoOffice)
class model4_register(admin.ModelAdmin):
    list_display=['id','name','rto_code','add']

# testing on user models
@admin.register(Officer)
class model4_register(admin.ModelAdmin):
    list_display=['id','username','first_name']

@admin.register(Moderator)
class model4_register(admin.ModelAdmin):
    list_display=['id','username','username']


admin.site.site_header='RTO Admin Console'


