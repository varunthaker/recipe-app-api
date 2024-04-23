from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.Serializer):

    class Meta:
        model = Recipe
        fiels = ['id', 'title', 'link','time_minutes', 'price']
        read_only_fields = ['id']