from .data import Instituicao, session
from os import system

class InstituicaoCRUD:
    def instituicao_crate(self):
        nome = input('Nome da instituição: ').title().strip()
        system('clear')
        tipo = input('Tipo de transação: ').capitalize().strip()
        system('clear')
        descricao = input('Descrição da transação: ').capitalize().strip()
        system('clear')
        try:
            create = Instituicao(nome, tipo, descricao)
            session.add(create)
            session.commit()
            return print(f'{create.nome} \n-Cadastrada com sucesso!')
        except:
            return print('Não foi possivel realizar o cadastro!')