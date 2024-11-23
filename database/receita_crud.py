from .data import Receita, Usuario, Instituicao, session
from InquirerPy import prompt


def usuario_menu():
    names = [i.nome for i in session.query(Usuario).all()]
    users_menu = [
        {
            'type': 'list',
            'message': 'Selecione o usuário abaixo',
            'choices': names,
            'name': 'user'
        }
    ]
    resultado = prompt(users_menu)
    return resultado['user']


def instituicao_menu():
    inst_names = [i.nome for i in session.query(Instituicao).all()]
    inst_menu = [
        {
            'type': 'list',
            'message': 'Selecione a instituição abaixo',
            'choices': inst_names,
            'name': 'inst'
        }
    ]
    resultado = prompt(inst_menu)
    return resultado['inst']

class ReceitaCRUD:
    def receita_create(self):
        user_name = usuario_menu()
        inst_name = instituicao_menu()
        user = session.query(Usuario).filter_by(nome=user_name).one()
        inst = session.query(Instituicao).filter_by(nome=inst_name).one()
        valor = float(input('Valor da transação: '))
        if type(valor) != float:
            return print('Erro! Valor inválido')
        try:
            create = Receita(user.id, inst.id, valor)
            session.add(create)
            session.commit()
        except Exception as e:
            return print('Erro, não foi possível realizar o cadadastro! \n', e)
        return print('Transação cadastrada com sucesso!')