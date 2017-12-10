from django.http import HttpResponse
from django.shortcuts import *
from django.views import View
from django.template import loader

from models import Model
from Products import Products
from Product import Product


def Hello(request):
    return HttpResponse("Welcome to Our pages")

def Contact(request):
    return HttpResponse("contact us")

def HomePage(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'home.html')

def ContactUs(request):
    return HttpResponse("Contact Us")

def Target(request):
    #return render(request,'home.html',{'name':'test'})
    t = loader.get_template('home.html')
    val = request.GET['txtName']
    c = {'name' : val};
    return HttpResponse(t.render(c,request))

def StudentData(request):
    l = [3,2,3,4]
    average = sum(l)/len(l)

    m = Model()
    m.Name = "John"
    m.Faculty = "Math"
    m.grades = l;
    m.average = sum(l)/len(l)

    #return render(request,'StudentData.html',{'name':'Avi','faculty':'Math','grades':l,'average':average})
    return render(request, 'StudentData.html', {'model': m})

def products(request):

    p = Product()
    p.ProductID = 1
    p.name = "test1"
    p.price = 10
    p.IsExists = True

    p1 = Product()
    p1.ProductID = 2
    p1.name = "test2"
    p1.price = 100
    p1.IsExists = True

    plist = Products()
    plist.products = [p,p1]

    return render(request,'products.html',{'p':plist})

def product(request,id):

    #p = Product()
    #p.IsExists = True
    #p.price = 0
    #p.ProductID = 20
    #p.name = "zzzzzz"

    #return render(request,'product.html',{'product':p})
    return HttpResponse('Product')

