from rest_framework import serializers
from .models import Brand, Feature, Product

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    model_brand = BrandSerializer()
    model_features = FeatureSerializer(many=True)
    class Meta:
        model = Product
        fields = "__all__"

        