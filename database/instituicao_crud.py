from .data import Instituicao, session
from os import system
from InquirerPy import prompt

class InstituicaoCRUD:
    def instituicao_crate(self):
        nome = input('Nome da instituição: ').title().strip()
        system('clear')
        tipo = input('Tipo de transação: ').capitalize().strip()
        system('clear')
        descricao = input('Descrição da transação: ').capitalize().strip()
        system('clear')
        try:
            create = Instituicao(nome, tipo, descricao)
            session.add(create)
            session.commit()
            return print(f'{create.nome} \n-Cadastrada com sucesso!')
        except:
            return print('Não foi possivel realizar o cadastro!')
        
        
def menu_instituicao_crud():
    from menu.menu import menu_principal
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