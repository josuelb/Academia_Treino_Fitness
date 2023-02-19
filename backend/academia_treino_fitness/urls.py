from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView
)
from .views import *

router = routers.DefaultRouter()
router.register(r'clientes', ClienteView, basename='APIClientes')
router.register(r'funcionarios', FuncionarioView, basename='APIFuncionarios')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('api/academia-treino-fitness/clientelist/', ClienteList.as_view(), name='Clientelist'),
    path('api/academia-treino-fitness/funcionariolist/', FuncionarioList.as_view(), name='FuncionarioList'),
    path('api/academia-treino-fitness/cargos/', CargoView.as_view(), name='cargos'),
    path('api/academia-treino-fitness/planos/', PlanoView.as_view(), name='planos'),
    path('api/academia-treino-fitness/', include(router.urls)),
    path('api/academia-treino-fitness/authentication/', Authentication, name='Authentication'),
    path('api/academia-treino-fitness/create_user/', CreateUser, name="CreateUser")
]