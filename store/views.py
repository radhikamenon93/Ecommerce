from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView
from store.models import Category,Product,cart,order
from store.forms import userreg,Loginform,orderform
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect("login")
    return wrapper

   
class home(ListView):
    model=Category
    template_name="store\index.html"
    context_object_name="categories"

class Productview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.filter(category_id=id)
        name=Category.objects.get(id=id)
        return render(request,"store\categorydetail.html",{"data":data,"name":name})    
    
class proddetailview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        pdata=Product.objects.filter(id=id)
        return render(request,"store\proddetail.html",{"pdata":pdata}) 

class Registerview(CreateView):  
    template_name="store/register.html"
    form_class=userreg
    model=User
    success_url=reverse_lazy("home")

class Loginview(View):
    def get(self,request,*args,**kwargs):
        form=Loginform
        return render(request,"store/login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pass1=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=uname,password=pass1)
            if user_obj:
                login(request,user_obj)
                return redirect("home")
            else:
                print("false")
            return redirect("login")  
class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("home")
    
class addtocartview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        cart.objects.create(item=data,user=request.user)
        print("added successfully")
        return redirect("home")

@method_decorator(signin_required,name="dispatch") 
class cartview(View):  
    def get(self,request,*args,**kwargs):
        data=cart.objects.filter(user=request.user)
        return render(request,"store/cart.html",{"data":data}) 
    
class cartdelview(View):
     def get(self,request,*args,**kwargs):
         id=kwargs.get("pk")
         cart.objects.get(id=id).delete()
         return redirect("home")


class orderview(View):   
    def get(self,request,*args,**kwargs):
        form=orderform()
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        return render(request,"store/orderform.html",{"form":form,"data":data}) 
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        form=orderform(request.POST)
        if form.is_valid():
            qs=form.cleaned_data.get("address")
            order.objects.create(order_item=data,customer=request.user,address=qs)
            return redirect("home")
        return redirect("cartview")

class orderlist(View):
    def get(self,request,*args,**kwargs):
        data=order.objects.filter(customer=request.user)
        return render(request,"store/orderview.html",{"data":data})    
class removeorder(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        order.objects.get(id=id).delete()
        return redirect("cart")    

        




    

