from .data import Receita, Usuario, Instituicao, session
from menu.menu import usuario_menu, instituicao_menu
from os import system
from InquirerPy import prompt
from rich import print
from rich.table import Table
ftime = '%d/%m/%Y %H:%M:%S'


class ReceitaCRUD:
    def receita_create(self):
        user_name = usuario_menu('Selecione abaixo o nome de quem recebeu a receita.')
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
    
    
    def receita_read(self):
        tb = Table(show_lines=True, style='blue', title='Receitas')
        tb_header = ['nome', 'instituicao', 'tipo', 'descrição', 'valor', 'data']
        total = sum(i.valor for i in session.query(Receita).all())
        for i in range(len(tb_header)):
            tb.add_column(tb_header[i].upper(), style='green', no_wrap=True)
        for i in session.query(Receita).all():
            tb.add_row(
                i.usuario.nome,
                i.instituicao.nome,
                i.instituicao.tipo,
                i.instituicao.descricao,
                str(i.valor),
                i.data.strftime(ftime),
            )
        tb.grid(expand=True) 
        tb.add_row(str(total))       
        print(tb)
        print(f'O valor total da receita é R$: {total:.2f}')
        return
    
    
    def receita_update(self):
        pass
    
    
    def receita_delete(self):
        pass
    
    
def menu_receita_crud():
    from menu.menu import menu_principal
    receita = ReceitaCRUD()
    system('clear')
    create = [
        {
            'type': 'list',
            'message': 'Opções receita',
            'choices': ['Cadastrar', 'Exibir', 'Editar', 'Deletar', 'Voltar'],
            'name': 'rec'
        }
    ]
    resp = prompt(create)
    if resp['rec'] == 'Cadastrar':
        receita.receita_create()
    if resp['rec'] == 'Exibir':
        receita.receita_read()
    if resp['rec'] == 'Editar':
        receita.receita_update()
    if resp['rec'] == 'Deletar':
        receita.receita_delete()
    if resp['rec'] == 'Voltar':
        menu_principal()