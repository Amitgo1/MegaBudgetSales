from django.shortcuts import render
from main.utils import outer_func

@outer_func
def products(request):
    return render(request,'products/products.html',{"login":True})
