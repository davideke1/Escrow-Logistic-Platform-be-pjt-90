#from django.contrib.auth import authenticate, get_user_model
#from django.contrib.auth.tokens import PasswordResetTokenGenerator
#from django.utils.encoding import force_str
#from django.utils.http import urlsafe_base64_decode
from django.db import models
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
##from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from api.models import Product, User, Customer, Vendor, sellerInfo


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        customer = Customer.objects.create(**validated_data, user=user)
        customer.save()
        return customer

class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    business_name = serializers.CharField()

    class Meta:
        model = Vendor
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        vendor = Vendor.objects.create(**validated_data, user=user)
        vendor.save()
        return vendor


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    tokens = serializers.CharField(max_length=255, read_only=True)

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'tokens': user.tokens
        }

        return super().validate(attrs)

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = sellerInfo
        fields = '__all__'
        
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('brief_description', 'price', 'quantity')
