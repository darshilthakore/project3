from django.contrib import admin

# Register your models here.
from .models import Topping, RegularPizza, SicilianPizza, Cart

admin.site.register(Topping)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Cart)