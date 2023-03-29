from rest_framework import viewsets
from .serializers import CoinFindSerializer
from .models import CoinFind


class CoinFindViewSet(viewsets.ModelViewSet):
    queryset = CoinFind.objects.all()
    serializer_class = CoinFindSerializer
