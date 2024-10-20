from rest_framework import serializers

class ChatSerializer(serializers.Serializer):
    prompt = serializers.CharField(required=True, max_length=500)