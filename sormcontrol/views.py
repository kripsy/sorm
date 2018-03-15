from django.shortcuts import render
from django.shortcuts import render
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from sormcontrol.models import *
# Create your views here.





@login_required
def sormcreatecontrol(request):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    user_group = u.groups
    if (user_group.filter(name='create_object').exists()):
        if (request.POST):
            newcontrol = Control(name = request.POST['control_name'], type_realization=TypeRealization.objects.get(id= request.POST['type_realization']))
            newcontrol.save()
            return redirect("/control/control")
        else:
            args['Type_realization_all'] = TypeRealization.objects.order_by("name")
            return render(request, 'sormcontrol/sormcreatecontrol.html', args)

    else:
        return redirect("/control/control")



@login_required
def sormcontrol(request):
    args = {}
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    args['Control_all'] = Control.objects.order_by('name')

    return render(request, 'sormcontrol/sormcontrol.html', args)



@login_required
def sormdeletecontrol(request, control_id):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    try:
        control = Control.objects.get(id=control_id)
    except Control.DoesNotExist:
        return redirect("/information/type_information")

    user_group = u.groups
    if (user_group.filter(name = 'delete_object').exists()):
        control.delete()
    return redirect("/control/control")