from django.forms import ModelForm
from django import forms
from .models import *
from .choice import *
from datetime import *
import re


current_date=datetime.now()

class DateInput(forms.DateInput):
    input_type='date' 

# ------------------------------[DL-SEARCH-FORM]-----------------------------------
class Search_ModelForm(forms.Form):
    dl=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'Search'}),label='Driving License No',help_text='DL-Format MH432021000000',required=True,error_messages={'required':'drving License should not be blank'})
    
    def clean_dl(self):
        dl_no=self.cleaned_data['dl']
        re_obj=re.compile(r'^(\w{2})(\d{12})$')
        out=re_obj.search(dl_no)

        if out==None:
            print('Error')
            raise forms.ValidationError('Ensure the format of license is correct')
        return dl_no
    
# ------------------------------[RC-SEARCH-FORM]-----------------------------------

class RC_Search_Form_Api(forms.Form):

    vechile_no=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'Search'}),label='Vechile No',help_text='Format:- MH43AA0000',required=True,error_messages={'required':'Vechile No should not be blank'})
    
    def clean_vechile_no(self):
        vechile_no=self.cleaned_data['vechile_no']
        re_obj=re.compile(r'^[A-Z|a-z]{2}\s?[0-9]{1,2}\s?[A-Z|a-z]{0,3}\s?[0-9]{3,4}$')
        out=re_obj.search(vechile_no)

        if out==None:
            print('Error')
            raise forms.ValidationError('Ensure the format of Vechile No is correct')
        return vechile_no
    
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ [LICENSE REG] +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class LR_ModelForm(forms.ModelForm):

    owner=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-allfield','placeholder':'kuchbhichalega'}),label='First Name',required=True,error_messages={'required':'Owner Name should not be blank'})
    surname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-allfield','placeholder':'kuchbhichalega'}),label='Middle Name',required=True,error_messages={'required':'Middle Name should not be blank'})
    vechile_class = forms.ChoiceField(choices = list_of_vech_class, help_text="Class of Vechile", widget=forms.Select(),error_messages={'required':'Please Select the Vechile Class'})
    # expiry=forms.DateField(widget=DateInput(attrs={'class':'expiry-field'})) 

    class Meta:
        model=LicenseRegistration
        fields=['owner','surname','vechile_class','last_payment']
    
    def clean(self):
        cleaned_data=super().clean()
        # ----GETTING THE DATA---
        get_owner_name=self.cleaned_data.get('owner')
        get_cov=self.cleaned_data['vechile_class']

        if get_cov=='Class':
            raise forms.ValidationError('Select the Class of Vechile')

    #    if get_last_payment=='Select RTO office':
    #        raise forms.ValidationError('Select Current RTO office')



# ++++++++++++++++++++++++++++++++++++++++++++++++++++ [RC REG] +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class RC_ModelForm(forms.ModelForm):

    vechile_no=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-allfield','placeholder':'anyexample'}),label='Vechile No',help_text='Format MH43AQ000',required=True,error_messages={'required':'vechile No should not be blank'})
    owner=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-allfield','placeholder':'kuchbhichalega'}),label='Owner Name',required=True,error_messages={'required':'Owner Name should not be blank'})
    fuel_type = forms.ChoiceField(choices = list_fuel_type, help_text="Fuel Type", widget=forms.Select(),required=True,error_messages={'required':'Please Select the Fuel Type'})
    reg_date=forms.DateField(widget=DateInput(attrs={'class':'doi-field'}),help_text="Registration on",initial=current_date,error_messages={'required':'Select the Date'},required=True)
    insurance=forms.DateField(widget=DateInput(attrs={'class':'dob-field'}),help_text="Insurance issue on",error_messages={'required':'Select the Date of Insurance'},required=True) 
    permit_no=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-allfield','placeholder':'anyexample'}) , label='Permit No',help_text='Format MH43CCAUTO20185309',required=True,error_messages={'required':'Permit No should not be blank'})
    # permit_expiry=forms.DateField(widget=DateInput(attrs={'class':'expiry-field'}),help_text="Permit issue on",error_messages={'required':'Select the Date of Permit Expiry'},required=True) 
    
    
    class Meta:
        model=RCRegister
        fields=['vechile_no','rto_office','fuel_type','owner','reg_date','insurance','permit_no']



    def clean(self):      
        cleaned_data=super().clean()
        # ----GETTING THE DATA---
        permit_no=self.cleaned_data['permit_no']
        vechile_no=self.cleaned_data['vechile_no']
        fuel_type=self.cleaned_data['fuel_type']
        # rto_office=self.cleaned_data['rto_office']
        
        # ----REGEX FORMAT--
        per_obj=re.compile(r'^(\w{2}\d{2,3})(\w{2})?(\w{2,4})(\d{8,10})')
        vec_obj=re.compile(r'^[A-Z|a-z]{2}\s?[0-9]{1,2}\s?[A-Z|a-z]{0,3}\s?[0-9]{3,4}$')
        out1=per_obj.search(permit_no)
        out2=vec_obj.search(vechile_no)
        
        # ----CHECKING ON VALIDATION--
        if out2==None:
            print('Vechile No Error')
            raise forms.ValidationError('Ensure the format & Vechile No is correct or should not be blank')

        # if rto_office=='Select RTO office':
        #     print('Select RTO OFFICE Error')
        #     raise forms.ValidationError('Please select the RTO office')

        if fuel_type=='Select Fuel Type':
            print('Select Fuel Type Error')
            raise forms.ValidationError('Please select the Fuel Type')

        if out1==None:
            print('Permit Error')
            raise forms.ValidationError('Ensure the format & Permit No is correct or not be Blank')
        

class Fine_ModelForm(forms.ModelForm):

    vechile_no=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-allfield','placeholder':'anyexample'}),label='Vechile No',help_text='Format MH43AQ000',required=True,error_messages={'required':'Vechile No should not be blank'})
    fine = forms.ChoiceField(choices = list_fine_charge, help_text='Select which Offence', widget=forms.Select(),required=True,error_messages={'required':'Select the Offence'})
    offence_on=forms.DateField(widget=DateInput(attrs={'class':'offence-on'}),help_text="Offence on",required=True,initial=current_date,error_messages={'required':'Select the Date of offence on'})
    state = forms.ChoiceField(choices = list_states, help_text='Select which Offence', widget=forms.Select(),required=True,error_messages={'required':'Select the State'})
   

    class Meta:
        model=VechileFine
        fields=['vechile_no','offence_on','fine','state']
        error_messages={'vechile no': {'required':'This is error message'}}

    def clean(self):      
        cleaned_data=super().clean()
        vechile_no=cleaned_data['vechile_no']
        offence_on=cleaned_data['offence_on']
        fine=cleaned_data['fine']
        state=cleaned_data['state']


        vec_obj=re.compile(r'(\w\w)(\d\d)(\w|\w\w)(\d{3,4})')
        out=vec_obj.search(vechile_no)

        if out==None:
            print('Vechile format Error')
            raise forms.ValidationError('Ensure the format of Vechile No is correct')
        
        if fine=='select':
            print('offence Error')
            raise forms.ValidationError('Select the offence type')
        
        if state=='select':
            print('state Error')
            raise forms.ValidationError('Select the State')
        

    
  



       
    