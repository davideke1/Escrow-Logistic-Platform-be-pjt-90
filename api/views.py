from api.models import Product
from api.serializers import CustomerSerializer, LoginSerializer, ProductSerializers, SellerSerializer, VendorSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics, permissions, views
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser



# Create your views here.
class CustomerCreateAPIView(APIView):
    serializer_class = CustomerSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorCreateAPIView(APIView):
    serializer_class = VendorSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SellerInfoAPIView(APIView):
    serializer_class = SellerSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def product(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return JsonResponse(serializer.data, status=500)
