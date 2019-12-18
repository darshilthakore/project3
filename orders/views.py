from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import RegularPizza, SicilianPizza, Topping, Cart
# Create your views here.

def index(request):
	if not request.user.is_authenticated:
		return render(request, "orders/login.html", {"message": None})
	context = {
		"user": request.user,
		"regularpizzas": RegularPizza.objects.all(),
		"sicilianpizzas": SicilianPizza.objects.all(),
		"toppings": Topping.objects.all()


	}
	return render(request, "orders/menu.html", context)

def login_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "orders/login.html", {"message": "Invalid Credentials"})

def logout_view(request):
	logout(request)
	return render(request, "orders/login.html", {"message": "Logged Out"})


def register_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
	email = request.POST["email"]

	user = User.objects.create_user(username, email, password)
	user.first_name = request.POST["first"]
	user.last_name = request.POST["last"]
	user.save()
	login(request, user)

	return HttpResponseRedirect(reverse("index"))

def menu(request):
	context = {
		"user": request.user,
		"regularpizzas": RegularPizza.objects.all(),
		"sicilianpizzas": SicilianPizza.objects.all(),
		"toppings": Topping.objects.all(),
		"cart": Cart.objects.get(user=request.user.first_name)		
	}

	return render(request, "orders/menu.html", context)


def cart(request, regularpizza_id):
	if request.method == "POST":
		size = request.POST['size']
		print(f"pizza size is {size}")
		topping_id = request.POST.getlist('toppings')
		print(f"topping is : {topping_id}")
		pizza = RegularPizza.objects.get(pk=regularpizza_id)
		print(f"pizza is : {pizza.name}")
		for t in topping_id:
			topping = Topping.objects.get(pk=int(t))
			pizza.toppings.add(topping)
		item = Cart(user=request.user.first_name, item_name=pizza.name, item_price=size)
		print(f"{item}")
		item.save()
		return HttpResponseRedirect(reverse("menu"))