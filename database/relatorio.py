from InquirerPy import prompt
from os import system
from .data import *
from menu.menu import menu_principal, sim_ou_nao
from rich import print
from rich.table import Table


def relatorio():
    receita = session.query(Receita).all()
    despesa = session.query(Despesa).all()
    
    receita_soma = sum(i.valor for i in session.query(Receita).all())
    despesa_soma = sum(i.valor for i in session.query(Despesa).all())
    
    tb = Table(show_lines=True, style='#696969', show_header=False)
    tb.add_column(no_wrap=True)
    tb.add_row('Nome', 'Insituição', 'Tipo', 'Descrição', 'Receita', style='#90EE90')
    for i in receita:
        tb.add_row(
            i.usuario.nome,
            i.instituicao.nome,
            i.instituicao.tipo,
            i.instituicao.descricao,
            f'R$ {i.valor:.2f}',
            style='#ADD8E6'
        )
        
    tb.add_row('Receita', '--', '--', 'Total', f'R$ {receita_soma:.2f}', style='#90EE90 bold')
    tb.add_row('Nome', 'Insituição', 'Tipo', 'Descrição', 'Despesa', style='#DAA520')
    
    for i in despesa:
        tb.add_row(
            i.usuario.nome,
            i.instituicao.nome,
            i.instituicao.tipo,
            i.instituicao.descricao,
            f'{i.valor:.2f}',
            style='#ADD8E6',
            end_section = True
        )
        
    saldo = receita_soma - despesa_soma
    tb.add_row('Despesa', '--', '--', 'Total', f'R$ {despesa_soma:.2f}', style='#DAA520 bold')
    tb.add_row('Saldo', '--', '--', 'Total', f'R$ {saldo:.2f}', style='green bold')
    
    print(tb)
    yn = sim_ou_nao('Retornar ao menu principal?')
    if yn == 'Sim':
        menu_principal()
    else:
        print('Sistema encerrado. \n--Volte sempre')
        return
    
    
def menu_relatorio():
    menu = [
        {
            'type': 'list',
            'message': 'Opções instituição',
            'choices': ['Exibir relatório', 'Voltar'],
            'name': 'inst'
        }
    ]
    resp = prompt(menu)
    if resp['inst'] == 'Exibir relatório':
        relatorio()
    if resp['inst'] == 'Voltar':
        menu_principal()