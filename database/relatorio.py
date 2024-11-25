from InquirerPy import prompt
from os import system
from .data import *
from rich import print
from rich.table import Table

def relatorio_receita():
    soma = []
    exibir = session.query(Receita).all()
    tb = Table(show_lines=True, style='green')
    tb_header = ['nome', 'insituição', 'tipo', 'descrição', 'receita']
    for _, v in enumerate(tb_header):
        tb.add_column(v.upper(), style='blue')
    for i in exibir:
        soma.append(i.valor)
        tb.add_row(
            i.usuario.nome,
            i.instituicao.nome,
            i.instituicao.tipo,
            i.instituicao.descricao,
            str(i.valor)
        )
    total = sum(soma)
    tb.grid(expand=True)
    tb.add_row('', '', '', 'Total: ', f'R$: {total}')
    return print(tb)

def relatorio_despesa():
    soma = []
    exibir = session.query(Despesa).all()
    tb = Table(show_lines=True, style='green')
    tb_header = ['nome', 'insituição', 'tipo', 'descrição', 'despesa']
    for _, v in enumerate(tb_header):
        tb.add_column(v.upper(), style='blue')
    for i in exibir:
        soma.append(i.valor)
        tb.add_row(
            i.usuario.nome,
            i.instituicao.nome,
            i.instituicao.tipo,
            i.instituicao.descricao,
            f'{i.valor:.2f}'
        )
    total = sum(soma)
    tb.grid(expand=True)
    tb.add_row('', '', '', 'Total: ', f'R$: {total}')
    return print(tb)

def relatorio():
    receita = session.query(Receita).all()
    despesa = session.query(Despesa).all()
    
    receita_soma = sum(i.valor for i in session.query(Receita).all())
    despesa_soma = sum(i.valor for i in session.query(Despesa).all())
    
    tb = Table(show_lines=True, style='#696969', show_header=False)
    tb.add_row('Nome', 'Insituição', 'Tipo', 'Descrição', 'Receita', style='#90EE90')
    for i in receita:
        tb.add_row(
            i.usuario.nome,
            i.instituicao.nome,
            i.instituicao.tipo,
            i.instituicao.descricao,
            f'{i.valor:.2f}',
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
            style='#ADD8E6'
        )
        
    tb.add_row('Despesa', '--', '--', 'Total', f'R$ {despesa_soma:.2f}', style='#DAA520 bold')
    tb.add_row('Saldo', '--', '--', 'Total', f'R$ {receita_soma - despesa_soma}', style='green bold')
    
    return print(tb)
    
    
def menu_relatorio():
    from menu.menu import menu_principal
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