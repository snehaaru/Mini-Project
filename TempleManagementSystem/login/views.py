from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        u_name=request.POST.get('usr')
        passw=request.POST.get('pwd')
        obj=Login.objects.filter(uname=u_name,password=passw)
        tp=''
        for ob in obj:
            tp=ob.u_type
            uid=ob.u_id
            if tp=="admin":
                request.session["u_id"]= uid
                return HttpResponseRedirect('/temp/adminhome/')
            elif tp=="user":
                request.session["uid"]= uid
                return HttpResponseRedirect('/temp/devoteehome/')

        else:
            objlist="Username or password incorrect..check your credentials"
            context={
                'msg' :objlist,
                }
            return render(request,'login/login.html',context)
    return render(request, 'login/login.html')




