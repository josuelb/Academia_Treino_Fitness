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
