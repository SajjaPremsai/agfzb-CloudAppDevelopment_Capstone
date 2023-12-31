from django.contrib import admin

from djangoapp.models import CarMake, CarModel
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here

admin.site.register(CarModel)
admin.site.register(CarMake)
