from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
#from allauth.account.signals import user_signed_up


class CustomUserManager(UserManager):
    def create(self, email, password=None, **extra_fields):
        user = super().create(email, password=password, **extra_fields)
        CoinFind.objects.create(userPesquisa=user, pesquisas=3)
        return user


class CoinFind(models.Model):
    pesquisas = models.IntegerField(default=0)
    userPesquisa = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.userPesquisa} tem {self.pesquisas} pesquisas' 
    
   

class FindCitation(models.Model):
    research_done = models.CharField(max_length=10)
    userPesquisa = models.ForeignKey(User, on_delete=models.CASCADE)


