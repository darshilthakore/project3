# Generated by Django 2.0.12 on 2019-12-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegularPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price_small', models.IntegerField()),
                ('price_large', models.IntegerField()),
                ('toppings', models.ManyToManyField(blank=True, related_name='regular_pizzas', to='orders.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='SicilianPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price_small', models.IntegerField()),
                ('price_large', models.IntegerField()),
                ('toppings', models.ManyToManyField(blank=True, related_name='sicilian_pizzas', to='orders.Topping')),
            ],
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
    ]
