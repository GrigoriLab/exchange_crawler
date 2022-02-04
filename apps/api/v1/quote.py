from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.quote.models import Quote
from apps.quote.serializers import QuoteSerializer
from apps.quote.tasks import crawler


class QuoteView(APIView):

    def get(self, request):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    def post(self, request):
        crawler.delay()
        return Response({"info": "crawler manually triggered!"},
                        status=status.HTTP_201_CREATED)
