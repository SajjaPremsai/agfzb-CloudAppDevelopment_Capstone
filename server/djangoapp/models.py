from django.db import models
from django.utils.timezone import now


# Create your models here.


# <HINT> Create a Car Make model `class CarMake(models.Model)`:


class CarMake(models.Model):
    Name = models.CharField(max_length=25)
    Description = models.TextField()
# - Name
# - Description
# - Any other fields you would like to include in car make model
    def __str__(self) -> str:
        return self.Name
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    name = models.CharField(max_length=255)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.CharField(max_length=255)
    CAR_TYPES_CHOICES = (
        ("SEDAN", "Sedan"), ("SUV", "SUV"), ("WAGON", "Wagon"), ("LIMOUSINE", "Limousine"), ("BATMOBILE", "Batmobile")
    )
    type = models.CharField(max_length=10, choices=CAR_TYPES_CHOICES)
    year = models.DateField()

    def __str__(self):
        return "Name: " + self.name + " Make Name: " + self.car_make.name + " Type: " + self.type + " Dealer ID: " + str(self.dealer_id) + " Year: " + str(self.year)




# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year,sentiment, id):
        self.dealership=dealership
        self.name=name
        self.purchase=purchase
        self.review=review
        self.purchase_date=purchase_date
        self.car_make=car_make
        self.car_model=car_model
        self.car_year=car_year
        self.sentiment=sentiment #Watson NLU service
        self.id=id

    def __str__(self):
        return f"Review ID: {self.id}\n" \
               f"Dealership: {self.dealership}\n" \
               f"Name: {self.name}\n" \
               f"Purchase: {self.purchase}\n" \
               f"Review: {self.review}\n" \
               f"Purchase Date: {self.purchase_date}\n" \
               f"Car Make: {self.car_make}\n" \
               f"Car Model: {self.car_model}\n" \
               f"Car Year: {self.car_year}\n" \
               f"Sentiment: {self.sentiment}\n"

# <HINT> Create a plain Python class `DealerReview` to hold review data
