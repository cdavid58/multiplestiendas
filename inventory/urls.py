from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Categories/$',Categories,name="Categories"),
		url(r'^GET_LIST_SUBCATEGORIES/(\d+)/$',GET_LIST_SUBCATEGORIES,name="GET_LIST_SUBCATEGORIES"),
		url(r'^LIST_PRODUCTS/(\d+)/$',LIST_PRODUCTS,name="LIST_PRODUCTS"),
		url(r'^GET_LIST_PRODUCT_BY_COMPANY/(\d+)/$',GET_LIST_PRODUCT_BY_COMPANY,name="GET_LIST_PRODUCT_BY_COMPANY"),
		url(r'^GET_DETAIL_PRODUCT/(\d+)/$',GET_DETAIL_PRODUCT,name="GET_DETAIL_PRODUCT"),
		url(r'^Add_Cart/$',Add_Cart,name="Add_Cart"),
		url(r'^Cart/$',Cart,name="Cart"),
		url(r'^Remove_Product/$',Remove_Product,name="Remove_Product"),
		url(r'^CheckOut/$',CheckOut,name="CheckOut"),
]