from dotenv import load_dotenv
import os, json, requests

load_dotenv()

class Get_Elements:

	def GET_ALL_CATEGORIES(self):
		url = os.getenv('GET_ALL_CATEGORIES')
		payload = json.dumps({})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)

	def GET_LIST_SUBCATEGORIES(self,pk):
		url = os.getenv('GET_LIST_SUBCATEGORIES')
		payload = json.dumps({"pk_category": pk})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)

	def LIST_PRODUCTS(self,pk,price_top,price_low):
		url = os.getenv('LIST_PRODUCTS')
		payload = json.dumps({
		  "subcategory": pk,
		  "price_top": price_top,
		  "price_low": price_low
		})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)

	def GET_LIST_PRODUCT_BY_COMPANY(self,pk):
		url = os.getenv('GET_LIST_PRODUCT_BY_COMPANY')
		payload = json.dumps({
		  "company": pk
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)


	def GET_DETAIL_PRODUCT(self,pk):
		url = os.getenv('GET_DETAIL_PRODUCT')
		payload = json.dumps({
			"product": pk
		})
		headers = {
		'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)

	def CREATE_ORDER(self,info):
		url = "http://localhost:9090/order/CREATE_ORDER/"
		data = {}
		_data = []
		for i in info:
			_data.append(
				{
		      "name": "Harina Pan",
		      "price": 3200,
		      "quanty": 1,
		      "shipping": 0,
		      "user": 1
		    }
			)
		payload = json.dumps({
		  "order": [
		    {
		      "name": "Harina Pan",
		      "price": 3200,
		      "quanty": 1,
		      "shipping": 0,
		      "user": 1
		    }
		  ]
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)

		print(response.text)