from rolepermissions.roles import AbstractUserRole

class Funcionario(AbstractUserRole):
    available_permissions = {
        'adicionar_dvd': True,
        'deletar_dvd': True,
        'home_funcionarios': True,
        'consulta_funcionarios': True,
    }
    
class Cliente(AbstractUserRole):
    available_permissions = {
        'remover_dvd': True,
        'inserir_lista_espera': True,
        'devolver_dvd': True,
        'efetivar_pagamento_dvd': True,
        'dvds_alugados': True,
        
    }