from django.shortcuts import render

def index(request):
    return render(request,'pages/index.html')

def contact(request):
    return render(request, 'pages/contact.html')

def services(request):
    return render(request, 'pages/services.html')