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
    
    tb = Table(show_lines=True, style='green', show_header=False)
    tb.add_row('Nome', 'Insituição', 'Tipo', 'Descrição', 'Receita', style='blue')
    for i in receita:
        tb.add_row(
            i.usuario.nome,
            i.instituicao.nome,
            i.instituicao.tipo,
            i.instituicao.descricao,
            f'{i.valor:.2f}',
        )
        
    tb.add_row('Receita', '', '', 'Total', f'R$ {receita_soma:.2f}')
    tb.add_row('')
    tb.add_row('Nome', 'Insituição', 'Tipo', 'Descrição', 'Despesa', style='red')
    
    for i in despesa:
        tb.add_row(
            i.usuario.nome,
            i.instituicao.nome,
            i.instituicao.tipo,
            i.instituicao.descricao,
            f'{i.valor:.2f}', 
        )
        
    tb.add_row('Despesa', '', '', 'Total', f'R$ {despesa_soma:.2f}')
    tb.add_row('')
    tb.add_row('', '', '', 'Saldo', f'R$ {receita_soma - despesa_soma}')
    
    return print(tb)
    
    
    