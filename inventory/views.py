from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv
from .get_element import Get_Elements
import os, json, requests
from cart import *

get_elements = Get_Elements()


def Categories(request):

	return render(request,'inventory/categories.html',{
		'categories':get_elements.GET_ALL_CATEGORIES()
		})

def GET_LIST_SUBCATEGORIES(request,pk):
	return render(request,'inventory/subcategories.html',{'subcategories':get_elements.GET_LIST_SUBCATEGORIES(pk)})

def LIST_PRODUCTS(request,pk):
	list_product = get_elements.LIST_PRODUCTS(pk,None,None)
	if request.is_ajax():
		data = request.GET
		if int(data['price_low']) == 0:
			list_product = get_elements.LIST_PRODUCTS(pk,None,None)
			print(list_product)
		elif int(data['price_low']) > 0:
			list_product = get_elements.LIST_PRODUCTS(pk,data['price_top'],data['price_low'])
		return HttpResponse(json.dumps(list_product))
	return render(request,'inventory/list_product.html',{'features':list_product[0]['features'][0]})

def GET_LIST_PRODUCT_BY_COMPANY(request,pk):
	list_product = get_elements.GET_LIST_PRODUCT_BY_COMPANY(pk)
	if request.is_ajax():
		return HttpResponse(json.dumps(list_product))
	return render(request,'inventory/list_product_company.html',{'features':list_product[0]['features'][0]})


def GET_DETAIL_PRODUCT(request,pk):
	product = get_elements.GET_DETAIL_PRODUCT(pk)
	gallery = product['gallery']
	return render(request,'inventory/details_product.html',{'product':product['product'],'gallery':gallery})


def Add_Cart(request):
	cart = Carrito(request)
	product = get_elements.GET_DETAIL_PRODUCT(request.GET['pk_product'])['product']
	quanty = int(request.GET['quanty'])
	if quanty <= 0:
		cart.remove(product)
	else:
		cart.add(product,quanty)
	return HttpResponse(request.session['carrito'])


def Cart(request):
	cart = Carrito(request)
	shipping = 0
	subtotal = 0
	for i in cart:
		shipping += float(i['shipping_price'])
		subtotal += float(i['total'])
	total = shipping + subtotal
	return render(request,'inventory/cart.html',{'cart':cart,'subtotal':subtotal, 'shipping':shipping, 'total':total})

def Remove_Product(request):
	cart = Carrito(request)
	product = get_elements.GET_DETAIL_PRODUCT(request.GET['pk_product'])['product']
	print(product,'PRODUCTO')
	cart.remove(product)
	return HttpResponse(request.session['carrito'])


def CheckOut(request):
	if request.method == 'POST':
		print(request.POST)
	cart = Carrito(request)
	shipping = 0
	subtotal = 0
	for i in cart:
		shipping += float(i['shipping_price'])
		subtotal += float(i['total'])
	total = shipping + subtotal
	return render(request,'inventory/checkout.html',{'cart':cart,'subtotal':subtotal, 'shipping':shipping, 'total':total})

