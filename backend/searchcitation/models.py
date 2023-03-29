from django.contrib.auth.models import User
from searchcoin.models import CoinFind
#from django.core.exceptions import ValidationError
from django.db import models


class Search(models.Model):
    query = models.CharField(max_length=200)
    citation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user} pesquisou por {self.query}"


