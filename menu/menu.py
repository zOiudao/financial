from database.data import Usuario, Instituicao, session
from InquirerPy import prompt
from os import system


def usuario_menu(msg):
    names = [i.nome for i in session.query(Usuario).all()]
    users_menu = [
        {
            'type': 'list',
            'message': msg,
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


def receita_menu():
    pass


def despesa_menu():
    pass


def relatorio_menu():
    pass

def menu_principal():
    system('clear')
    from database.receita_crud import menu_receita_crud
    from database.usuario_crud import menu_usuario_crud
    from database.instituicao_crud import menu_instituicao_crud
    from database.despesa_crud import menu_despesa_crud
    from database.relatorio import menu_relatorio
    menu = [
        {
            'type': 'list',
            'message': 'Selecione uma das opções abaixo.',
            'choices': ['Usuário', 'Instituição', 'Receita', 'Despesa', 'Relatório', 'Sair'],
            'name': 'm'
        }
    ]
    resultado = prompt(menu)
    if resultado['m'] == 'Usuário':
        menu_usuario_crud()
    if resultado['m'] == 'Instituição':
        menu_instituicao_crud()
    if resultado['m'] == 'Receita':
        menu_receita_crud()
    if resultado['m'] == 'Despesa':
        menu_despesa_crud()
    if resultado['m'] == 'Relatório':
        menu_relatorio()
    if resultado['m'] == 'Sair':
        print('Sistema encerrado!')
        return