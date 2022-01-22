from django.db import models

# Create your models here.
class Homestay(models.Model):
    name = models.CharField(max_length = 700)
    price = models.IntegerField()
    rating = models.FloatField(null=True)
    location = models.CharField(max_length = 200)
    guest = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    wifi = models.IntegerField()
    pool = models.IntegerField()
    parking = models.IntegerField()

    def __str__(self):
        return self.name

    #Name,Price,Rating,Location,Guest,Bed,Bath,Wifi,Pool,Parking

