# Generated by Django 5.0.4 on 2024-04-30 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_car_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='./img/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='./img/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='./img/'),
        ),
    ]
