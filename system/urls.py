from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^', views.options, name='options'),
    url(r'^employee/new/$', views.employee_new, name='employee_new'),
    url(r'^customer/new/$', views.customer_new, name='customer_new'),
    url(r'^invoice/new/$', views.invoice_new, name='invoice_new'),
    url(r'^invoice/(?P<pk>\d+)/$', views.invoice_detail, name='invoice_detail'),

]
