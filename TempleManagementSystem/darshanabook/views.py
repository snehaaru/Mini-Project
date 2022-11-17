from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from darshanabook.models import Darshanabook
from darshana.models import Darshana
from ureg.models import Ureg

# Create your views here.
# def darshanabook(request):
#     if request.method=="POST":
#         obj=Darshanabook()
#         obj.day=request.POST.get('day')
#         obj.date=request.POST.get('dt')
#         obj.time=request.POST.get('tim')
#         obj.ppls=request.POST.get('ppl')
#         obj.name=request.POST.get('n1')
#         obj.address=request.POST.get('ad1')
#         obj.id_proof=request.POST.get('prv')
#         obj.id_number=request.POST.get('prv_no')
#         obj.phone_no=request.POST.get('phn')
#         obj.date_of_birth=request.POST.get('dob')
#         obj.star=request.POST.get('str')
#         # obj.u_id=request.POST.get('u')
#         obj.save()
#
#
#     return render(request, 'darshanabook/darshanabook.html')

def darshanabook(request):
    if request.method=='POST':
        obj=Darshanabook()
        obj.name=request.POST.get('n1')
        obj.date=request.POST.get('dt')
        obj.time=request.POST.get('tim')
        obj.ppls=request.POST.get('ppl')
        obj.address=request.POST.get('ad1')
        # obj.id_proof=request.POST.get('prv')
        myfile = request.FILES['prv']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.id_proof=myfile.name
        obj.id_number=request.POST.get('prv_no')
        obj.phone_no=request.POST.get('phn')
        obj.date_of_birth=request.POST.get('dob')
        obj.star=request.POST.get('str')
        obj.gender=request.POST.get('gender')
        obj.save()
    return render(request,'darshanabook/darshanabook.html')

def viewbookdarshan(request):
    obj1=Darshanabook.objects.all()
    context={
        'w':obj1
    }

    return render(request,'darshanabook/viewdarshanabook.html',context)