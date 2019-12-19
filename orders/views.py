from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist


from .models import RegularPizza, SicilianPizza, Topping, Cart
# Create your views here.

def index(request):
	if not request.user.is_authenticated:
		return render(request, "orders/login.html", {"message": None})
	fname = request.user.first_name
	print(f"User is: {fname}")
	try:
		cart = Cart.objects.get(user=fname)
		print(f"cart is : {cart}")
		
		print("this is try part")
		
	except (TypeError, ObjectDoesNotExist) as e:
		print("except begins")
		context = {
			"user": request.user,
			"regularpizzas": RegularPizza.objects.all(),
			"sicilianpizzas": SicilianPizza.objects.all(),
			"toppings": Topping.objects.all(),
			#"cart": Cart.objects.get(user=fname)
		}
		return render(request, "orders/menu.html", context)
	else:
		print("no exceptions")
		context = {
			"user": request.user,
			"regularpizzas": RegularPizza.objects.all(),
			"sicilianpizzas": SicilianPizza.objects.all(),
			"toppings": Topping.objects.all(),
			"cart": cart.definitions.all()
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
		pizza_price = request.POST['size']
		print(f"Baze pizza price is {pizza_price}")
		topping_id = request.POST.getlist('toppings')
		print(f"topping is : {topping_id}")
		pizza = RegularPizza.objects.get(pk=regularpizza_id)
		print(f"pizza is : {pizza.name}")

		total_cost = float(pizza_price)
		print(f"total cost is {total_cost}")
		for t in topping_id:
			total_cost = total_cost + float(Topping.objects.get(pk=int(t)).rate)
			print(f"total cost in loop is : {total_cost}")

		item = Cart(user=request.user.first_name, item_name=pizza.name, item_price=pizza_price, grand_total=total_cost)
		item.save()
		for t in topping_id:
			topping = Topping.objects.get(pk=int(t))
			item.extra_toppings.add(topping)

		print(f"Cart is {item}")
		
		return HttpResponseRedirect(reverse("index"))