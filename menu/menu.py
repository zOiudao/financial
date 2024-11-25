from database.data import Usuario, Instituicao, session, Receita
from InquirerPy import prompt
from os import system


def bd_menu(bd_name, msg):
    names = [i.nome for i in session.query(bd_name).all()]
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


def sim_ou_nao(msg):
    yn = [
        {
            'type': 'list',
            'message': msg,
            'choices': ['Sim', 'Não'],
            'name': 'yn'
        }
    ]
    res = prompt(yn)
    return res['yn']


def receita_menu(msg):
    nome = [i.usuario.nome for i in session.query(Receita).all()]
    print(nome)


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
            'message': 'Selecione a opção abaixo.',
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