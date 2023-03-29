from django.db import models
from searchcoin.models import CoinFind
from django.contrib.auth.models import User


class CoinCJ(models.Model):
    class Meta:
        verbose_name = 'CoinCJ'
        verbose_name_plural = 'CoinsCJ'
        
    product = models.CharField(max_length=100, verbose_name='Nome do Produto')
    qnt = models.IntegerField(default=0, verbose_name='Quantidade Pesquisa')
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product} vale {self.qnt} pesquisas.'


class BuyConCJ(models.Model):
    class Meta:
        verbose_name = 'BuyCoinCJ'
        verbose_name_plural = 'BuyCoinsCJ'

    buying = models.ForeignKey(CoinCJ, on_delete=models.CASCADE, verbose_name='Produto')
    custumeruser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário Comprador')

    def __str__(self):
        return f'{self.custumeruser}, comprou {self.buying}.'

    @staticmethod
    def update_coinfind(user, qnt):
        CoinFind.objects.filter(userPesquisa=user).update(pesquisas=models.F('pesquisas') + qnt)
    
    def save(self, *args, **kwargs):
        self.qnt = self.buying.qnt
        self.update_coinfind(self.custumeruser, self.qnt)

