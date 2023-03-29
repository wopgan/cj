from rest_framework import serializers
from .models import Search


class SearchSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Search
        fields = ['id', 'query', 'created_at']