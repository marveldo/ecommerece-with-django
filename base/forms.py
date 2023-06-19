from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from base.models import Item


class Userupdatedform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
        labels = { 'username':'Name'}

    def __init__(self,*args, **kwargs):
        super(Userupdatedform,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':"input-loginform"})
class itemCreation(ModelForm):
    class Meta:
        model = Item
        fields = ['item_image','item_name','price','item_about','quantity_available']

    def __init__(self,*args,**kwargs):
        super(itemCreation,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input-loginform'})

