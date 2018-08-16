from django import forms

from .models import *

from shipment.countries import COUNTRIES


class OrderForm(forms.ModelForm):
    shipper_country = forms.ChoiceField(label='Country:',choices=COUNTRIES, required=True, widget=forms.Select(attrs={ 'id':'shipper_country' }))
    items           = forms.CharField(required=False,widget=forms.HiddenInput(attrs={ 'class':'variant_container'}) )
    class Meta:
        model =Order
        fields=('shipper_name','shipper_company','shipper_address','shipper_alter_address','shipper_country','shipper_cite','shipper_postalcode','shipper_phone')








class countryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields=('name','code')