from django.shortcuts import render

# Create your views here.


def sormauth(request):
    return render(request, 'sormauth/sormauth.html', locals())




def mainpage(request):
    return render(request, 'sormauth/mainpage.html', locals())