
from .models import Rubbish, Category
from rest_framework import serializers


class RubbishSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Rubbish
        fields = ('name', 'category')


class RubbishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'summary')

