from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Review,Item,Order,OrderItem
from django.core.mail import send_mass_mail
from django.http import JsonResponse,HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import Userupdatedform,itemCreation
from django.contrib import messages
import requests
import json
# Create your views here.
def home (request):
    page = 'home'
       
      
    if request.method == 'POST':
        name = request.POST.get('Name')
        e_mail = request.POST.get('Email')
        phone = request.POST.get('Phone')
        address = request.POST.get('Address')
        subject = request.POST.get('Subject')
        message = request.POST.get('Message')

        Subject = subject
        Message = f'Mr solomon ({name}) user has an issue and this is his message : ({message}) , His phone number is ({phone}) in case you want to contact him and his address his ({address}) incase you want to visit '
        Subject1 = f'response on {subject}'
        Message1 = f'Good day Mr/Mrs ({name}), We have received your message and we will contact you soon.'
       
        datatuple = (
    ( Subject, Message, settings.EMAIL_HOST_USER , ["utibesolomon17@gmail.com"]),
    (Subject1, Message1, settings.EMAIL_HOST_USER, [e_mail]),)
        
        try:
           send_mass_mail(datatuple)
           messages.success(request, 'your message has been sent')
        except:
            messages.error(request ,'couldnt send message plss check your internet')
        
       
           


        
    context = {'page':page}
    return render(request,'base/home.html', context) 
def reviews(request):
    page = 'reviews'
    reviews = Review.objects.all()

    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('E-mail')
        message = request.POST.get('Message')
        try:
           Review.objects.create(
            name = name,
            e_mail = email,
            message = message )
           messages.success(request, 'Review has been sent')
        except:
           messages.error(request, 'review couldnt send')
    context = {'page':page, 'reviews':reviews}
    return render(request, 'base/reviews.html' , context)

def Theteam(request):
    page = 'theteam'
    context = {'page' : page}
    return render(request,'base/theteam.html',context)
def shop(request):
    page= 'shop'
    items = Item.objects.all()
    context = {'page' : page , 'items':items}
    return render(request, 'base/shop.html', context)

def bookonline(request,pk):
    
    item = Item.objects.get(id=pk)
    
    context ={'item':item}
   
    
   
    return render(request, 'base/bookonline.html', context)

def shoppingbag(request):
    page = 'shoppingbag'

    try:
       customer = request.user.customer
       order, created = Order.objects.get_or_create(customer = customer, complete = False)

       items = order.orderitem_set.all()
    except:
        customer =[]
        order = []
        items = []
    context = {'page': page,'orderlist':items, 'orders':order}
    
    return render(request,'base/shoppingbag.html',context)
    
 
def customerlogin(request):
    page = 'login'
    if request.user.is_authenticated :
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        try :
            user = User.objects.get(username = username)
        except:
            print('user oesnt exist')
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect('home')
        else:
            messages.error(request , 'Incorrect Password')
        
    context = {'page': page}
    return render (request, 'base/login.html',context)
def logoutcustomer(request) :
    logout(request)
    messages.success(request, 'User has been logged out')
    return redirect('home')

def registerCustomer(request):
    page = 'register'
    form = Userupdatedform()
    if request.method == 'POST':
        form = Userupdatedform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    context = {'form': form, 'page': page}
    return render(request,'base/login.html',context)
def changeproduct(request):
    data = json.loads(request.body)
    productid = data['product']
    action =  data['action']

    customer = request.user.customer
    try:
       item = Item.objects.get(id = productid)
    except:
        print('item does not exist')
    
    order,created = Order.objects.get_or_create(customer = customer, complete = False)
    try:
       orderitem,created  = OrderItem.objects.get_or_create( order = order , item = item)
       
    except:
        orderitem = []

    if action == 'add':
        orderitem.quantity +=1
        
        if orderitem.quantity > item.quantity_available:
            orderitem.quantity = item.quantity_available
        
    orderitem.save()
    if action == 'remove':
        orderitem.quantity -= 1
        messages.success(request, 'Item has been removed check the shopping bag icon for more')
        orderitem.save()
        if orderitem.quantity <= 0 :
            orderitem.delete()
      

    
    if action =='delete':
        orderitem.delete()
        messages.success(request, 'Item has been removed check the shopping bag icon for more')
    


    print(productid,action)
    return JsonResponse('product has been altered', safe=False)


def checkout(request):
    customer = request.user.customer
    
    order = Order.objects.get(customer = customer, complete = False)
    
    try:
        ip = json.loads(requests.get('https://api.ipify.org?format=json').text)
        location = requests.get(f'http://ip-api.com/json/{ip["ip"]}').text
        location1 = json.loads(location)
    except :
        location1 = []
    
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get("lastname")
        Phonenumber = request.POST.get("phonenumber")
        email = request.POST.get("email")
        user_location = location1['city']
        address = request.POST.get('address')

        order.firstname = firstname
        order.lastname = lastname
        order.phone = Phonenumber
        order.e_mail = email
        order.location = user_location
        order.Address = address
        order.complete = True

        order.save()
        subject = 'Your pending order'
        message = f'hello mr {lastname} your  order has been confirmed and it will be delivered to you in the next 72 hours'
        subject1 = f'Order from {firstname} {lastname}'
        message1 = f'Solomon you have an order from {firstname} {lastname} check your orders for more info'
        datatuple = ((subject,message,settings.EMAIL_HOST_USER,[email]),(subject1, message1, settings.EMAIL_HOST_USER , ["utibesolomon17@gmail.com"]))
        try:
           send_mass_mail(datatuple)
           messages.success(request, 'your Order has been made')
        except:
           messages.error(request ,'Order wasnt processed')

        return redirect('shoppingbag')
        
        
    
    context = {'order': order, 'location':location1}
    
    return render(request, 'base/checkout.html', context)

def Pendingorders(request):
    page = 'orders'

    if not request.user.is_staff :
        return HttpResponse('404 page not found')
    
    orders = Order.objects.filter(complete = True)
    context ={'orders': orders, 'page': page}
   
    return render(request, 'base/orderview.html', context)

def Completeorders(request):
    data = json.loads(request.body)
    Orderid = data['order']
    action = data['action']
    order = Order.objects.get(id =  Orderid)
    if action == 'complete':
        order.delete()
    print(data)
    return JsonResponse('Order has been completed' , safe=False)

def Createitems(request):
    if request.user.is_staff:
       form = itemCreation()
       if request.method == 'POST':
           form = itemCreation(request.POST, request.FILES)
           if form.is_valid():
               try:
                  form.save()
                  messages.success(request,'Item has been added')
                  return redirect('shop')
               except:
                   messages.error(request, 'couldnt save item')
                   
              
       context = {'form':form}
       return render(request,'base/createitem.html',context)
    else:
        return HttpResponse('404 page not found')
def Updateitems(request,pk):
    if  not request.user.is_staff:
        return HttpResponse('404 page not found')
    else:
        item = Item.objects.get(id=pk)
        form = itemCreation( instance = item)
        if request.method == 'POST':
            form = itemCreation(request.POST, request.FILES, instance = item)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, 'item was updated')
                    return redirect('shop')
                except:
                    messages.error('item couldnt be updated')
        context = {'form': form}
        return render(request,'base/createitem.html',context)

def deleteitems(request):
    data = json.loads(request.body)
    itemid = data['itemid']
    action = data['action']
    item = Item.objects.get(id = itemid)
    if action == 'delete':
        item.delete()
        messages.success(request, 'item succesfully deleted')

    return JsonResponse('Item was deleted', safe = False)



