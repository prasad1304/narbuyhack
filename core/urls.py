from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
  
    AddCouponView,
    RequestRefundView,

    products,
    SearchResultsView,
    UserProfielView,
    OrderDetail,
    showShops,
    PaymentView,
    handlerequest,
    success
    
   
)

from django.conf.urls import url


app_name = 'core'

urlpatterns = [
    path('', HomeView, name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', products, name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
  
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('search/', SearchResultsView, name='search_results'),
    path('user-profile/', UserProfielView, name="profile"),
    path('order-detail/', OrderDetail, name="order_detail"),
    path('shop-list/<str:shop>/', showShops, name="shop-list"),
    path('payment/<payment_option>/', PaymentView, name='payment'),
    path("handlerequest/", handlerequest, name="HandleRequest"),
    path('success/',success,name="success")

 

]
