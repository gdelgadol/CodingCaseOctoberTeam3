from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Brand, Feature, Product
from .serializers import BrandSerializer, FeatureSerializer, ProductSerializer

# Create your views here.
class BrandViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all brands
    """

    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class FeatureViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all features
    """

    queryset = Feature.objects.all()

    def list(self, request):
        serializer = FeatureSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all products
    """

    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)