from django.template.response import TemplateResponse
from django.shortcuts import HttpResponse
import random

class MaintainenceMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        text='Site is under Maintainence, please Retry after later'
        x=TemplateResponse(request,'App_1\\Maintainence.html',{'text':text})
        return x.render()

    # def process_view(request,*args,**kwargs):
    #     return HttpResponse('Process view is call after the MAIN VIEW IS CALL')