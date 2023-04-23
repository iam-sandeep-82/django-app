from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .import Auth_Views
from django.contrib.auth import views as auth_views
from .Auth_Forms import *

app_name='App_1'

urlpatterns=[

    path('', views.home, name='HOMEPAGE'), #  url(r'^$', views.home, name='HOMEPAGE'),
# -----------------------[LIST_ALL_DL_RC]---------------------
    path('dl-users/', views.dl_allusers, name='DL_ALLUSERS'), 
    path('rc-users/', views.rc_allusers, name='rc_ALLUSERS'), 

# --------------------------[SEARCH URLS]-----------------------
    path('dl-search/', views.dl_search, name='SEARCH'),
    path('rc-search/', views.rc_search, name='RC-SEARCH'),
    path('my-fines', views.fine_search, name='FINE-SEARCH'),

# ---------------------------[REGISTRATION URLS]--------------------------
    path('dl-register/<str:statecode>/', views.dl_registration, name='DL_REGISTER'), 
    path('rc-register/<str:statecode>/', views.rc_register, name='RC_REGISTER'),
    path('fine-register', views.fine_register, name='FINE_REGISTER'),
    
    # path('rc-search', views.rc_register, name='')
    # path('search/', views.dl_search, name='SEARCH')

  
# ---------------------------[User Authentication URLS]-------------------------- 
    path('login/', Auth_Views.getlogin, name='LOGIN'),
    path('get_otp/<int:id>/', Auth_Views.get_otp_verify.as_view(), name='GETOTP'),
    path('verify_otp/', Auth_Views.otp_verify.as_view(), name='CONFIRMOTP'),
    path('logout/', Auth_Views.getlogout, name='LOGOUT'),
    path('signup/', Auth_Views.signup, name='SIGNUP'),
    path('password/', Auth_Views.setpassword_2, name='SETPASSWORD'),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='App_1/pswrd_temp/password_reset_form.html',from_email='Dyanmo@Site.com'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='App_1/pswrd_temp/password_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='App_1/pswrd_temp/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='App_1/pswrd_temp/password_reset_confirm.html'),name='password_reset_complete'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)