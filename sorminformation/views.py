from django.shortcuts import render
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from sorminformation.models import *
from sormcontrol.models import *

# Create your views here.






@login_required
def sormtypeinformation(request):
    args = {}
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    args['Type_information_all'] = TypeInformation.objects.order_by('name')

    return render(request, 'sorminformation/sormtypeinformation.html', args)


@login_required
def sormcreatetypeinformation(request):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    user_group = u.groups
    if (user_group.filter(name='create_object').exists()):
        if (request.POST):
            newtypeinformation = TypeInformation(name = request.POST['type_information_name'])
            newtypeinformation.save()
            return redirect("/information/type_information")
        else:
            return render(request, 'sorminformation/sormcreatetypeinformation.html', args)

    else:
        return redirect("/information/type_information")


@login_required
def sormdeletetypeinformation(request, typeinformation_id):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    try:
        typeinformation = TypeInformation.objects.get(id=typeinformation_id)
    except TypeInformation.DoesNotExist:
        return redirect("/information/type_information")

    user_group = u.groups
    if (user_group.filter(name = 'delete_object').exists()):
        typeinformation.delete()
    return redirect("/information/type_information")


@login_required
def sorminformation(request):
    args = {}
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    args['Information_all'] = InformationAsset.objects.order_by('name')

    return render(request, 'sorminformation/sorminformation.html', args)



@login_required
def sormcreateinformation(request):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    user_group = u.groups
    if (user_group.filter(name='create_object').exists()):
        if (request.POST):
            newinformation = InformationAsset(name = request.POST['information_name'], type_information= TypeInformation.objects.get(id= request.POST['type_information']),
                                              category_information=CategoryInformation.objects.get(id= request.POST['category_information']),
            protectionLevel_information = ProtectionLevelInformation.objects.get(id = request.POST['levelprotection_information']))
            newinformation.save()
            return redirect("/information/information")
        else:
            args['Type_information_all'] = TypeInformation.objects.order_by('name')
            args['Category_information_all'] = CategoryInformation.objects.order_by('name')
            args['levelprotection_information_all'] = ProtectionLevelInformation.objects.order_by('name')
            return render(request, 'sorminformation/sormcreateinformation.html', args)

    else:
        return redirect("/information/information")


@login_required
def sormdeleteinformation(request, information_id):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    try:
        information = InformationAsset.objects.get(id=information_id)
    except InformationAsset.DoesNotExist:
        return redirect("/information/information")

    user_group = u.groups
    if (user_group.filter(name = 'delete_object').exists()):
        information.delete()
    return redirect("/information/information")

@login_required
def sormeditinformation(request, information_id):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    try:
        information = InformationAsset.objects.get(id=information_id)
    except InformationAsset.DoesNotExist:
        return redirect("/information/information")
    user_group = u.groups
    if (user_group.filter(name = 'delete_object').exists()):
        if (request.POST):
            newenvobject_id = request.POST.getlist('newenvobject')
            newclasscontrols_id = request.POST.getlist('newclass')
            information.envobject_information.clear()
            information.information_class_controls.clear()
            information.save()
            for x in newenvobject_id:
                information.envobject_information.add(EnvironmentObject.objects.get(id=x))
            information.save()
            for x in newclasscontrols_id:
                information.information_class_controls.add(ClassControl.objects.get(id=x))
            information.save()
            return redirect("/information/information")
        args['information'] = InformationAsset.objects.get(id = information_id)
        args['envobject_all'] = EnvironmentObject.objects.order_by('name')
        args['classcontrols'] = ClassControl.objects.order_by('name')
        return render(request, 'sorminformation/sormeditinformation.html', args)
    return redirect("/information/information")


@login_required
def sormcategoryinformation(request):
    args = {}
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    args['Category_information_all'] = CategoryInformation.objects.order_by('name')

    return render(request, 'sorminformation/sormcategoryinformation.html', args)


@login_required
def sormcreatecategoryinformation(request):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    user_group = u.groups
    if (user_group.filter(name='create_object').exists()):
        if (request.POST):
            newcategoryinformation = CategoryInformation(name = request.POST['category_name'])
            newcategoryinformation.save()
            return redirect("/information/category_information")
        else:
            return render(request, 'sorminformation/sormcreatecategoryinformation.html', args)

    else:
        return redirect("/information/category_information")


@login_required
def sormdeletecategoryinformation(request, category_information_id):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    try:
        categoryinformation = CategoryInformation.objects.get(id=category_information_id)
    except CategoryInformation.DoesNotExist:
        return redirect("/information/category_information")

    user_group = u.groups
    if (user_group.filter(name = 'delete_object').exists()):
        categoryinformation.delete()
    return redirect("/information/category_information")







@login_required
def sormcreateenvobject(request):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    user_group = u.groups
    if (user_group.filter(name='create_object').exists()):
        if (request.POST):
            newenvobject = EnvironmentObject(name = request.POST['envobject_name'])
            newenvobject.save()
            return redirect("/information/envobject")
        else:
            return render(request, 'sorminformation/sormcreateenvobject.html', args)

    else:
        return redirect("/information/envobject")


@login_required
def sormenvobject(request):
    args = {}
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    args['Envobject_all'] = EnvironmentObject.objects.order_by('name')
    return render(request, 'sorminformation/sormenvobject.html', args)



@login_required
def sormdeleteenvobject(request, envobject_id):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    try:
        envobject = EnvironmentObject.objects.get(id=envobject_id)
    except EnvironmentObject.DoesNotExist:
        return redirect("/information/envobject")

    user_group = u.groups
    if (user_group.filter(name = 'delete_object').exists()):
        envobject.delete()
    return redirect("/information/envobject")



@login_required
def sormlevelprotectioninformation(request):
    args = {}
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    args['Levelprotection_all'] = ProtectionLevelInformation.objects.order_by('name')
    return render(request, 'sorminformation/sormlevelprotectioninformation.html', args)


@login_required
def sormeditinformation(request, information_id):
    args = {}
    args.update(csrf(request))
    u = User.objects.get(username=auth.get_user(request).username)
    args['username'] = u.username
    try:
        information = InformationAsset.objects.get(id=information_id)
    except InformationAsset.DoesNotExist:
        return redirect("/information/information")
    user_group = u.groups
    if (user_group.filter(name = 'delete_object').exists()):
        if (request.POST):
            newenvobject_id = request.POST.getlist('newenvobject')
            newclasscontrols_id = request.POST.getlist('newclass')
            information.envobject_information.clear()
            information.information_class_controls.clear()
            information.save()
            for x in newenvobject_id:
                information.envobject_information.add(EnvironmentObject.objects.get(id=x))
            information.save()
            for x in newclasscontrols_id:
                information.information_class_controls.add(ClassControl.objects.get(id=x))
            information.save()
            return redirect("/information/information")
        args['information'] = InformationAsset.objects.get(id = information_id)
        args['envobject_all'] = EnvironmentObject.objects.order_by('name')
        args['classcontrols'] = ClassControl.objects.order_by('name')
        return render(request, 'sorminformation/sormeditinformation.html', args)
    return redirect("/information/information")