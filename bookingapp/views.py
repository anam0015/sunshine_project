from django.shortcuts import render

# Create your views here.

def sunshine_view(request):
    return render(request,'bookingapp/index.html')
