from darshanabook import views
from django.conf.urls import url

urlpatterns=[
    url('bookdar/',views.darshanabook),
    url('viewdar/', views.viewbookdarshan),

]