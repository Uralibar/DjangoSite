# Generated by Django 5.0.4 on 2024-04-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_car_top_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='img/'),
        ),
    ]