from django.conf.urls import url
from temple import views

urlpatterns = [
    url('templedata/',views.temple),
    url('vtemp/',views.vtemple)

]