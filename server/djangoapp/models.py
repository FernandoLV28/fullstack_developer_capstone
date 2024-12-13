from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    country = models.CharField(max_length=50, blank=True, null=True)
    founded_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    CONVERTIBLE = 'Convertible'

    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedán'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (CONVERTIBLE, 'Convertible'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='car_models')
    dealership_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50)
    car_type = models.CharField(choices=CAR_TYPE_CHOICES, max_length=20)
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])
    color = models.CharField(max_length=20, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.car_make.name} {self.name} ({self.year}) - {self.car_type}'
