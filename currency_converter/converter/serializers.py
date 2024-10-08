from rest_framework import serializers

class CurrencyConverterSerializer(serializers.Serializer):
    base_currency = serializers.CharField(max_length=3)
    target_currency = serializers.CharField(max_length=3)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)