# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# Create your models here.
Curruncy_list = (('USD', 'US Dollar'), ('EGP', 'Egyptian Pound'))

Order_Types_CHOICES = (
    ('II', 'International Importation'),
    ('IE', 'International Export'),
    ('DI', 'Domestic Import'),
    ('DE', 'Domestic Export'),
)

SERVICE_TYPE_CHOICES = (
    ('Ex', 'Express'),
    ('Ec', 'Economy'),
)


class Country(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Zone(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    zoneNo = models.IntegerField()
    economy = models.BooleanField(default=False)
    express = models.BooleanField(default=False)

    def __str__(self):
        return self.zoneNo

    @property
    def get_ZoneNo(self):
        return self.zoneNo


class Tariff(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    wieght = models.DecimalField(max_digits=3, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    service_type = models.CharField(max_length=2, choices=SERVICE_TYPE_CHOICES)
    transit = models.CharField(max_length=2, choices=(('Im', 'Import'), ('Ex', 'Export')))
    document = models.BooleanField(default=False)
    extra = models.BooleanField(default=False)


class Order(models.Model):
    order_type = models.CharField(max_length=2, choices=Order_Types_CHOICES)
    contact_id = models.IntegerField()
    consignment = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, models.CASCADE)
    service_type = models.CharField(max_length=2, choices=SERVICE_TYPE_CHOICES)

    shipper_name = models.CharField(max_length=100 , verbose_name="shipper_name")
    shipper_company = models.CharField(max_length=100)
    shipper_address = models.CharField(max_length=1000)
    shipper_alter_address = models.CharField(max_length=1000)
    #shipper_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='shipper_country')
    shipper_country = models.CharField(max_length=3 , verbose_name="shipper_country")
    #shipper_cite = models.ForeignKey(City, models.CASCADE, related_name='shipper_cite')
    shipper_cite    = models.CharField(max_length=100 , verbose_name="shipper_cite")
    shipper_postalcode = models.CharField(max_length=50)
    shipper_phone = models.CharField(max_length=100)

    consignee_name = models.CharField(max_length=100)
    consignee_company = models.CharField(max_length=100)
    consignee_address = models.CharField(max_length=1000)
    consignee_alter_address = models.CharField(max_length=1000)
    consignee_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='consignee_country')
    consignee_cite = models.ForeignKey(City, models.CASCADE, related_name='consignee_cite')
    consignee_postalcode = models.CharField(max_length=50)
    consignee_phone = models.CharField(max_length=100)

    description = models.CharField(max_length=1000)
    is_document = models.BooleanField(default=False)
    Quantity = models.IntegerField()
    custom_value = models.DecimalField(max_digits=13, decimal_places=2)

    custom_currency = models.CharField(max_length=3, choices=Curruncy_list)
    actual_weight = models.DecimalField(max_digits=13, decimal_places=3)
    chargeable_weight = models.DecimalField(max_digits=13, decimal_places=3)
    payment_type = models.CharField(max_length=10)
    currency = models.CharField(max_length=3, choices=Curruncy_list)
    tariff = models.DecimalField(max_digits=6, decimal_places=2)
    insurance = models.DecimalField(max_digits=8, decimal_places=2)
    vat = models.DecimalField(max_digits=8, decimal_places=2)
    fuel = models.DecimalField(max_digits=8, decimal_places=2)
    postalfees = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    order_value = models.DecimalField(max_digits=12, decimal_places=2)
    confirmed = models.BooleanField(default=False)
