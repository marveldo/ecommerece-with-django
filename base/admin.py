from django.contrib import admin
from .models import Review,Item,Customer,Order,OrderItem


admin.site.register(Review)
admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)


# Register your models here.
