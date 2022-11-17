from django.shortcuts import render
from ureg.models import Ureg
from login.models import Login

# Create your views here.

def ureg(request):
    if request.method=="POST":
        obj=Ureg()
        obj.uname=request.POST.get('name')
        obj.usname=request.POST.get('username')
        obj.address=request.POST.get('address')
        obj.gender=request.POST.get('gen')
        obj.phone=request.POST.get('Phone')
        obj.password=request.POST.get('pwd')
        obj.cpassword=request.POST.get('pwd1')
        obj.email=request.POST.get('email')
        obj.nakshathra=request.POST.get('str')
        obj.dob=request.POST.get('dob')
        obj.save()

        ob = Login()
        ob.uname = obj.uname
        ob.password = obj.password
        ob.u_type = 'user'
        ob.u_id = obj.u_id
        ob.save()

    return render(request,'ureg/userreg.html')
def manage(request):
    ss=request.session["uid"]
    obj=Ureg.objects.filter(u_id=ss)
    context ={
        'u': obj
    }
    return render(request,'ureg/manage.html',context)


def uprofile(request,idd):
    obj=Ureg.objects.get(u_id=idd)
    context={
        't':obj
    }
    if request.method=="POST":
        obj=Ureg.objects.get(u_id=idd)
        obj.uname = request.POST.get('name')
        obj.address = request.POST.get('ads')
        obj.dob = request.POST.get('dob')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('Phone')
        obj.nakshathra = request.POST.get('str')
        obj.save()
        return manage(request)
    return render(request,'ureg/userprofile.html',context)

def viewuser(request):
    obj=Ureg.objects.all()
    context={
        'g':obj
    }


    return render(request,'ureg/viewuser.html',context)


