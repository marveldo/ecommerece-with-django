# Generated by Django 4.1.4 on 2023-06-09 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_item_quantity_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('e_mail', models.EmailField(max_length=254, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('quantiy', models.IntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.customer')),
                ('product_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.item')),
            ],
        ),
    ]
