# Generated by Django 2.1.7 on 2019-04-05 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='image',
            field=models.ImageField(default='guest/img/default.png', upload_to='guest/img/'),
        ),
    ]
