from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm) 
from .forms import *
from .Auth_Forms import *
from .models import *
from django.contrib import messages
from dateutil.relativedelta import relativedelta
from django.urls import reverse, reverse_lazy, resolve
from .choice import dict_challan
from .Auth_Forms import *
from Base.settings import *
from django.contrib.auth.models import Permission,Group
from django.contrib.auth.decorators import login_required
from .utility import *
from django.core.cache import cache
from django.template.response import TemplateResponse
import datetime as dt
from django.views.generic.base import View
from django.views.generic import (TemplateView, RedirectView, ListView, DetailView)
# from email.message import EmailMessage #django prefer
from django.core.mail import EmailMessage #django prefer
import smtplib
from twilio.rest import Client 
import requests,json



def signup(request):
    dt=datetime.now()
    time=dt 

    if request.method=='POST':
        form_ins=SignUpForm(request.POST)

        if form_ins.is_valid():

            print('Validation Done')
            first_name=form_ins.cleaned_data['first_name']
            user=form_ins.save(commit=False)
            user.is_staff=True
            user=form_ins.save(commit=True)
            get_group=Group.objects.get(name='RTO_OFFICERS')
            user.groups.add(get_group)
            # request.session['login_user']=user.username
            messages.success(request, f'User {first_name} is Succesfully Register!')
            return redirect(LOGIN_URL)

    else:
        form_ins=SignUpForm()
        


    context={
        'form_ins':form_ins,'title':'__RC-REGISTER__',
        'time':time,'date':date,'header':'RTO Officer SignUp',
        'cred':[uname,first,last,email]
     
    }
    return render(request,'App_1//registration.html',context)
    

def getlogin(request):

    if request.method=='POST':
        form_ins=LoginForm(request=request,data=request.POST)
        username=request.POST['username']

        if form_ins.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            active_user=authenticate(username=username,password=password)
            request.session['active_user']=active_user.id
            if active_user is not None:
                return redirect(reverse('App_1:GETOTP', kwargs={ 'id': active_user.id }))

                
        else:
            messages.success(request, f'Invalid User or Password.')
            return HttpResponseRedirect(reverse('App_1:HOMEPAGE'))
            
    else:
        form_ins=LoginForm()

    context={
        'form_ins':form_ins,'title':'__SIGNUP__'
    }
    return TemplateResponse(request,'App_1//authenticate_form.html',context)


class get_otp_verify(View):
    id=''
    #global gen_otp it uses [get_otp_verify and verify_otp] class
    gen_otp=otp_gen()
    def get(self,request,id):
        # ----------------------------------------------------

        # ----------------------------------------------------
        
        user=User.objects.get(id=id)
        get_mail=user.email

        EMAIL=os.getenv('HOST')
        PASS=os.getenv('PASS')
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo() # Can be omitted
        server.starttls() # Secure the connection

        server.ehlo() # Can be omitted
        

        my_mess=EmailMessage('VEHinfo Confirmation OTP',
                    'OTP:- '+ str(self.gen_otp) +'. \nCurrent OTP is sensitive. Please don`t share with anyone.', #content
                    EMAIL, #receipent 
                    [get_mail, 'YOURMAIL@.COM'], #list_receiver
                    ['YOURMAIL@.COM'],   #cc
                    reply_to=['another@example.com'],  #if query then email us
                    headers={'Message-ID': 'foo'})


 
        print('START')
        if server.login(EMAIL,PASS):
            print('Server is sending message')
            print(f'Gen-OTP {get_otp_verify.gen_otp}')
            my_mess.send()
            # server.send_message(my_mess)
        else:
            print('INVALID')
        server.quit()
        print('END')

        form_obj=OtpForm()
        context={
            'form':form_obj
        }
        return render(request,'App_1/otp/otp_input.html',context=context)


class otp_verify(get_otp_verify,View):
    def post(self,request):
        print(otp_verify.gen_otp)
        form_obj=OtpForm(request.POST)
        if form_obj.is_valid():
            get_otp=form_obj.cleaned_data.get('otp')
        
            if int(get_otp) == int(otp_verify.gen_otp):
                get_active_user_id=request.session.get('active_user')
                print(get_active_user_id)
                active_user=User.objects.get(id=get_active_user_id)
                print(active_user)
                messages.success(request, f'Login Successfull {active_user.username}!')
                login(request,active_user)
                user_ip=request.META['REMOTE_ADDR']


                return redirect(reverse('App_1:HOMEPAGE'))
            else:
                return HttpResponse('<h1>NOT VALID OTP :(')



@login_required(login_url=LOGIN_URL)
def getlogout(request): 
    logout(request)
    return HttpResponseRedirect(HOME_URL)    #using home url 
    # return HttpResponseRedirect(reverse('App_1:HOMEPAGE'))  

# password change form using old password as a authentication
@login_required(login_url=LOGIN_URL)
def setpassword(request):

    if request.method=='POST':
        form_ins=PasswordChangeForm(user=request.user,data=request.POST)

        if form_ins.is_valid():
            form_ins.save()
            update_session_auth_hash(request,form_ins.user)
            messages.success(request,'Now, you are password is changed')
            return HttpResponseRedirect(HOME_URL)   
        
    else:
        form_ins=PasswordChangeForm(user=request.user)

    context={
        'form_ins':form_ins,'title':'__PSWRDCHNG__'
    }
    return render(request,'App_1//registration.html',context)

        
# SetPasswordForm form using gmail or username as a authentication

def setpassword_2(request):
    if request.method=='POST':
        form_ins=PasswordChangeForm(user=request.user,data=request.POST)
        if form_ins.is_valid():
            return HttpResponseRedirect(HOME_URL)   
    else:
        form_ins=PasswordChangeForm(user=request.user)
    context={
        'form_ins':form_ins,'title':'__PSWRDCHNG__'
    }
    return render(request,'App_1//registration.html',context)





    
    