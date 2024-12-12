# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

# Modelo para la marca de coche
class CarMake(models.Model):
    name = models.CharField(max_length=50)  # Nombre de la marca de coche
    description = models.TextField()  # Descripción de la marca de coche
    country = models.CharField(max_length=50, blank=True, null=True)  # País de origen (opcional)
    founded_year = models.IntegerField(blank=True, null=True)  # Año de fundación de la marca (opcional)

    def __str__(self):
        """Retorna una representación amigable del objeto CarMake"""
        return f'{self.name} - {self.description}'

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

# Modelo para el coche (CarModel)
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    CONVERTIBLE = 'Convertible'
    
    # Definimos las opciones para el tipo de coche
    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedán'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (CONVERTIBLE, 'Convertible'),
    ]
    
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Relación de muchos a uno con CarMake
    dealership_id = models.IntegerField()  # Referencia a un concesionario en la base de datos Cloudant
    name = models.CharField(max_length=50)  # Nombre del modelo de coche
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)  # Tipo de coche (Sedán, SUV, etc.)
    year = models.DateField()  # Año del modelo de coche
    color = models.CharField(max_length=20, blank=True, null=True)  # Color del coche (opcional)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Precio del coche (opcional)
    
    def __str__(self):
        """Retorna una representación amigable del objeto CarModel"""
        return f'{self.car_make.name} {self.name} ({self.year.year}) - {self.car_type}'
