# Generated by Django 3.2.13 on 2022-05-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0019_alter_secretkey_expiry_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='biouser',
            name='image_profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]