from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .forms import OrderForm , countryForm

from .models import Country, Company
# Create your views here.
def index(request):
    return HttpResponse("asdasdasd")

class IndexView(generic.TemplateView):
    template_name = 'international/index.html'

class CompanyView(generic.ListView):
    model = Company
    template_name = 'international/companies.html'
    allcompanies = Company.objects.all()
    context_object_name = 'allcompanies'


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = OrderForm()
    return render(request, 'international/order.html', {'form': form})

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




