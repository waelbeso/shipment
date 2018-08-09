from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view() ,name='index'),
    path('companies',views.CompanyView.as_view() ,name='companies'),
    path('<int:bill_id>/bill',views.bill ,name='bill'),
    path('order/',views.order ,name='order'),
    path('country/',views.countryView ,name='country')
]