from .data import Usuario, session
from os import system

class UsuarioCRUD:
    def usuario_create(self):
        nome = input('Nome completo: ').title().strip()
        system('clear')
        cpf = input('CPF: ').strip()
        system('clear')
        email = input('E-Mail: ').lower().strip()
        system('clear')
        senha = input('Senha: ').strip()
        
        try:
            create = Usuario(nome, cpf, email, senha)
            session.add(create)
            session.commit()
            system('clear')
            return print(f'{create.nome} \n-Cadastrado com sucesso!')
        except:
            return print('Não foi possivel realizar o cadastro!')