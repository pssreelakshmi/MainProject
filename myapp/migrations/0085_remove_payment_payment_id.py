# Generated by Django 5.0.6 on 2024-11-15 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0084_remove_orderdetails_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_id',
        ),
    ]
