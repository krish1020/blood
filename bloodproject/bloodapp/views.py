from django.shortcuts import render
from . models import place


# Create your views here.
def index(request):
    obj=place.objects.all()
    # obj1=blood.objects.all()
    return render(request,'index.html',{'result':obj})