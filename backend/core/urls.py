from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from searchcitation.views import SearchViewSet
from core.views import UserViewSet, GroupViewSet
from searchcoin.views import CoinFindViewSet
from productcj.views import CoinCJViewSet, BuyCoinCJViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'searchs', SearchViewSet)
router.register(r'coins', CoinFindViewSet)
router.register(r'products', CoinCJViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('busca/', SearchViewSet.as_view({'post': 'search_citation'}), name='serach-citation'),
]
