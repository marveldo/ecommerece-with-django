from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Customer


def CreateCustomer(sender,instance,created,**kwargs):

    if created:
        user = instance
        customer = Customer.objects.create(
            user = user,
            name = user.username,
           
        )

post_save.connect(CreateCustomer, sender= User)