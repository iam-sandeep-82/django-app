from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,User
from django.core.exceptions import ValidationError
from .models import *


class SignUpForm(UserCreationForm):
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-allfield','placeholder':'kuchbhichalega'}),label='Password',required=True,error_messages={'required':'Enter Password'})
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-allfield','placeholder':'kuchbhichalega'}),label='Confirm Password',required=True,error_messages={'required':'Confirm Password'})

    class Meta:
        model=Officer
        fields=['username','first_name','last_name','email']
        labels={'username':'Username','first_name':'First Name','last_name':'Last Name','email':'Email Id'}
        
        
        # error_message={'required':'Enter Password'}
        widgets={ 
            'username' : forms.TextInput(attrs={'class':'form-control form-allfield','placeholder':'kuchbhichalega'}),
            'first_name': forms.TextInput(attrs={'class':'form-control form-allfield','placeholder':'kuchbhichalega'}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-allfield','placeholder':'kuchbhichalega'}),
            'email': forms.EmailInput(attrs={'class':'form-control form-allfield','placeholder':'kuchbhichalega'}),
            
            }
    
    def clean(self):
        cleaned_data=super().clean()
        get_email=self.cleaned_data.get('email')
        get_name=User.objects.all().filter(email__iexact=get_email)

        if get_name.exists():
            forms.ValidationError('Entered Email is Exists')
        
    
class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'username','placeholder':'Username*'}),required=True,error_messages={'required':'Enter Username'})
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'password','placeholder':'Password*'}),required=True,error_messages={'required':'Enter Password'})



class OtpForm(forms.Form):
    otp=forms.CharField(widget=forms.TextInput(attrs={'class':"otp-field" ,'placeholder':"Enter OTP"}),required=True, error_messages={'required':'Please Enter OTP. OTP has been sent to your registered mail id.'})


        