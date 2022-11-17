from django.conf.urls import url
from temp import views
urlpatterns=[
    url('publichome/',views.home),
    url('devoteehome/',views.devotee),
    url('adminhome/',views.adminhome),
]
