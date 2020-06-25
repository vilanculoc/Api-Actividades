from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='celsa', idade = '23')
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
   # pessoa = Pessoas.query.filter_by(nome=nome).first()
    #print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='celsa').first()
    print(pessoa)
    pessoa.nome = 'Isaura'
    pessoa.save()
    print(pessoa)

def exclui_pessoa():
    pessoa =Pessoas.query.filter_by(nome='celsa').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()
    consultar = Usuarios.query.all()
    print(consultar)



if __name__ == '__main__':
    #insere_pessoas()
    #consulta_pessoas('Beatriz')
    #altera_pessoa()
    #consulta_pessoas()
    #exclui_pessoa()
   # consulta_pessoas('Beatriz')
    insere_usuario('root','12345')
    insere_usuario('admin','admin')