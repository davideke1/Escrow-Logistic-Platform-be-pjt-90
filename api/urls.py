from .views import CustomerCreateAPIView, LoginAPIView, LogoutAPIView, ProductInfoAPIView, SellerInfoAPIView, VendorCreateAPIView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('vendor-register/', VendorCreateAPIView.as_view(), name='vendor_register'),
    path('customer-register/', CustomerCreateAPIView.as_view(), name='customer_register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add-seller-info/', SellerInfoAPIView.as_view()),
    path('add-product-info/', ProductInfoAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
]