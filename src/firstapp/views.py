from django.shortcuts import render,HttpResponse

# Create your views here.
def firstview(request):
    return render(request,'first.html')
def secondview(request):
    return render(request,'second.html')
