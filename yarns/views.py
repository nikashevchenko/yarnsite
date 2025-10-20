from itertools import product

from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from yarns.models import Yarn, Brand, Product
from yarns.serializers import YarnSerializer, BrandSerializer, ProductSerializer
from rest_framework import status

class YarnsListViews(APIView):
    def get(self, request):
        yarns = Yarn.objects.all()
        serializer = YarnSerializer(yarns, many=True)
        return Response(serializer.data)

class YarnsDetailViews(APIView):
    def get_object (self, pk):
        try:
            return Yarn.objects.get(pk=pk)
        except Yarn.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        yarn = self.get_object(pk)
        serializer = YarnSerializer(yarn)
        return Response(serializer.data)


class BrandListViews(APIView):
    def get(self, request,format=None):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

class BrandDetailViews(APIView):
    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

class ProductListViews(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailViews(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


