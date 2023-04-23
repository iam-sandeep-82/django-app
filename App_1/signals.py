from django.db.models.signals import ( pre_save, post_save, pre_delete, post_delete, pre_init, post_init)
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.models import User
from .models import *
from django.dispatch import receiver
from django.contrib.auth.models import Permission,Group
from django.contrib import messages
from .models import *
from django.core.cache import cache
#sender
#event which trigger messsage
#reciever

@receiver(post_init, sender=User)
def instance_creation(sender, instance,**kwargs):
    pass
    # print('---------------S-POST INIT-----------------------')


@receiver(pre_save, sender=User)
def pre_signal_testing(sender,instance, **kwargs):
    pass
    # print('---------------S-PRE SAVE-----------------------')


@receiver(post_save,sender=User)
def post_signal_testing(sender, instance, created, **kwargs):
    if created:
        print(instance.has_perm('App_1.delete_VechileFine'))
        print(f'New Account is created {instance.first_name}')   
    # print('---------------S-POST SAVE-----------------------')

    
@receiver(user_logged_in)
def user_logged_in(sender,user,request,**kwargs):
    ct=cache.get_or_set('no_of_attempts',0,360,version=user.pk)
    ct+=1
    cache.set('no_of_attempts',ct,360,version=user.pk)
    print('---------------S-USER-LOGIN-----------------------')

    request.session['client_ip']=request.META.get('REMOTE_ADDR')


@receiver(user_logged_out, sender=User)
def do_stuff(sender, user, request, **kwargs):
    messages.success(request, f'Sucessfully Logout!!!')
    print('---------------S-USER-LOGOUT-----------------------')

@receiver(post_save, sender=Moderator)
def do_stuff(sender, instance, created, **kwargs):
    get_group=Group.objects.get(name='MODERATOR')
    instance.groups.add(get_group)
    print(f'user {instance.username} is save {get_group}')

    