from django.conf.urls import url
from ureg import views

urlpatterns = [
    url('ureg/',views.ureg),
    url('vuser/',views.viewuser),
    url('manage/',views.manage),
    url(r'^up/(?P<idd>\w+)',views.uprofile,name='up'),

]