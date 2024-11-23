from database.usuario_crud import UsuarioCRUD
from database.instituicao_crud import InstituicaoCRUD
from database.receita_crud import ReceitaCRUD

user = UsuarioCRUD()
inst = InstituicaoCRUD()
rece = ReceitaCRUD()

if __name__ == '__main__':
    #user.usuario_create()
    #inst.instituicao_crate()
    rece.receita_create()
    pass