# Generated by Django 2.0.12 on 2019-12-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20191218_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='extra_toppings',
            field=models.ManyToManyField(blank=True, related_name='cart', to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='cart',
            name='grand_total',
            field=models.FloatField(default=0),
        ),
    ]
