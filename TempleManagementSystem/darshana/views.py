from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from darshana.models import Darshana
from  darshanabook.models import Darshanabook
from ureg.models import Ureg

# Create your views here.

def darshanaadd(request):
    if request.method == "POST":
        obj = Darshana()
        obj.day = request.POST.get('day')
        obj.time = request.POST.get('tim')
        obj.date = request.POST.get('dt')
        obj.desc = request.POST.get('desc')
        obj.type = request.POST.get('spcl')
        obj.price=request.POST.get('pr')
        obj.save()

    return render(request, 'darshana/dharshanatime.html')


def darshanaview(request):
    obj=Darshana.objects.filter(type='vazhipade')
    context={
        'a' :obj
    }


    return render(request, 'darshana/pooja.html',context)

def vazhipad_view(request):
    obj=Darshana.objects.filter(type='pooja')
    context={
        'a' :obj
    }


    return render(request, 'darshana/vazhipad.html',context)


def book(request):
    # obj=Darshana.objects.get(did=idd)
    # obk=Ureg.objects.all()
    # context={
    #     'a':obj,
    #     'w':obk
    # }
    if request.method == "POST":
        obj = Darshanabook()
        obj.day = request.POST.get('day')
        obj.date = request.POST.get('dt')
        obj.time = request.POST.get('tim')
        obj.ppls = request.POST.get('ppl')
        obj.u_id=request.POST.get('u')
        obj.address=request.POST.get('ad1')
        obj.gender=request.POST.get('gender')
        obj.date_of_birth=request.POST.get('dob')
        obj.id_number=request.POST.get('prv_no')
        obj.phone_no=request.POST.get('phn')
        # obj.id_proof=request.POST.get('prv')
        myfile = request.FILES['prv']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.id_proof = myfile.name
        obj.name=request.POST.get('n1')
        obj.star=request.POST.get('str')
        obj.save()
        # return darshanaview(request)
    return render(request,'darshanabook/darshanabook.html')
from django.http import HttpResponseRedirect
from darshana.models import BookingTemp
def vazh_book(request,idd):
    ss=request.session["uid"]
    ob=BookingTemp()
    ob.d_id=idd
    ob.u_id=ss
    ob.status="pending"
    ob.vb_id="0"
    ob.save()
    # obj=Darshana.objects.get(did=idd)
    # obk=Ureg.objects.all()
    # context={
    #     'a':obj,
    #     'w':obk
    # }
    # if request.method == "POST":
    #     obj = Darshanabook()
    #     obj.day = request.POST.get('day')
    #     obj.date = request.POST.get('dt')
    #     obj.time = request.POST.get('tim')
    #     obj.ppls = request.POST.get('ppl')
    #     obj.u_id=request.POST.get('u')
    #     obj.save()
    #     # return darshanaview(request)

    return HttpResponseRedirect('/darshana/viewdarshana/')
    # return render(request,'darshanabook/vayipadbooking.html',context)


def vazh_booknew(request):
    ss = request.session["uid"]
    obj1=BookingTemp.objects.filter(u_id=ss,status="pending")
    # obk=Ureg.objects.all()
    context={
        'a':obj1,
    #     'w':obk
    }
    if request.method == "POST":
        obj = Vazhipadbook()
        obj.date = request.POST.get('dt')
        obj.star = request.POST.get('str')
        obj.time = request.POST.get('tim')
        obj.name = request.POST.get('n1')
        obj.u_id=ss
        obj.gender=request.POST.get('gender')
        obj.save()

        for o in obj1:
            o.status="Booked"
            o.vb_id=obj.vb_id
            o.save()

        # return darshanaview(request)
        return HttpResponseRedirect('/darshana/viewdarshana/')
    return render(request,'darshanabook/vayipadbooking.html',context)


def remove(request,idd):
    ob=BookingTemp.objects.get(booking_id=idd)
    ob.delete()

    return vazh_booknew(request)

from darshana.models import Vazhipadbook

def viewvazhi(request):
    ob=Vazhipadbook.objects.all()
    context={
        'ok':ob
    }
    return render(request,'darshana/viewvazhipad.html',context)

def details(request,idd):
    ob=BookingTemp.objects.filter(vb_id=idd)
    context={
        'ok':ob
    }
    return render(request,'darshana/details.html',context)