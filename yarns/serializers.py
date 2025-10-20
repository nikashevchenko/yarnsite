from rest_framework import serializers
from yarns.models import Yarn, Brand, Material, Product


class YarnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yarn
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



