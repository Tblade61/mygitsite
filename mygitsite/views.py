from django.shortcuts import render,redirect

def showdata(request):
    return render(request,'home.html')

def home(request):
    print('Home')
    return render(request,'home.html')

def about(request):
    print('About')
    return render(request,'about.html')