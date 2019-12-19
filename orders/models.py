from django.db import models

# Create your models here.

class Topping(models.Model):
	topping = models.CharField(max_length=64)
	rate = models.FloatField()

	def __str__(self):
		return f"{self.topping}: $ {self.rate}"


class RegularPizza(models.Model):
	name = models.CharField(max_length=64)
	price_small = models.FloatField()
	price_large = models.FloatField()
	toppings = models.ManyToManyField(Topping, blank=True, related_name="regular_pizzas")

	def __str__(self):
		return f"Pizza - {self.name} | Small - $ {self.price_small} | Large - ${self.price_large}"

class SicilianPizza(models.Model):
	name = models.CharField(max_length=64)
	price_small = models.FloatField()
	price_large = models.FloatField()
	toppings = models.ManyToManyField(Topping, blank=True, related_name="sicilian_pizzas")

	def __str__(self):
		return f"Pizza - {self.name} | Small - $ {self.price_small} | Large - ${self.price_large}"


class Cart(models.Model):
	user = models.CharField(max_length=64)
	item_name = models.CharField(max_length=64)
	item_price = models.FloatField()
	extra_toppings = models.ManyToManyField(Topping, blank=True, related_name="cart")
	grand_total = models.FloatField(default=0)
	# item_quantity = models.IntegerField(blank=True)
	# sub_total = models.FloatField(blank=True)

	def __str__(self):
		return f"{self.user} ordered {self.item_name} costing ${self.item_price}"