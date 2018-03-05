from django.shortcuts import render

# Create your views here.



def mainasset(request):


    return render(request, 'sormasset/mainasset.html', locals())