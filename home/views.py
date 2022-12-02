from django.shortcuts import render
from dotenv import load_dotenv
import os, json, requests

load_dotenv()

def Index(request):
	if 'carrito' not in request.session:
		request.session['carrito'] = 0

	return render(request,'index.html',{'cat_more_search':GET_CATEGORY_MORE_SEARCHED(),
														'logo_company':GET_LOGO_COMPANY()
													})


def GET_CATEGORY_MORE_SEARCHED():
	url = os.getenv('GET_CATEGORY_MORE_SEARCHED')
	print(url)
	payload = "{}"
	headers = {
	  'Content-Type': 'text/plain'
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	return json.loads(response.text)


def GET_LOGO_COMPANY():
	url = os.getenv('GET_LOGO_COMPANY')
	payload = json.dumps({})
	headers = {'Content-Type': 'application/json'}
	response = requests.request("POST", url, headers=headers, data=payload)
	return json.loads(response.text)