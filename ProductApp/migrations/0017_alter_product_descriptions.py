# Generated by Django 3.2.13 on 2022-05-18 17:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0016_alter_product_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='descriptions',
            field=ckeditor.fields.RichTextField(default='This', null=True),
        ),
    ]
