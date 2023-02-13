from django.db import models


# Modelos de bancos de dados
def Photo(instance, filename):
    return f'{instance.Pessoa}-{filename}'


class Pessoa(models.Model):
    foto = models.ImageField(upload_to=Photo, blank=True, null=False)
    nome = models.CharField(max_length=100, null=False)
    sobrenome = models.CharField(max_length=100, null=False)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=11, null=False, unique=True)
    rg = models.IntegerField(null=False, unique=True)

    class Meta:
        abstract = True


class Cargo(models.Model):
    nome = models.CharField(max_length=50)
    remuneracao = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome}'


class Plano(models.Model):
    plano = models.CharField(max_length=50)
    valor = models.IntegerField(max_length=10)

    def __str__(self):
        return f'{self.plano}'


class Cliente(Pessoa):
    user = models.CharField(max_length=50, null=False, unique=True)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=25, null=False)
    situacao = models.CharField(max_length=7, null=False)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE, default='Mensal')
    objetivo = models.CharField(max_length=100)


class Funcionario(Pessoa):
    user = models.CharField(max_length=50, null=False, unique=True)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=25, null=False)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, default=None)

