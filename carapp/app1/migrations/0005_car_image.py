# Generated by Django 5.0.4 on 2024-04-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_car_name_car_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default='', upload_to='img/'),
        ),
    ]
