# Generated by Django 3.2.13 on 2022-05-22 22:18

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_id', models.CharField(max_length=25, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('suplier', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_id', models.CharField(max_length=25, unique=True)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('doc_type', models.CharField(max_length=3)),
                ('number', models.CharField(max_length=255, unique=True)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('note', ckeditor.fields.RichTextField(null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.suplier')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_id', models.CharField(max_length=25, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255, unique=True)),
                ('purchase', models.PositiveIntegerField()),
                ('selling', models.PositiveIntegerField()),
                ('stock', models.IntegerField(default=0, null=True)),
                ('update', models.DateField(auto_now=True)),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.suplier')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.purchaseorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.product')),
            ],
        ),
    ]
