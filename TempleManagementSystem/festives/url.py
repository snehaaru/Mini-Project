from django.conf.urls import url
from festives import views

urlpatterns = [
    url('festives/',views.fest),
    url('vfest/',views.vfest)
]