# Generated by Django 2.1.7 on 2019-04-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0002_guest_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='phone_address',
            field=models.CharField(default='Sin registrar', max_length=10),
        ),
    ]
