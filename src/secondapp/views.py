from django.shortcuts import render,HttpResponse

# Create your views here.
def thirdview(request):
    return render(request,'third.html')
def fourthview(request):
    return render(request,'fourth.html')