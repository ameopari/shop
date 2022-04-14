from asyncio import exceptions
from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from .models import *
from .forms import RegistrationForm
import json
from math import ceil
import stripe
from django.conf import settings
from django.views.generic.base import TemplateView


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def home(request):
    intemvount = CartItem.objects.all().count()
    p = Products.objects.all()
    return render(request,'frontend/home.html',locals())

def index(request):
    return render(request,'backend/index2.html')

# class Register(View):
#     def get(self,request):
#       form = RegistrationForm()
#       return render(request,'frontend/register.html',{'form':form})
#     def post(self,request):
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#          messages.success(request, 'congrats !!! REGISTERED SUCCESSFULLY')
#          form.save()
#         return render(request,'frontend/register.html',{'form':form})

class Register(View):
    def get(self,request):
        print("ggggggggggg")
        return render(request,'backend/register.html')


    def post(self,request):
        print("in post method")
        username= request.POST.get('username')
        password=request.POST.get('password')
        confirmpass=request.POST.get('repeatpassword')
        email= request.POST.get('email')
        print(request.POST)

        try:
            User.objects.get(email=email)
            return HttpResponse("email already exists")
        except User.DoesNotExist:
            if password == confirmpass:
                u=User.objects.create(username=username,email=email)
                u.set_password(password)
                u.save()
                messages.success(request, 'Now you can login')
                return HttpResponseRedirect('login')
            else:
                messages.error(request, 'password doesnt match')
                return HttpResponse("password doesnot match")
        except Exception as e:
            print(e)
            return HttpResponse("facing exception")
           




class Login(View):
    def get(self, request):
        return render(request,'backend/login.html')

    def post(self,request):
        email= request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email).first()
        print(user,'==========================user')
        user = authenticate(username=user.username, password=password)
        print(user,'=========user')
        if user is not None:
            login(request, user)
            messages.success(request, 'logged in')
            print("logged in user is ",user)
            return render(request,'backend/index.html',locals())
        else:
                messages.error(request, "Invalid Credentials")
                return HttpResponseRedirect("login")
        




class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("login")    



class Addproduct(View):
    def get(self,request):
        print(request.user,'============')
        if request.user.is_superuser == True:
            get_all_cat = Categories.objects.all()
            print(get_all_cat,'===========')
            return render(request,'backend/nalika/product-edit.html',locals())
        else:
            messages.error(request, 'User not exists')
            return HttpResponse("ADD")
    def post(self,request):
        print(request.POST)
        
        userr = User.objects.get(username=request.user)
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        cat = request.POST.get('categories')
        cat_id =  Categories.objects.get(id=cat)
        title = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        obj = Products(user=userr,price=price,quantity=quantity,category=cat_id,title=title,description=description,image=image)
        obj.save()
        messages.success(request, 'product saveed !')
        return render(request,'backend/nalika/product-edit.html',locals())

def Cate(request):
   cat = Categories.objects.all()
   context_dict = {'categories': cat}

   return render(request,'backend/product-cat.html',context_dict)
    

def upd(request,id):
    if request.method == "POST":
        print(request.POST)

        try:
            product = Products.objects.get(id = id)
            product.img = request.FILES.get('image')
            product.user = request.POST.get('user')
            product.price = request.POST.get('price')
            product.quantity = request.POST.get('quantity')
            product.category = request.POST.get('category')
            product.save()
            
            
        except Exception as e:
            return HttpResponse('UPDATED')
        
        
    else:
        p = Products.objects.get(id = id)
        print(p,'ppppppppppppppppppppppp')
        test = {'p':p}
        return render(request,"backend/nalika/product-detail.html",test)

def delete(request, id):
    if request.method == 'POST':
        p = User.objects.get(pk=id)
        p.delete()
    return HttpResponseRedirect('show')
    


def Show(request):
     tesr=Products.objects.all()
     context = {'products': tesr}
     print(context,'===================context')
    #  print(context)
    #  return render(request,'backend/nalika/product-list.html',context)
     return render(request,"backend/nalika/product-list.html",context)


class addtocart(View):
    def get(self,request):
        products = CartItem.objects.all()
        return render(request,'backend/nalika/product-cart.html', locals())
    
    def post(self,request):
        product_id = request.POST.get('product_id')
        print(product_id)
        qty =  request.POST.get('qty')
        print(qty)

        try:        
            cart, created = Cart.objects.get_or_create(user=request.user)
            product = Products.objects.get(pk=product_id)
            if int(qty) <= int(product.quantity):
                item, item_created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
                item.quantity = qty
                item.save()
                product.quantity = product.quantity - int(qty)
                product.save()
                status = True
                msg = "Saved"
            else:
                status = False
                msg = "Quantity should be less than total qty"
        except Products.DoesNotExist:
            status = False
            msg = "Invalid Product"
        return redirect('addtocart')      
        return HttpResponse(json.dumps({'status': status, 'msg':msg}), 
            content_type='application/json')


