from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Actividades
import json

app = Flask(__name__)
api = Api(app)


class Pessoa_manipulacao(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Pessoa nao encontrada'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = json.loads(request.data)
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade'in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
                'id': pessoa.id,
                'nome':pessoa.nome,
                'idade':pessoa.idade
            }

        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'O utilizador {} foi excluido com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status':'success', 'mensagem':mensagem}

class Pessoas_lista(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [ {'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        print(response)
        return response

    def post(self):
        dados = json.loads(request.data)
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response={
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }

        return response


class actividades_lista(Resource):
    def get(self):
        atividades = Actividades.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome} for i in atividades]
        return response


    
    def post(self):
        dados = json.loads(request.data)
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        actividade = Actividades(nome=dados['nome'], pessoa = pessoa)
        actividade.save()
        response = {
            'pessoa':actividade.pessoa.nome,
            'nome':actividade.nome,
            'id':actividade.id
            }

        return response



api.add_resource(Pessoa_manipulacao, '/pessoa/<string:nome>/')
api.add_resource(Pessoas_lista, '/pessoa/')
api.add_resource(actividades_lista, '/actividades/')

if __name__ == '__main__':
    app.run(debug=True)