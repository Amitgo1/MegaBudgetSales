from django.shortcuts import render
from main.utils import outer_func



@outer_func
def category(request):
    return render(request,'category/category.html',{"login":True})
