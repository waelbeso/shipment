# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.views import generic
from .forms import OrderForm , countryForm

from .models import Country, Company
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("asdasdasd")

class IndexView(generic.TemplateView):
    template_name = 'international/index.html'

class CompanyView(generic.ListView):
    model = Company
    template_name = 'international/companies.html'
    allcompanies = Company.objects.all()
    context_object_name = 'allcompanies'

@login_required
def order(request):
    items_data = [ {"weight": "1", "width": "1", "height": "1", "lenth": "1", "shipping": "1"} , {"weight": "2", 'width': "2", "height": "2", "lenth": "2", "shipping": "2"} ]
    title = "Order"
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
        	print form.data['items']
    else:
        form = OrderForm()
    return render(request, 'international/order.html', {'form': form , 'items':items_data,'title':title  })

def bill(request,bill_id):
    return HttpResponse("Bill is %i" %bill_id)

def countryView(request):
    if request.method == 'POST':
        form = countryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = countryForm()
    return render(request, 'international/countryform.html', {'form': form})
