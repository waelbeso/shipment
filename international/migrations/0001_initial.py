# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-16 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(choices=[('II', 'International Importation'), ('IE', 'International Export'), ('DI', 'Domestic Import'), ('DE', 'Domestic Export')], max_length=2)),
                ('contact_id', models.IntegerField()),
                ('consignment', models.CharField(max_length=20)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('service_type', models.CharField(choices=[('Ex', 'Express'), ('Ec', 'Economy')], max_length=2)),
                ('shipper_name', models.CharField(max_length=100, verbose_name='sh_name')),
                ('shipper_company', models.CharField(max_length=100)),
                ('shipper_address', models.CharField(max_length=1000)),
                ('shipper_alter_address', models.CharField(max_length=1000)),
                ('shipper_postalcode', models.CharField(max_length=50)),
                ('shipper_phone', models.CharField(max_length=100)),
                ('consignee_name', models.CharField(max_length=100)),
                ('consignee_company', models.CharField(max_length=100)),
                ('consignee_address', models.CharField(max_length=1000)),
                ('consignee_alter_address', models.CharField(max_length=1000)),
                ('consignee_postalcode', models.CharField(max_length=50)),
                ('consignee_phone', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('is_document', models.BooleanField(default=False)),
                ('Quantity', models.IntegerField()),
                ('custom_value', models.DecimalField(decimal_places=2, max_digits=13)),
                ('custom_currency', models.CharField(choices=[('USD', 'US Dollar'), ('EGP', 'Egyptian Pound')], max_length=3)),
                ('actual_weight', models.DecimalField(decimal_places=3, max_digits=13)),
                ('chargeable_weight', models.DecimalField(decimal_places=3, max_digits=13)),
                ('payment_type', models.CharField(max_length=10)),
                ('currency', models.CharField(choices=[('USD', 'US Dollar'), ('EGP', 'Egyptian Pound')], max_length=3)),
                ('tariff', models.DecimalField(decimal_places=2, max_digits=6)),
                ('insurance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('vat', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fuel', models.DecimalField(decimal_places=2, max_digits=8)),
                ('postalfees', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('order_value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('confirmed', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='international.Company')),
                ('consignee_cite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consignee_cite', to='international.City')),
                ('consignee_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consignee_country', to='international.Country')),
                ('shipper_cite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipper_cite', to='international.City')),
                ('shipper_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipper_country', to='international.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wieght', models.DecimalField(decimal_places=2, max_digits=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('service_type', models.CharField(choices=[('Ex', 'Express'), ('Ec', 'Economy')], max_length=2)),
                ('transit', models.CharField(choices=[('Im', 'Import'), ('Ex', 'Export')], max_length=2)),
                ('document', models.BooleanField(default=False)),
                ('extra', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zoneNo', models.IntegerField()),
                ('economy', models.BooleanField(default=False)),
                ('express', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='international.Company')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='international.Country')),
            ],
        ),
        migrations.AddField(
            model_name='tariff',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='international.Zone'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='international.Country'),
        ),
    ]
