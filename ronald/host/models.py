from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=120)
    department = models.CharField(max_length=60)
    phone_address = models.CharField(max_length=10)
    web_page = models.CharField(max_length=50)
    image = models.ImageField(upload_to='hospital/img/', default='hospital/img/default.png')

class House(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=120)
    department = models.CharField(max_length=60)
    phone_address = models.CharField(max_length=10)
    image = models.ImageField(upload_to='house/img/', default='house/img/default.png')

class Guest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=60)
    date_of_birth = models.DateField()
    date_of_request = models.DateField()
    # ForeignKey
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    # Number of room
    room_number = models.IntegerField()
