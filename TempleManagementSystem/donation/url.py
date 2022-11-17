from django.conf.urls import url
from donation import views

urlpatterns = [
    url('donation/',views.donate),
    url('view/',views.vdon),
    url(r'^ap/(?P<idd>\w+)', views.ap, name='y'),
    url(r'^re/(?P<idd>\w+)', views.re, name='i'),
    url(r'^gddt/(?P<idd>\w+)', views.gd, name='gm'),
    url('cm/',views.con),
    url('mo/',views.monthly),
    url('gd/',views.good)

]