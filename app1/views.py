from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a':500,'b':2000,'c':4000}
    return render(request,'conditions.html',d)