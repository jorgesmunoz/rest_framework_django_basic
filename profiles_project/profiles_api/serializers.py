from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serialize a name for testing out APIView"""
    name = serializers.CharField(max_length=10)
