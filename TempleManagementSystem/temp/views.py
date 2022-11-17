from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'temp/publicindex.html')

def devotee(request):
    return render(request,'temp/devoteeindex.html')

def adminhome(request):
    return render(request,'temp/adminindex.html')