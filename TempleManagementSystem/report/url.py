from django.conf.urls import url
from report import views

urlpatterns = [
    url('report/',views.report),
    url('viewre/',views.vreport)

]
