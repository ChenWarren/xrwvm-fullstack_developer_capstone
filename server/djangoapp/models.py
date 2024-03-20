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
class CarMake(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    founded = models.DateField(blank=True, null=True)  # Year the company was founded
    headquarters = models.CharField(max_length=255, blank=True, null=True)  # Location of headquarters
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='car_models')
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=(('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe'), ('Wagon', 'Wagon')))
    year = models.IntegerField()
    engine_size = models.IntegerField(blank=True, null=True)  # in cubic centimeters
    fuel_type = models.CharField(max_length=10, blank=True, null=True, choices=(('Gasoline', 'Gasoline'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')))

    def __str__(self):
        return '{} - {}'.format(self.make.name, self.name)
