from rest_framework import serializers

class SentimentSerializer(serializers.Serializer):
    sentence = serializers.CharField(max_length=5000)
