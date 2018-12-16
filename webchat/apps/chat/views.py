from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login_view(request):
    #return HttpResponse("Hello World! From Jerry Coding")
    return render(request, 'chat/index.html')
