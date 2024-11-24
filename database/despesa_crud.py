from .data import Despesa, session, Usuario, Instituicao
from menu.menu import usuario_menu, instituicao_menu
from os import system
from InquirerPy import prompt
from rich.table import Table
from rich import print
ftime = '%d/%m/%Y %H:%M:%S'

class DespesaCRUD:
    def despesa_create(self):
        user_name = usuario_menu('Selecione abaixo o nome de quem gerou a despesa.')
        inst_name = instituicao_menu()
        user = session.query(Usuario).filter_by(nome=user_name).one()
        inst = session.query(Instituicao).filter_by(nome=inst_name).one()
        valor = float(input('Valor da transação: '))
        
        try:
            parcelas = int(input('Quantidade de parcelas: '))
        except ValueError:
            parcelas = 1
            
        if type(valor) != float:
            return print('Erro! Valor inválido')
        try:
            create = Despesa(user.id, inst.id, valor, parcelas)
            session.add(create)
            session.commit()
        except Exception as e:
            return print('Erro! Não foi possível realizar o cadastro \n', e)
        return print('Cadastro realizado com sucesso!')
    
    
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
        return
    
    
    def despesa_update(self):
        pass
    
    
    def despesa_delete(self):
        pass
        
        
def menu_despesa_crud():
    from menu.menu import menu_principal
    despesa = DespesaCRUD()
    system('clear')
    create = [
        {
            'type': 'list',
            'message': 'Opções despesa',
            'choices': ['Cadastrar', 'Exibir', 'Editar', 'Deletar', 'Voltar'],
            'name': 'rec'
        }
    ]
    resp = prompt(create)
    if resp['rec'] == 'Cadastrar':
        despesa.despesa_create()
    if resp['rec'] == 'Exibir':
        despesa.despesa_read()
    if resp['rec'] == 'Editar':
        despesa.despesa_update()
    if resp['rec'] == 'Deletar':
        despesa.despesa_delete()
    if resp['rec'] == 'Voltar':
        menu_principal()