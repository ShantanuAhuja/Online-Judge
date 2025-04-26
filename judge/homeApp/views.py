from django.shortcuts import render

# Create your views here.

def renderHomeApi(request):
    return render(request, 'homePage.html')