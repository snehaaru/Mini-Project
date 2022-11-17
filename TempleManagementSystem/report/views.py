from django.shortcuts import render
from report.models import  Report
# Create your views here.


def report(request):
    obj=Report()
    if request.method=="POST":
        obj.caption=request.POST.get('cap')
        obj.about=request.POST.get('abt')
        obj.report=request.POST.get('rpt')
        obj.date=request.POST.get('dt')
        obj.time=request.POST.get('tm')
        obj.save()


    return render(request,'report/report1.html')

def vreport(request):
    obj=Report.objects.all()
    context={
        'e' : obj
    }

    return render(request,'report/viewreport.html',context)
