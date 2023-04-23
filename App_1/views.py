from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib import messages
import datetime as dt
from dateutil.relativedelta import relativedelta
from django.urls import reverse, reverse_lazy, resolve
from .choice import dict_challan
from .Auth_Forms import SignUpForm
from django.contrib.auth.models import Group
from Base.settings import *
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.contrib.auth.models import User
from django.db.models import Q, Avg, Sum, Min,Count
from .managers import *
from .utility import *

# app_name='App_1'
# Create your views here.

std_dt=datetime.now()
curr_date=dt.date(year=std_dt.year,month=std_dt.month,day=std_dt.day)

# ----------------------------------[ HOME VIEWS ]-----------------------------------------
def home(request):
    # 14th feb 2019
    print(request.META['HTTP_HOST'])
    # print(request.META['HTTP_REFERER'])
    print(request.META['QUERY_STRING'])
    # print(request.META['REMOTE_USER'])
    print(request.META['SERVER_NAME'])
    print(request.META['SERVER_PORT'])
    print(request.headers)
    print(request.is_secure)
    
    

    curr_date_time=std_dt.strftime('%dth-%A-%Y | %H:%M:%S')

    salution_list=['Good, Morning','Good, Afternoon', 'Good, Evening']
    
    if std_dt.hour>=6 and std_dt.hour<=12:
        sal=salution_list[0]
    elif std_dt.hour>12 and std_dt.hour<=16:
        sal=salution_list[1]

    elif std_dt.hour>16 and std_dt.hour<=18:
        sal=salution_list[2]
    else:
        sal='Good, Night'
        vech_no=' mh43 c 549'
        vech_no=vech_no.strip().upper()
        
        x=VechileFine.objects.all().filter(vechile_no__iexact='mh43c549')
        print(x)
        y=x.aggregate(Sum('charge'))
        z=x.aggregate(Min('charge'))
        z=x.aggregate(Count('charge'))
        print(y['charge__sum'])
        print(z.get('charge__min'))
        print('Challans' + str(z.get('charge__count')))


    if request.user is not None:
        curr_user=request.user.username

    context={'text':'DL Register','title':'VAHAN|HOME','time':curr_date_time,'sal':sal,'curr_user':curr_user}
    return render(request, 'App_1//home.html',context)
    

# ----------------------------------[ DL-SEARCH VIEWS ]-----------------------------------------

def dl_search(request):

    if request.method=='POST':
        
        form_ins=Search_ModelForm(request.POST)
        if form_ins.is_valid():
            dl=form_ins.cleaned_data['dl']
            res=LicenseRegistration.man_objects.is_dl_exists(dl)

            if res:
                detail=LicenseRegistration.objects.filter(dl__iexact=dl)
                # print('PERMIT EXPIRY' + detail.get('per   mit_expiry'))

                context={
                    'caption':f'Search result for {dl}','res':detail }
                return render(request,'App_1//dl-result.html',context)
                
            else:
                context={
                    'res':f'No Data found for Driving License {dl}' ,'title':'No-Data-Found','url':reverse('App_1:SEARCH') }
                return render(request,'App_1//nodatafound.html',context)
  
    else:
        form_ins=Search_ModelForm()
    context={
        'form_ins':form_ins,'title':'DL-SEARCH','search_for':'Driving License',
    }
    return render(request,'App_1//searchpage.html',context)

# ----------------------------------[ RC-SEARCH VIEWS ]-----------------------------------------

def rc_search(request):

    if request.method=='POST':
        
        form_ins=RC_Search_Form_Api(request.POST)
        if form_ins.is_valid():

            vechile_no=form_ins.cleaned_data['vechile_no']

            model_obj=RCRegister.objects.all()
            
            if form_ins.cleaned_data['vechile_no']:
                res=model_obj.filter(vechile_no__iexact=form_ins.cleaned_data['vechile_no'])
        

                if bool(res)==True:
                    context={
                        'caption':f'Search result for {vechile_no}','res':res }
                    return render(request,'App_1//rc-result.html',context)
                
                else:
                    context={
                        'res':vechile_no,'url':reverse('App_1:RC-SEARCH')}
                    return render(request,'App_1//nodatafound.html',context)
        

    else:
        form_ins=RC_Search_Form_Api()

    context={
        'form_ins':form_ins,'title':'RC-SEARCH','search_for':'Vechile | RC',
    }
    return render(request,'App_1//searchpage.html',context)

