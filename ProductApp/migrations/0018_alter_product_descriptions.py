# Generated by Django 3.2.13 on 2022-05-18 17:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0017_alter_product_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='descriptions',
            field=ckeditor.fields.RichTextField(default='None', null=True),
        ),
    ]
