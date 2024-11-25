from .data import Usuario, session
from menu.menu import bd_menu, sim_ou_nao, menu_principal
from os import system
from InquirerPy import prompt
from rich import print
from rich.table import Table
from time import sleep


class UsuarioCRUD:
    def usuario_create(self):
        nome = input('Nome completo: ').title().strip()
        cpf = input('CPF: ').strip()
        email = input('E-Mail: ').lower().strip()
        senha = input('Senha: ').strip()
        
        try:
            create = Usuario(nome, cpf, email, senha)
            session.add(create)
            session.commit()
            print(f'{create.nome} Cadastrado com sucesso! \n--Voltar ao menu')
        except:
            print('Não foi possivel realizar o cadastro! \n--Voltar ao menu')
        
        sleep(2)
        system('clear')
        return menu_usuario_crud()
        
    
    def usuario_read(self):
        tb = Table(show_lines=True, style='green')
        tb_header = 'nome', 'cpf', 'email', 'data',
        for i in range(len(tb_header)):
            tb.add_column(tb_header[i].capitalize(), style='blue', no_wrap=True)
        for i in session.query(Usuario).all():
            tb.add_row(
                i.nome,
                i.cpf,
                i.email,
                i.data.strftime('%d/%m/%Y %H:%M:%S')
            )
        print(tb)
        yn = sim_ou_nao('Voltar ao menu?')
        if yn == 'Sim':
            system('clear')
            menu_usuario_crud()
        else:
            system('clear')
            print('Sistema encerrado. \n-Volte sempre!')
            return
    
    
    def usuario_update(self):
                
        nome = bd_menu(Usuario, 'Selecione abaixo o usuário que deseja editar')
        update = session.query(Usuario).filter_by(nome=nome).one()
        
        up_nome = str(input('Digite o nome atualizado: ')).strip().title()
        if up_nome:
            update.nome = up_nome
            
        up_cpf = str(input('Digite o cpf atualizado: ')).strip().replace('.', '').replace('-', '')
        if up_cpf:
            update.cpf = up_cpf
            
        up_email = str(input('Digite o email atualizado: ')).strip().lower()
        if up_email:
            update.email = up_email
            
        up_senha = str(input('Digite a senha atualizada: ')).strip()
        if up_senha:
            update.senha = up_senha
        
        session.commit()
        system('clear')
        
        print(f'{update.nome} Atualizado com sucesso! \n--Voltar ao menu')
        sleep(2)
        system('clear')
        
        return menu_usuario_crud()
        
        
    def usuario_delete(self):
        nome = bd_menu(Usuario, 'Selecione abaixo o usuário que deseja deletar')
        _del = session.query(Usuario).filter_by(nome=nome).one()
        
        conf = sim_ou_nao(f'Tem certeza que deseja deletar o cadastro de {_del.nome}?')
        if conf == 'Sim':
            session.delete(_del)
            session.commit()
            print(f'{nome} deletado com sucesso! \n--Voltar ao menu')
        else:
            session.close()
            print('Operação cancelada! \n--Voltar ao menu')
        
        sleep(2)
        system('clear')    
        return menu_usuario_crud()
    
        
def menu_usuario_crud():
    system('clear')
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