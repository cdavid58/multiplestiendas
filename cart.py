from django.http import HttpResponseRedirect
from decimal import Decimal
from django.conf import settings
from datetime import date
from datetime import datetime

class Carrito(object):
	def __init__(self,request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart
		self.request = request

	def save(self):
		self.session[settings.CART_SESSION_ID]=self.cart
		self.session.modified = True

	def add(self,product,quanty):
		total = float(product['price']) * float(quanty)
		_id = str(product['pk'])
		if str(_id) in self.cart:
			if int(quanty) == 0:
				del self.cart[_id]
				if int(self.request.session['carrito']) > 0:
					n = int(self.request.session['carrito']) - 1
					self.request.session['carrito'] = n
				self.save()
			else:
				print(quanty)
				total = float(product['price']) * float(quanty)
				self.cart[_id]['quanty'] = quanty
				self.cart[_id]['total'] = total
				self.save()

		else:
			if int(quanty) >= 1:
				self.request.session['carrito'] +=1
				self.cart[_id] = {'pk':product['pk'],'product':product['name'],'quanty':quanty,'price':product['price'],
														'total':total,'img':product['img'],'shipping_price':product['shipping'],'company':product['pk_company']
													  }
		print(self.cart)
		self.save()

	def remove(self,product):
		product_id = str(product['pk'])
		if product_id in self.cart:
			del self.cart[product_id]
			self.request.session['carrito'] -=1
			self.save()

	def __iter__(self):
		product_ids = self.cart.keys()
		for item in self.cart.values():
			yield item


	def __len__(self):
		return sum(int(item['quanty']) for item in self.cart.values())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True