# ----------------------------------[ FINE-SEARCH VIEWS ]-----------------------------------------
def fine_search(request):

    if request.method=='POST':
        
        form_ins=RC_Search_Form_Api(request.POST)
        if form_ins.is_valid():

            vechile_no=form_ins.cleaned_data['vechile_no']

            # model_obj=VechileFine.objects.all()
            
            
            if form_ins.cleaned_data['vechile_no']:
            
                res=VechileFine.objects.all().filter(vechile_no__iexact=form_ins.cleaned_data['vechile_no'])

                total_fine=res.aggregate(Sum('charge'))
                total_fine=total_fine.get('charge__sum')
                print('total_fine'+ str(total_fine))

                no_of_challans=res.aggregate(Count('fine'))
                no_of_challans=no_of_challans['fine__count']
                print(no_of_challans)

                # total_fine=0
                # for chrg in res:
                #     total_fine+=chrg.charge
                # print(total_fine)
                
                if bool(res)==True:
                    
                    context={
                        'vechile_no':vechile_no,'res':res,'total_fine':total_fine,'no_of_challans':no_of_challans}
                    return render(request,'App_1//fine-result.html',context)
                
                else:
                    context={
                        'res':f'No Fines found for Vechile No {vechile_no}','url':reverse('App_1:FINE-SEARCH')}
                    return render(request,'App_1//nodatafound.html',context)
        

    else:
        form_ins=RC_Search_Form_Api()

    context={
        'form_ins':form_ins,'title':'PAY-FINE','search_for':'Fine | Challan',
    }
    return render(request,'App_1//searchpage.html',context)



# ----------------------------------[ ALL DL HOLDERS USERS ]-----------------------------------------
@login_required(login_url=LOGIN_URL)
def dl_allusers(request):
    
    model_obj=LicenseRegistration.objects.all()
        
    context={
        'title':'ALL-DL-USERS','res':model_obj,'caption':'Driving License Holders',
    }

    return render(request,'App_1//dl-result.html',context)

# ----------------------------------[ ALL RC ]-----------------------------------------
@login_required(login_url=LOGIN_URL)
def rc_allusers(request):
    
    model_obj=RCRegister.objects.all()
        
    context={
        'title':'ALL-RC-USERS','res':model_obj,'caption':'Registration Certificate copy ',
    }

    return render(request,'App_1//rc-result.html',context)

# ----------------------------------[ DL REGISTRATION VIEWS ]-----------------------------------------
@login_required(login_url=LOGIN_URL)
def dl_registration(request,statecode):
    dt=datetime.now()
    time=dt
    if request.method=='POST':
        form_ins=LR_ModelForm(request.POST)

        if form_ins.is_valid():
            model_obj=LicenseRegistration.objects.all()
            print('Validation Done')

            # FETCH THE DATA FROM USER FORM
            owner=form_ins.cleaned_data['owner']
            surname=form_ins.cleaned_data['surname']
            last_payment=form_ins.cleaned_data['last_payment']
            vechile_class=form_ins.cleaned_data['vechile_class']

            #DEFAULT FIELDS WHICH ABSTRACT FROM USER
                
            doi=curr_date
            cov_issue=curr_date
            expiry= doi + relativedelta(years=2)
            # TESTING ON MANAGER
            while True:
                gen_dl=LicenseRegistration.man_objects.dl_gen(state='MH',rto=43)
                if not LicenseRegistration.man_objects.is_dl_exists(gen_dl):                                 
                    model_obj=LicenseRegistration(dl=gen_dl,owner=owner.title(),surname=surname.title(),doi=doi,expiry=expiry,cov_issue=cov_issue,last_payment=last_payment,vechile_class=vechile_class)
                    model_obj.save()
                    messages.success(request, f'Driving License No {gen_dl} is issued for {owner.upper()}')
                    form_ins=LR_ModelForm()
                    break
                else:
                    continue
                    

    else:
        form_ins=LR_ModelForm()

    context={
        'form_ins':form_ins,'title':'DL-REG','statecode':statecode,
        'time':time,'date':date,'header':'Driving License Registration'
    }
    return render(request,'App_1//registration.html',context)

