from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate

from .forms import RegistrationForm

# Create your views here.

def home(request):
    return render(request,'home.html')

class Register(View):
    def get(self,request):
      form = RegistrationForm()
      return render(request,'register.html',{'form':form})
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
         messages.success(request, 'congrats !!! REGISTERED SUCCESSFULLY')
         form.save()
         return render(request,'register.html',{'form':form})

# class Logout(View):

#     def get(self,request):
#         logout(request)
#         return HttpResponseRedirect('home/')





# class Register(View):
#     template_name="register.html"
#     def get(self,request):
#         return render(request,self.template_name)

#     def post(self,request):
#         username= request.POST.get('username')
#         email= request.POST.get('email')
#         password=request.POST.get('password')
#         confirmpass=request.POST.get('password1')
#         try:
#             User.objects.get(email=email)
#             return HttpResponse("email already exists")

#         except Exception as e:
#             if password== confirmpass:
#                 u=User.objects.create(username=username,email=email)
#                 u.set_password(password)
#                 u.save()
#                 messages.success(request, 'Now you can login')
#                 return HttpResponseRedirect('login')

# class Login(View):
#     def get(self,request):
#         print("in get method")
      
#         return render(request,'login.html')
#     def post(self,request):
        
#         print(request.POST)
#         email= request.POST['email']
#         password = request.POST['password']
#         print("in post method")
#         print("email",email,"password",password)

#         try:
#             user = User.objects.get(email=email)
#             print("user value",user)
#             user = authenticate(username= user.username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'logged in')
#                 print("logged in user is ",user)
#                 return render(request,'header.html',locals())
#             else:
#                  messages.error(request, "Invalid Credentials")
#                  return HttpResponseRedirect("login")
#         except Exception as e:
#             print(e)
#             messages.error(request, 'User not exists with given username')
#             return HttpResponseRedirect("login")
