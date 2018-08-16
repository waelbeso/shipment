from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/', views.IndexView.as_view(),   name='index'),
    url(r'^companies/$', views.CompanyView.as_view(), name='companies'),
    url(r'^<int:bill_id>/bill$', views.bill,                  name='bill'),
    url(r'^order/$', views.order,                 name='order'),
    url(r'^country/$', views.countryView,           name='country'),
]
