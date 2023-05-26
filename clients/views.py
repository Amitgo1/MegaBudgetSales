from django.shortcuts import render
from main.utils import outer_func


@outer_func
def clients(request):
    return render(request,'clients/clients.html',{"login":True})
