#from django.shortcuts import render
import openai
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from searchcoin.models import CoinFind
from .models import Search
from .serializers import SearchSerializers


openai.api_key = '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'


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializers


    @action(detail=False, methods=['POST'])
    def search_citation(self, request):


        user = request.user
        coinfind = CoinFind.objects.get(userPesquisa=user)



        if coinfind.pesquisas > 0:

            query = request.data.get('busca_citacao')
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"liste 1 citação sobre '{query}' em livros a partir de 2015 até o ano atual, citando autor, nome do livro, editora, site da editora e ano.",
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )

            result = {
                'citacao': response.choices[0].text,
            }

            result['citacao'] = result['citacao'].replace('\\', '').replace('\n', '').replace('\n2', '')

            Search.objects.create(
                query=query,
                citation=result['citacao'],
                user=user,
            )

            coinfind.pesquisas -= 1
            coinfind.save()

            return Response(result)

        else:

            result = {
                'error': 'Adquira mais CoinFinds'
            }

            return Response(result)
