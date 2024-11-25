from .data import Despesa, session, Usuario, Instituicao
from menu.menu import bd_menu, sim_ou_nao, menu_principal
from os import system
from time import sleep
from InquirerPy import prompt
from rich.table import Table
from rich import print
ftime = '%d/%m/%Y %H:%M:%S'

class DespesaCRUD:
    def despesa_create(self):
        user_name = bd_menu(Usuario, 'Selecione abaixo o nome de quem gerou a despesa.')
        inst_name = bd_menu(Instituicao, 'Selecione abaixo o nome de onde foi gerada a despesa.')
        user = session.query(Usuario).filter_by(nome=user_name).one()
        inst = session.query(Instituicao).filter_by(nome=inst_name).one()
        valor = float(input('Valor da transação: '))
        
        try:
            parcelas = int(input('Quantidade de parcelas: '))
        except ValueError:
            parcelas = 1
            
        if type(valor) != float:
            print('Erro! Valor inválido \n--Voltar ao menu')
        try:
            create = Despesa(user.id, inst.id, valor, parcelas)
            session.add(create)
            session.commit()
        except Exception as e:
            return print('Erro! Não foi possível realizar o cadastro \n', e, '\n--Voltar ao menu')
        
        print('Cadastro realizado com sucesso! \n--Voltar ao menu')
        sleep(2)        
        system('clear')
        return menu_despesa_crud()        
    
    
    def despesa_read(self):
        tb = Table(show_lines=True, style='blue', title='Despesas')
        tb_header = ['id', 'nome', 'instituição', 'tipo', 'descrição', 'valor', 'data']
        for i in range(len(tb_header)):
            tb.add_column(tb_header[i].upper(), style='green', no_wrap=True)
        for i in session.query(Despesa).all():
            tb.add_row(
                str(i.id),
                i.usuario.nome,
                i.instituicao.nome,
                i.instituicao.tipo,
                i.instituicao.descricao,
                str(i.valor),
                i.data.strftime(ftime)
            )
        total = sum(i.valor for i in session.query(Despesa).all())
        print(tb)
        print(f'O valor total das despesas é: R$: {total:.2f}')
        
        yn = sim_ou_nao('Voltar ao menu?')
        if yn == 'Sim':
            system('clear')
            menu_despesa_crud()
        else:
            system('clear')
            print('Sistema encerrado. \n-Volte sempre!')
            return
    
    
    def despesa_delete(self):
        inst_nome = bd_menu(Despesa, 'Selecione a despesa que deseja deletar.')
        _del = session.query(Despesa).filter_by(nome=inst_nome).one()
        
        conf = sim_ou_nao(f'Tem certeza que deseja deletar o cadastro da despesa {_del.nome}?')
        if conf == 'Sim':
            session.delete(_del)
            session.commit()
            session.close()
            print(f'{inst_nome} deletado com sucesso! \n--Voltar ao menu!')
        else:
            session.close()
            print('Operação cancelada! \n--Voltar ao menu!')
        
        sleep(2)        
        system('clear')
        return menu_despesa_crud()    
    
def menu_despesa_crud():
    despesa = DespesaCRUD()
    system('clear')
    create = [
        {
            'type': 'list',
            'message': 'Opções despesa',
            'choices': ['Cadastrar', 'Exibir', 'Deletar', 'Voltar'],
            'name': 'rec'
        }
    ]
    resp = prompt(create)
    if resp['rec'] == 'Cadastrar':
        despesa.despesa_create()
    if resp['rec'] == 'Exibir':
        despesa.despesa_read()
    if resp['rec'] == 'Deletar':
        despesa.despesa_delete()
    if resp['rec'] == 'Voltar':
        menu_principal()