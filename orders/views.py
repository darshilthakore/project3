from django.http import HttpResponse
from django.shortcuts import render


from .models import RegularPizza, SicilianPizza, Topping
# Create your views here.
def index(request):
	context = {
		"regularpizzas": RegularPizza.objects.all(),
		"sicilianpizzas": SicilianPizza.objects.all(),
		"toppings": Topping.objects.all()
	}

	return render(request, "orders/menu.html", context)
