from django.shortcuts import render
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import Group
# Create your views here.


def sormauth(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('full name input', '')
        password = request.POST.get('password input', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('sormauth/sormauth.html', args)

    else:
        return render_to_response('sormauth/sormauth.html', args)

@login_required
def sormlogout(request):
    
    logout(request)
    return render_to_response('sorm/mainsorm.html')

@login_required
def mainpage(request):
    args = {}
    user = User.objects.get(username = auth.get_user(request).username)
    args['username'] = user.username
    args['email'] = user.email
    if user.groups.all().exists():
        groups_help = user.groups.values_list('name',flat=True)
        args['group'] = []
        for x in groups_help:
            args['group'].append(x)

    else:
    # Action if not existing
        args['group'] = "None"
    return render_to_response('sormauth/mainpage.html', args)
