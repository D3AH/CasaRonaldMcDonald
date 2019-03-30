# Generated by Django 2.1.7 on 2019-03-30 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=60)),
                ('date_of_birth', models.DateField()),
                ('date_of_request', models.DateField()),
                ('room_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=120)),
                ('department', models.CharField(max_length=60)),
                ('phone_address', models.CharField(max_length=10)),
                ('web_page', models.CharField(max_length=50)),
                ('image', models.ImageField(default='hospital/img/default.png', upload_to='hospital/img/')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=120)),
                ('department', models.CharField(max_length=60)),
                ('phone_address', models.CharField(max_length=10)),
                ('image', models.ImageField(default='house/img/default.png', upload_to='house/img/')),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.Hospital'),
        ),
        migrations.AddField(
            model_name='guest',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.House'),
        ),
    ]
