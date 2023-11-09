from django.shortcuts import render

# Create your views here.
def audi(request):
    return render(request,'audi.html' )

def hobbies(request):
    return render(request,'hobbies.html' )

def movies(request):
    return render(request,'movies.html' )

def royalenfield(request):
    return render(request,'royalenfield.html' )
