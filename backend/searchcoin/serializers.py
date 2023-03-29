from rest_framework import serializers
from .models import CoinFind


class CoinFindSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoinFind
        fields = ['id', 'pesquisas', 'userPesquisa']