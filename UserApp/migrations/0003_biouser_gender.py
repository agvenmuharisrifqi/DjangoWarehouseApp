# Generated by Django 3.2.13 on 2022-05-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_auto_20220517_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='biouser',
            name='gender',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]