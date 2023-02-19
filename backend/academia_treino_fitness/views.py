import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rolepermissions.roles import assign_role, get_user_roles

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from .serializers import *
from .models import *


# Views de sereialização da API
class ClienteView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class FuncionarioView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class CargoView(ListAPIView):
    serializer_class = CargoSerializer

    def get_queryset(self):
        queryset = Cargo.objects.all()
        return queryset


class PlanoView(ListAPIView):
    serializer_class = PlanoSerializer

    def get_queryset(self):
        queryset = Plano.objects.all()
        return queryset   
    

class ClienteList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClienteSerializer

    def get_queryset(self):
        username = self.request.user
        queryset = Cliente.objects.filter(user=username)
        return queryset


class FuncionarioList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FuncionarioSerializer

    def get_queryset(self):
        username = self.request.user
        queryset = Funcionario.objects.filter(user=username)
        return queryset


# Para fazer a authenticação do usuário
@csrf_exempt
def Authentication(request):
    if request.method == "POST":
        dados = request.body
        dados = json.loads(dados)

        user = authenticate(username=dados['username'], password=dados['password'])

        if user:
            get_roles = get_user_roles(user)[0]
            response = {
                'Authorization': 'Autenticado',
                'Group': get_roles.__name__,
                'Permissions': get_roles.__dict__['available_permissions']
            }
            return HttpResponse(json.dumps(response))
        else:
            response = {
                'Authorization': 'Usuário ou senha incorreta'
            }
            return HttpResponse(json.dumps(response))
    else:
        return HttpResponse('Só metodos POSTs')


# Para criar um usuário novo
@csrf_exempt
def CreateUser(self, request, *args, **kwargs):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        dado = json.loads(request.body)

        if dado['type'][0] == "Cliente":
            data = {
                "nome": dado["nome"],
                "sobrenome": dado["sobrenome"],
                "data_nasc": dado['data_nasc'],
                "cpf": dado["cpf"],
                "rg": dado['rg'],
                "user": dado['user'],
                "email": dado['email'],
                "password": dado['password'],
                "situacao": dado["situacao"],
                "objetivo": dado['objetivo'],
                "plano": dado['plano']
            }
            data = json.dumps(data)

            self.create(request=data, *args, **kwargs)

            user = User.objects.create_user(username=dado['user'], password=dado['password'])
            user.save()

            assign_role(user, dado['type'][1])
            return HttpResponse('Usuário salvo com sucesso')
