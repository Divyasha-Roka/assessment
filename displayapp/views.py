from django.shortcuts import render
from .models import Display
# Create your views here.
def Display_view(request):
    data = Display.objects.all()
    return render( request , 'displayapp/food.html' , {'data':data} )