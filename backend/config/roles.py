from rolepermissions.roles import AbstractUserRole


class Executivo(AbstractUserRole):
    available_permissions = {
        'Can change cliente': True,
        'Can view cliente': True,
        'Can delete cliente': True,
        'Can change funcionario': True,
        'Can view funcionario': True,
        'Can delete funcionario': True,
        'Can change cargo': True,
        'Can view cargo': True,
        'Can delete cargo': True,
        'Can change plano': True,
        'Can view plano': True,
        'Can delete plano': True
    }


class Gerente(AbstractUserRole):
    available_permissions = {
        'Can change cliente': True,
        'Can view cliente': True,
        'Can delete cliente': True,
        'Can change funcionario': True,
        'Can view funcionario': True,
        'Can change cargo': True,
        'Can view cargo': True,
        'Can delete cargo': True,
        'Can change plano': True,
        'Can view plano': True,
        'Can delete plano': True
    }


class Recepcao(AbstractUserRole):
    available_permissions = {
        'Can change cliente': True,
        'Can view cliente': True,
        'Can delete cliente': True,
        'Can view funcionario': True,
        'Can view cargo': True,
        'Can view plano': True
    }


class Cliente(AbstractUserRole):
    pass