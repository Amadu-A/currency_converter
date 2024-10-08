from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CurrencyConverterSerializer
from .services import get_exchange_rate


class CurrencyConverterView(APIView):
    def post(self, request):
        serializer = CurrencyConverterSerializer(data=request.data)
        if serializer.is_valid():
            base_currency = serializer.validated_data['base_currency']
            target_currency = serializer.validated_data['target_currency']
            amount = serializer.validated_data['amount']

            # Получение курса валют
            rate = get_exchange_rate(base_currency, target_currency)
            if rate:
                converted_amount = float(amount) * rate
                return Response({
                    'base_currency': base_currency,
                    'target_currency': target_currency,
                    'amount': amount,
                    'converted_amount': converted_amount
                })
            else:
                return Response({"error": "Could not fetch the exchange rate."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
