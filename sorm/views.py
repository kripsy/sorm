from django.shortcuts import render
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def main(request):
    args = {}
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
#    args['username'] = auth.get_user(request).username
#    args['group'] = auth.get_user(request).groups

    return render(request, 'sorm/mainsorm.html', args)