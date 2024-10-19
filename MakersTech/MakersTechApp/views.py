from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Brand
from .serializers import BrandSerializer

# Create your views here.
class BrandView(viewsets.ViewSet):
    """
    A simple viewset for viewing all brands
    """

    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)