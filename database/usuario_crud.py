from .data import Usuario, session
from os import system
from InquirerPy import prompt
from rich import print
from rich.table import Table


class UsuarioCRUD:
    def usuario_create(self):
        nome = input('Nome completo: ').title().strip()
        system('clear')
        cpf = input('CPF: ').strip()
        system('clear')
        email = input('E-Mail: ').lower().strip()
        system('clear')
        senha = input('Senha: ').strip()
        
        try:
            create = Usuario(nome, cpf, email, senha)
            session.add(create)
            session.commit()
            system('clear')
            print(f'{create.nome} \n-Cadastrado com sucesso!')
            menu_voltar()
        except:
            return print('Não foi possivel realizar o cadastro!')
        finally:
            return
        
    
    def usuario_read(self):
        tb = Table(show_lines=True, style='green')
        tb_header = 'nome', 'cpf', 'email', 'data',
        for i in range(len(tb_header)):
            tb.add_column(tb_header[i].capitalize(), style='blue')
        for i in session.query(Usuario).all():
            tb.add_row(
                i.nome,
                i.cpf,
                i.email,
                i.data.strftime('%d/%m/%Y %H:%M:%S')
            )
        print(tb)
        return
    
    
    def usuario_update(self):
        from menu.menu import usuario_menu
        self.usuario_read()
        usuario_menu('Selecione abaixo o usuário que deseja editar')
        
        
        
def menu_voltar():
    system('clear')
    usuario = UsuarioCRUD()
    voltar = [
        {
            'type': 'list',
            'message': 'Opções usuário',
            'choices': ['Cadastrar', 'Voltar'],
            'name': 'v',
        }
    ]
    resultado = prompt(voltar)
    if resultado['v'] == 'Cadastrar':
        usuario.usuario_create()
    if resultado['v'] == 'Voltar':
        menu_usuario_crud()
        

def menu_usuario_crud():
    system('clear')
    from menu.menu import menu_principal
    usuario = UsuarioCRUD()
    menu = [
        {
            'type': 'list',
            'message': 'Opções usuário',
            'choices': ['Cadastrar', 'Exibir', 'Editar', 'Deletar', 'Voltar'],
            'name': 'u',
        }
    ]
    resultado = prompt(menu)
    if resultado['u'] == 'Cadastrar':
        usuario.usuario_create()
    if resultado['u'] == 'Exibir':
        usuario.usuario_read()
    if resultado['u'] == 'Editar':
        usuario.usuario_update()
    if resultado['u'] == 'Deletar':
        usuario.usuario_delete()
    if resultado['u'] == 'Voltar':
        menu_principal()