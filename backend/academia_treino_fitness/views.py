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


class CargoView(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class PlanoView(viewsets.ModelViewSet):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer


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
def CreateUser(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = json.loads(request.body)["username"]
        password = json.loads(request.body)["password"]
        type = json.loads(request.body)["type"]

        user = User.objects.create_user(username=username, password=password)
        user.save()

        assign_role(user, type)

        return HttpResponse('Usuário salvo com sucesso')
