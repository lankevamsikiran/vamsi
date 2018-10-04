from django.http import HttpResponse
from django.shortcuts import 

def homepage(request):
    return render(request, "home.html", {'A':'lankevamsikiran'})