# def add_to_cart(request):
#     user = request.user
#     product_id = request.Get.get("product_id")
#     product = product.objects.get(id=product_id)
#     Cart(user=user,product=product).save()
#     return redirect("addtocart")

# def show_cart(request):
#     if request.user.is_authenticated:
#         user = request.user
#         Cart = CartItem.objects.filter(user=user)
#         con_dict = {'carts': Cart }
        

#         return render(request,'frontend/header.html',con_dict)

# def show_cart(request):
#     if request.user.is_authenticated:
#         cart = Cart.objects.filter(user=request.user.id)
#         products = Products.objects.filter(cart=cart)
#         total = 0
#         count = 0
#         for Carts in Cart:
#             total += (Carts.products.price * Carts.quantity)
#             count += Carts.quantity
#         context = {
#             'cart': Cart,
#             'total': total,
#             'count': count,
#         }
#         return render(request, 'frontend/header.html',context)
#     else:
#         return redirect('home/')




# def cart(request):
#     if request.user.is_authenticated:
#         cart = Cart.objects.filter(user=request.user.id, active=True)
#         orders = BookOrder.objects.filter(cart=cart)
#         total = 0
#         count = 0
#         for order in orders:
#             total += (order.book.price * order.quantity)
#             count += order.quantity
#         context = {
#             'cart': orders, 
#             'total': total,
#             'count': count,
#         }
#         return render(request, 'store/cart.html', context)
#     else:
#         return redirect('index') 



    



# class Remove_from_cart(View):

#     def post(self,request):
#         product_id = request.POST.get('product_id')
#         try:        
#             product = Products.objects.get(pk=product_id)
#             item = CartItem.objects.get(cart__user=request.user, product_id=product_id)
#             qty = item.quantity
#             item.delete()
#             product.quantity = product.quantity + int(qty)
#             product.save()
           
#         except Products.DoesNotExist:
           
#          return HttpResponse('home/')


class Payment(TemplateView):
    template_name="backend/nalika/product-payment.html"

    def get(self,request):
        cart = Cart.objects.filter(user=request.user, is_submit=False).last()
        print(cart,'========cart')
        return render(request,self.template_name, locals())

    def post(self,request):
        address = request.POST.get('addr')
        cart_id = request.POST.get('cart_id')
        print(address)
        print(cart_id)
        data = Cart.objects.filter(id= cart_id).update(Address=address)
    

# class Payment(View):

#     # def get(self,request):
#     #    cartitem = CartItem.objects.all()
#     #    return render(request,'backend/nalika/product-payment.html', locals())
#     def post(self,request):
        
#         print(request.POST)
#         price_id = request.POST.get('price_id')
#         amount = request.POST.get('amout')
#         print(price_id,'guyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')

#         stripe.api_key = settings.STRIPE_SECRET_KEY

#         try:
#             session = stripe.checkout.Session.create(
#             success_url='http://127.0.0.1:8000/success/?session_id={CHECKOUT_SESSION_ID}&pid='+str(price_id),
#             cancel_url='http://127.0.0.1:8000/cancel',
#             payment_method_types=['card'],
#             mode='payment',
#              line_items=[
#                     {
#                         'name': 'T-shirt',
#                         'quantity': 1,
#                         'currency': 'inr',
#                         'amount': 2000,
#                     }]
#         )
#         except exceptions as e:
#             print(e,'======================gvhjjff')
 
        # return redirect('home/')


class ShowProduct(View):

    def get(self,request):
       cartitem = CartItem.objects.all()
       return render(request,'backend/nalika/payment.html', locals())
    def post(self,request):
        
        print(request.POST)
        # price_id =  'price_1KC2JXSJi6pCV3fKSG57y83k'
        price_id = request.POST.get('price_id')
        print(price_id)

        stripe.api_key = settings.STRIPE_SECRET_KEY

        session = stripe.checkout.Session.create(
            success_url='http://127.0.0.1:8000/success/?session_id={CHECKOUT_SESSION_ID}&pid='+str(price_id),
            cancel_url='http://127.0.0.1:8000/cancel',
            payment_method_types=['card'],
            mode='payment',
             line_items=[
                    {
                        'name': 'T-shirt',
                        'quantity': 1,
                        'currency': 'inr',
                        'amount' : 2000
                    }]
        )
        response = {
            'status':True,
            'session_url':session.url
        }
        # return redirect(session.url, code=303)
        return HttpResponse(json.dumps(response), content_type='application/json')
  
    



