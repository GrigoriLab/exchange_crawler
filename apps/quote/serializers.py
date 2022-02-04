from rest_framework import serializers

from apps.quote.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'
