import random
# import time
# import smtplib
# import os
# from email.message import EmailMessage
# import imghdr
# from .models import *
import datetime as dt
std_dt=dt.datetime.now()
import json

# python_dict={'Country':['Netherland','spain','turkey','germany','uk','sweden','norway'],'lake':['suez canal','mochigan lake','victoria fall','nigara fall']}
# python_dict_2={'Country':'Netherland','lake':'victoria fall'}

# parse_data=json.dumps(python_dict)
# print(parse_data)

# x=json.loads(parse_data)
# print(x.get('Country'))

# def captchaGen():
#     range_rand=[x for x in range(10)]
#     captcha=''
#     for num in range(1,7):
#         curr_captcha=str(random.choice(range_rand))
#         captcha+=(curr_captcha)
#     captcha=int(captcha)
#     return captcha

# def mailSender(request,receiver):
#     EMAIL='sandysingh9449@gmail.com'
#     PASS='rtgaeehtjdotnufb'

#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo() # Can be omitted
#     server.starttls() # Secure the connection
#     server.ehlo() # Can be omitted

#     msg=EmailMessage()
#     msg['from']=EMAIL
#     msg['to']=receiver
#     msg['subject']='Testing Message from PYTHON'
#     OTP=captchaGen()
#     print(f'-------------------{OTP}-----------------------')
#     msg.set_content(f'Your OTP for login is {OTP}. Don`t share with anyone')

    # main_dir='C:\\Users\\Sandy\\Downloads\\allwall'

    # images=[]

    # for fold,subfold,files in os.walk(main_dir):
    #     for f in files:
    #         images.append(main_dir + '\\' + f)

    # for img in images:
    #     image=open(img,'rb')
    #     image_data=image.read()
    #     file_type=imghdr.what(image.name)  
        # msg.add_attachment(image_data,'image',file_type)

    # print('START')
    # if server.login(EMAIL,PASS):
    #     print('Server is sending message')
    #     server.send_message(msg)
    # else:
    #     print('INVALID')
    # server.quit()
    # print('END')
    # return OTP


# MH 43 2021 08 4041
gen_dl=''

def dl_gen(state,rto,year=std_dt.year):
    global gen_dl
    last_6_digit=random.randint(0,200000)
    gen_dl=str(state) + str(rto)+ str(year) + str(last_6_digit)
    return gen_dl



def otp_gen():
    range_rand=[x for x in range(10)]
    otp=''
    for num in range(1,7):
        curr_otp=str(random.choice(range_rand))
        otp+=(curr_otp)
    otp=int(otp)
    return otp