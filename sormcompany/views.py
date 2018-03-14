from django.shortcuts import render
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from sormcompany.models import *
# Create your views here.


@login_required
def sormcompanymain(request):
    args = {}
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    args['Company_all'] = Company.objects.all()


    return render(request, 'sormcompany/sormcompanymainpage.html', args)



@login_required
def sormdeletecompany(request, company_id):
    args = {}
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    args['Company_all'] = Company.objects.all()

    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        return redirect("/company/main")

    user_group = u.groups
    if (user_group.filter(name = 'delete_object').exists()):
        company.delete()
    return redirect("/company/main")

@login_required
def sormcreatecompany(request):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    user_group = u.groups
    if (user_group.filter(name='create_object').exists()):
        if (request.POST):
            newcompany = Company(name = request.POST['company_name'], type_company=TypeCompany.objects.get(id= request.POST['company_type']))
            newcompany.save()
            return redirect("/company/main")
        else:
            args['Company_types'] = TypeCompany.objects.all()
            return render(request, 'sormcompany/sormcreatecompany.html', args)

    else:
        return redirect("/company/main")