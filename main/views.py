from django.contrib.auth.hashers import check_password,make_password                         
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from main.models import MyUser
from main.utils import outer_func

@outer_func
def index(request):
    return render(request,'main/index.html',{"login":True})


def register(request):
    
    if request.method == "POST":
      name  = request.POST.get("name")
      email  = request.POST.get("email")
      phone  = request.POST.get("phone")
      password  = request.POST.get("password")
      
      password = make_password(password)
      
      
      MyUser.objects.create(username = name, email = email, phone = phone, password = password)
    return render(request,'main/register.html')

def login3(request):
    errormessage = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            obj = MyUser.objects.get(username__iexact = username)
            print(password,obj.password)
            ismatched = check_password(password, obj.password)
            print(ismatched)
            if ismatched:
                request.session['username'] = username
                return redirect('index')
            else:
                errormessage = "username or password is invalid"
                
        except ObjectDoesNotExist:
            errormessage = "username or password is invalid"
    return render(request,'main/logintest.html',{"errormessage":errormessage})


def logout1(request):
    if 'username' in request.session:
        del request.session["username"]
    return redirect('login3')
            
        

# def index(request):
#     if request.user.is_authenticated:
#         return render(request,'main/index.html',{"login":True})
#     else:
#         return redirect("login")


# def login_page(request):
#     if request.method == "POST":
#         uname = request.POST.get("uname")
#         pw = request.POST.get("psw")
#         user = authenticate(request, username = uname, password = pw)
        
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             return render(request,'main/login.html',{"errormessage":"username or password Invalid"})
            
#     return render(request,'main/login.html')


# def logout_page(request):
#     logout(request)
#     return redirect("login")
