from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from escrowapi.views import (
    RegisterView,
    VendorCreateAPIView,
    CustomerCreateAPIView,
    LoginAPIView,
    PatientRetrieveUpdateAPIView, SetNewPasswordAPIView, LogoutAPIView, VerifyEmail, PasswordTokenCheckAPI
)

urlpatterns = [
     path('register/', RegisterView.as_view(), name='reg'),
    path('vendor-register/', VendorCreateAPIView.as_view(), name='vendor_register'),
    path('customer-register/', CustomerCreateAPIView.as_view(), name='customer_register'),
    path('update/<int:pk>/', PatientRetrieveUpdateAPIView.as_view(), name='update'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
    path('login/', LoginAPIView.as_view(), name='login12'),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # ('request-reset-email/', RequestPasswordResetEmail.as_view(),
    #     name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')

]
