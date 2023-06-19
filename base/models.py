from django.db import models
from django.contrib.auth.models import User
import uuid




class Review(models.Model):
    name = models.CharField(max_length=150, blank = True, null = True)
    e_mail = models.EmailField(blank = True, null = True)
    message = models.TextField(blank = True, null = True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    


    class Meta :
        ordering = ['-created']

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE )
    name = models.CharField(max_length=200, null = True)
    e_mail = models.EmailField(null = True)
    id = models.UUIDField(default = uuid.uuid4 , editable = False, unique = True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    item_name = models.CharField(max_length=150, blank =True, null = True)
    price = models.IntegerField()
    item_image = models.ImageField(upload_to= 'itempics')
    item_about = models.TextField(null =True)
    quantity_available = models.IntegerField( null=True)
    id = models.UUIDField(default= uuid.uuid4, editable= False, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name
    

class Order(models.Model):
    customer  = models.ForeignKey(Customer, blank = True, null = True, on_delete=models.CASCADE)
    complete = models.BooleanField(null= True, blank = True, default= False)
    firstname = models.CharField(max_length = 200, blank = True, null = True)
    lastname = models.CharField(max_length=200, blank = True, null =True)
    e_mail = models.EmailField(blank = True, null = True)
    location = models.CharField(max_length= 200, blank = True, null = True)
    phone = models.CharField(max_length= 200, blank = True, null = True)
    Address = models.CharField(max_length= 200, blank = True, null=True)
    
    id = models.UUIDField(default = uuid.uuid4, editable = False, unique = True, primary_key=True)

    date_ordered = models.DateTimeField(auto_now_add=True)
    
    @property
    def totalbill(self):
        orders = self.orderitem_set.all()
        total = sum([order.gettotal for order in orders])
        return total
    
    def __str__(self):
        return self.customer.name
    
    class Meta:
        ordering = ['firstname']
    
class OrderItem(models.Model):
    item = models.ForeignKey(Item, blank = True, null = True , on_delete = models.CASCADE)
    order = models.ForeignKey(Order, blank = True ,null = True , on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)
    id = models.UUIDField(default = uuid.uuid4, editable = False, unique = True, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    
    @property
    def gettotal(self):
        total = self.item.price * self.quantity
        return total

    def __str__(self):
        return self.order.customer.name

