from django.conf.urls import url
from darshana import views


urlpatterns=[
    url('adddarshana/',views.darshanaadd),
    url('viewdarshana/',views.darshanaview),
    url(r'^book/',views.book),
    url('vazhi/',views.vazhipad_view),
    url(r'^vazh_booking/(?P<idd>\w+)',views.vazh_book),
    url(r'^remove/(?P<idd>\w+)',views.remove,name='remove'),
    url('vayipad/',views.vazh_booknew),
    url('viewvayi/',views.viewvazhi),
    url('details/(?P<idd>\w+)',views.details,name='details')


]