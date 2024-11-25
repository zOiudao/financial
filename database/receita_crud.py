from .data import Receita, Usuario, Instituicao, session
from menu.menu import bd_menu, sim_ou_nao, menu_principal
from datetime import datetime
import pytz
from os import system
from InquirerPy import prompt
from rich import print
from rich.table import Table
from time import sleep
tmz = pytz.timezone('America/Sao_Paulo')
ftime = '%d/%m/%Y %H:%M:%S'
dt_atual = datetime.now(tmz)

class ReceitaCRUD:
    def receita_create(self):
        user_name = bd_menu(Usuario, 'Selecione abaixo o nome de quem recebeu a receita.')
        inst_name = bd_menu(Instituicao, 'Selecione abaixo o nome de onde veio a receita.')
        user = session.query(Usuario).filter_by(nome=user_name).one()
        inst = session.query(Instituicao).filter_by(nome=inst_name).one()
        valor = float(input('Valor da transação: '))
        if type(valor) != float:
            print('Erro! Valor inválido \n--Retornnando ao menu!')
        try:
            create = Receita(user.id, inst.id, valor)
            session.add(create)
            session.commit()
            print('Receita registrada com sucesso!')
        except Exception as e:
            print('Erro, não foi possível realizar o cadadastro! \n', e, '\n--Voltar ao menu principal!')
        
        print('Transação cadastrada com sucesso! \n--Voltar ao menu principal!')
        sleep(2)
        system('clear')
        menu_receita_crud()
        
    
    
    def receita_read(self):
        tb = Table(show_lines=True, style='blue', title='Receitas')
        tb_header = ['id', 'nome', 'instituicao', 'tipo', 'descrição', 'valor', 'data']
        total = sum(i.valor for i in session.query(Receita).all())
        for i in range(len(tb_header)):
            tb.add_column(tb_header[i].upper(), style='green', no_wrap=True)
        for i in session.query(Receita).all():
            tb.add_row(
                str(i.id),
                i.usuario.nome,
                i.instituicao.nome,
                i.instituicao.tipo,
                i.instituicao.descricao,
                str(i.valor),
                i.data.strftime(ftime),
            )
        tb.add_row('-', 'Receita total', '-', '-', '-', str(total), dt_atual.strftime(ftime), style='green bold')       
        print(tb)
        print(f'O valor total da receita é R$: {total:.2f}')
    
    
    def receita_delete(self):
        self.receita_read()
        rec_id = int(input('Digite o ID da receita que deseja deletar: '))
        _del = session.query(Receita).filter_by(id=rec_id).one()
        
        conf = sim_ou_nao(f'Tem certeza que deseja deletar a receita?')
        if conf == 'Sim':
            session.delete(_del)
            session.commit()
            session.close()
            print(f'Deletado com sucesso! \n--Voltar ao menu!')
        else:
            session.close()
            print('Operação cancelada! \n--Voltar ao menu!')
    
        sleep(2)
        system('clear')
        menu_receita_crud()
    
def menu_receita_crud():
    receita = ReceitaCRUD()
    system('clear')
    create = [
        {
            'type': 'list',
            'message': 'Opções receita',
            'choices': ['Cadastrar', 'Deletar', 'Voltar'],
            'name': 'rec'
        }
    ]
    resp = prompt(create)
    if resp['rec'] == 'Cadastrar':
        receita.receita_create()
    if resp['rec'] == 'Deletar':
        receita.receita_delete()
    if resp['rec'] == 'Voltar':
        menu_principal()