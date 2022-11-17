from django.shortcuts import render
from temple.models import  Temple
from django.core.files.storage import FileSystemStorage
# Create your views here.


def temple(request):

    if request.method=="POST":
        mfile=request.FILES['name']
        fs=FileSystemStorage()
        file=fs.save(mfile.name,mfile)

        obj=Temple()
        obj.tid="1"
        obj.place=request.POST.get('plc')
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('adrs')
        obj.prathishta=request.POST.get('lord')
        obj.estd=request.POST.get('estd')
        obj.history=request.POST.get('hst')
        obj.image=mfile.name
        obj.save()


    return render(request,'temple/temple.html')

def vtemple(request):
    obj=Temple.objects.all()
    context={
        'f':obj
    }
    return render(request,'temple/Viewtemple.html',context)

