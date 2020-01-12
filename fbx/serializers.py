from rest_framework import serializers
from .models import Fbx


class FbxSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        depth 	= 1
        model = Fbx
        fields = ('id','name','normals','bump', 'texture', 'status')
        read_only_fields = ('id','name','normals','bump', 'texture', 'status')
