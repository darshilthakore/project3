# Generated by Django 2.0.12 on 2019-12-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item_quantity',
            field=models.IntegerField(blank=True),
        ),
    ]