# Generated by Django 4.1.4 on 2023-06-11 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_remove_fullorder_customer_remove_fullorder_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_order',
        ),
        migrations.DeleteModel(
            name='Fullorder',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
