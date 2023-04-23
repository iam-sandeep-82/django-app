from django.db import models
import random
import datetime as dt
std_dt=dt.datetime.now()


class CustomManager(models.Manager):

    # CHECKING

    def is_owner_exists(self,name):
        return super().get_queryset().filter(owner__iexact=name).exists()

    def is_vechile_exists(self,vech_no):
        return super().get_queryset().filter(vechile_no__iexact=vech_no).exists()
    
    def is_dl_exists(self,dl_no):
        return super().get_queryset().filter(dl__iexact=dl_no).exists()
    
    def is_email_exists(self,email):
        return super().get_queryset().filter(email__iexact=email).exists()

    def is_permit_no(self,permit_no):
        return super().get_queryset().filter(permit_no__iexact=permit_no).exists()


    gen_dl=''
    def dl_gen(self,**kwargs):
        x=kwargs['state']
        y=kwargs['rto']
        global gen_dl
        last_6_digit=random.randint(0,200000)
        gen_dl=str(x) + str(y)+ str(std_dt.year) + str(last_6_digit)
        return gen_dl

    

    


    

    
    