# ----------------------------------[ RC REGISTRATION VIEWS ]-----------------------------------------
@login_required(login_url=LOGIN_URL)
def rc_register(request,statecode):
    if request.method=='POST':
        form_ins=RC_ModelForm(request.POST)

        if form_ins.is_valid():
            model_obj=RCRegister.objects.all()
            print('Validation Done')
            vechile_no=form_ins.cleaned_data['vechile_no']
            owner=form_ins.cleaned_data['owner']
            fuel_type=form_ins.cleaned_data['fuel_type']
            rto_office=form_ins.cleaned_data['rto_office']
            reg_date=form_ins.cleaned_data['reg_date']
            insurance=form_ins.cleaned_data['insurance']
            permit_no=form_ins.cleaned_data['permit_no']

            permit_expiry= curr_date + relativedelta(years=2)

       

            if form_ins.cleaned_data['vechile_no'] or form_ins.cleaned_data['permit_no']:
                res1=model_obj.filter(vechile_no__iexact=form_ins.cleaned_data['vechile_no'])
                res2=model_obj.filter(permit_no__iexact=form_ins.cleaned_data['permit_no'])

                if (res1.exists()==False) and (res2.exists()==False):                  
                    model_obj=RCRegister(vechile_no=vechile_no.upper(),rto_office=rto_office,fuel_type=fuel_type,owner=owner.title(),reg_date=reg_date,insurance=insurance,permit_no=permit_no,permit_expiry=permit_expiry,fitness='ACTIVE')
                    model_obj.save()
                    messages.success(request, f'RC of {permit_no} and {vechile_no} is Succesfully Register!!!')
                    form_ins=RC_ModelForm()

                else:
                    messages.error(request, f'Vechile No {vechile_no} or Permit No {permit_no} is Exist')
                    

    else:
        form_ins=RC_ModelForm(initial={'vechile_no':statecode.upper(),'permit_no':statecode.upper()})

    context={
        'form_ins':form_ins,'title':'RC-REG','statecode':statecode,
        'time':time,'date':date,'header':'RC Registration'
     
    }
    return render(request,'App_1//registration.html',context)


# ----------------------------------[ OFFENCE/FINE REGISTER VIEWS]---------------------------------

@login_required(login_url=LOGIN_URL)
def fine_register(request):

    dt=datetime.now()
    current_time=dt 
    if request.method=='POST':
        form_ins=Fine_ModelForm(request.POST)

        if form_ins.is_valid():
            model_obj=RCRegister.objects.all()
            vechile_no=form_ins.cleaned_data.get('vechile_no')
            fine=form_ins.cleaned_data['fine']
            fine=str(fine)


            # for i in list_fine_charge:
            #     if i[1]==str(fine)

            print(f'Entered vechile no {vechile_no} for FINE')
            print('Validation Done')
            vechile_no=form_ins.cleaned_data['vechile_no']
  
            if RCRegister.objects.all().filter(vechile_no__iexact=vechile_no).exists():
                for off,chrg in dict_challan.items():
                    print(fine, off, chrg)
                    if (off) == (fine):
                        print('yes GOTCHA!!!')
                        paid_upto = curr_date + relativedelta(months=2)
                        print('paid upto',paid_upto)
                        
                        model_obj=VechileFine(vechile_no=vechile_no.upper(),fine=fine,charge=chrg,offence_on=current_time, paid_upto=paid_upto)
                        model_obj.save()
                        messages.success(request, f'Fine/Challan is added to {vechile_no} for {fine} of Rs.{chrg}')
                        form_ins=Fine_ModelForm()
                    
                    
            else:
                messages.warning(request, f' Entered vechile {vechile_no.upper()} is not registered in RTO office')
                form_ins=Fine_ModelForm(initial={'vechile_no':'MH'})

                    

    else:
        form_ins=Fine_ModelForm(initial={'vechile_no':'MH'})

    context={
        'form_ins':form_ins,'title':'FINES|CHALLAN',
        'time':current_time,'date':date,'header':'Challan Registration'
     
    }
    return render(request,'App_1//registration.html',context)



    