from django.shortcuts import render
from main.utils import outer_func
from contact.models import Contact

@outer_func
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name,email)
        
        Contact.objects.create(name = name, email = email, phone = phone, message = message)
        
    return render(request,'contact/contact.html',{"login":True})
