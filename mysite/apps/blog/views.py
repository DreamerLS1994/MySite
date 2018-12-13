from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    #return HttpResponse("Hello World! From Jerry Coding")
    return render(request, 'blog/index.html')
