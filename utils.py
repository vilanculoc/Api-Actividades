from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Beatriz', idade = '16')
    print(pessoa)
    pessoa.save()

def consulta_pessoas(nome):
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
    pessoa =Pessoas.query.filter_by(nome='Isaura').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #consulta_pessoas('Beatriz')
    #altera_pessoa()
    consulta_pessoas()
    #exclui_pessoa()
   # consulta_pessoas('Beatriz')