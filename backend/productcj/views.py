from rest_framework import viewsets
from .serializers import CoinCJSerializer, BuyCoinCJSerializer
from .models import CoinCJ, BuyConCJ


class CoinCJViewSet(viewsets.ModelViewSet):
    queryset = CoinCJ.objects.all()
    serializer_class = CoinCJSerializer


class BuyCoinCJViewSet(viewsets.ModelViewSet):
    queryset = BuyConCJ
    serializer_class = BuyCoinCJSerializer
