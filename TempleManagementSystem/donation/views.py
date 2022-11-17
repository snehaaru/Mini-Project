from django.shortcuts import render
from donation.models import Donation
from ureg.models import Ureg


# Create your views here.
def donate(request):
    ob=Ureg.objects.all()
    context={
        'r':ob,
    }
    if request.method == "POST":
        obj = Donation()
        obj.amount = request.POST.get('amt')
        obj.date = request.POST.get('dat')
        obj.time = request.POST.get('time')
        obj.do_type = request.POST.get('type')
        obj.status='pending'
        obj.u_id=request.POST.get('u')
        obj.save()

    return render(request, 'donation/donations.html',context )


def vdon(request):
    # ss=request.session["u_id"]
    # ob=Ureg.objects.get(uid=ss)
    obj = Donation.objects.all()
    context = {
        'c': obj
    }

    return render(request, 'donation/viewdonation.html', context)

def con(request):
    obj = Donation.objects.filter(status='contributer')
    context = {
        'k': obj
    }

    return render(request, 'donation/contributers.html',context)



def ap(request,idd):
    obj = Donation.objects.get(do_id=idd)
    obj.status = 'contributer'
    obj.save()
    return vdon(request)


def re(request,idd):
    obj = Donation.objects.get(do_id=idd)
    obj.status = 'monthly aims'
    obj.save()
    return vdon(request)
def monthly(request):
    obj = Donation.objects.filter(status='monthly aims')
    context = {
        'k': obj
    }

    return render(request, 'donation/monthly_aims.html',context)

def gd(request,idd):
    obj = Donation.objects.get(do_id=idd)
    obj.status = 'good donation'
    obj.save()
    return vdon(request)
def good(request):
    obj = Donation.objects.filter(status='good donation')
    context = {
        'k': obj
    }

    return render(request, 'donation/good_donation.html',context)

