from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from festives.models import Festives


# Create your views here.
def fest(request):

    if request.method=="POST":
        obj = Festives()
        obj.startsdate=request.POST.get('fsdate')
        obj.enddate=request.POST.get('fedate')
        obj.fname=request.POST.get('fname')
        obj.enddate=request.POST.get('fedate')
        obj.about=request.POST.get('abt')
        obj.spclpooja=request.POST.get('pooja')
        obj.opentime=request.POST.get('opn')
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.image=myfile.name
        # obj.image=request.POST.get('name')
        obj.save()





    return render(request,'festives/festives.html')

def vfest(request):
    obj=Festives.objects.all()
    context={
        'd':obj
    }
    return render(request,'festives/viewfestival.html',context)

