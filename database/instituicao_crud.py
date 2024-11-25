from .data import Instituicao, session
from menu.menu import sim_ou_nao, bd_menu, menu_principal
from os import system
from InquirerPy import prompt
from rich.table import Table
from rich import print
from time import sleep

class InstituicaoCRUD:
    def instituicao_crate(self):
        nome = input('Nome da instituição: ').title().strip()
        tipo = input('Tipo de transação: ').capitalize().strip()
        descricao = input('Descrição da transação: ').capitalize().strip()
        try:
            create = Instituicao(nome, tipo, descricao)
            session.add(create)
            session.commit()
            print(f'{create.nome} -Cadastrada com sucesso! \n--Voltar ao menu')
        except:
            print('Não foi possivel realizar o cadastro! \n--Voltar ao menu')
        finally:
            sleep(2)
            system('clear')
            return menu_instituicao_crud()
        
        
    def instituicao_read(self):
        tb = Table(show_lines=True, style='green')
        tb_header = 'nome', 'tipo', 'descrição', 'data',
        for i in range(len(tb_header)):
            tb.add_column(tb_header[i].capitalize(), style='blue')
        for i in session.query(Instituicao).all():
            tb.add_row(
                i.nome,
                i.tipo,
                i.descricao,
                i.data.strftime('%d/%m/%Y %H:%M:%S')
            )
        print(tb)
        yn = sim_ou_nao('Voltar ao menu?')
        if yn == 'Sim':
            system('clear')
            menu_instituicao_crud()
        else:
            system('clear')
            print('Sistema encerrado. \n-Volte sempre!')
            return
    
    
    def instituicao_update(self):
        inst_nome = bd_menu(Instituicao, 'Selecione a instituição que deseja editar.')
        update = session.query(Instituicao).filter_by(nome=inst_nome).one()
        
        nome = str(input('Digite o nome da instituição atualizado: ')).strip().title()
        if nome:
            update.nome = nome
            
        tipo = str(input('Digite o tipo de transação atualizada: ')).strip().capitalize()
        if tipo:
            update.tipo = tipo
            
        descricao = str(input('Digite a descrição da transação atualizada: ')).strip().capitalize()
        if descricao:
            update.descricao = descricao
            
        session.commit()
        print(f'{update.nome} Atualizado com sucesso! \n--Voltar ao menu principal')
        session.close()
        
        sleep(2)
        system('clear')
        menu_instituicao_crud()
                
    
    def instituicao_delete(self):
        inst_nome = bd_menu(Instituicao, 'Selecione a instituição que deseja deletar.')
        _del = session.query(Instituicao).filter_by(nome=inst_nome).one()
        
        conf = sim_ou_nao(f'Tem certeza que deseja deletar o cadastro de {_del.nome}?')
        if conf == 'Sim':
            session.delete(_del)
            session.commit()
            print(f'{inst_nome} deletado com sucesso! \n--Voltar ao menu')
            session.close()
            sleep(2)
            system('clear')
            return menu_instituicao_crud()
        else:
            session.close()
            print('Operação cancelada! \n--Voltar ao menu')
            sleep(2)
            system('clear')
            return menu_instituicao_crud()
        
        
        
def menu_instituicao_crud():
    instituicao = InstituicaoCRUD()
    menu = [
        {
            'type': 'list',
            'message': 'Opções instituição',
            'choices': ['Cadastrar', 'Exibir', 'Editar', 'Deletar', 'Voltar'],
            'name': 'inst'
        }
    ]
    resp = prompt(menu)
    if resp['inst'] == 'Cadastrar':
        instituicao.instituicao_crate()
    if resp['inst'] == 'Exibir':
        instituicao.instituicao_read()
    if resp['inst'] == 'Editar':
        instituicao.instituicao_update()
    if resp['inst'] == 'Deletar':
        instituicao.instituicao_delete()
    if resp['inst'] == 'Voltar':
        menu_principal()