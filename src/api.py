from http.client import NOT_FOUND
from werkzeug.exceptions import BadRequest
from flask import Flask, jsonify, request
app = Flask(__name__)


database = {}
database['PEDIDOS'] = [{"id": 0, "imagem": "http://assets.stickpng.com/images/580b585b2edbce24c47b27bb.png", "titulo": "Relogio BIC", "quantidade": 28, "descricao": "Preto, feito em 2008"}, {
    "id": 1, "imagem": "http://assets.stickpng.com/images/580b585b2edbce24c47b27bb.png", "titulo": "Relogio DOC", "quantidade": 22, "descricao": "Vermelho, feito em 2008"}]
database['ESTOQUE'] = [{"id": 0, "imagem": "http://assets.stickpng.com/images/580b585b2edbce24c47b27bb.png", "titulo": "Relogio BIC", "quantidade": 28, "descricao": "Preto, feito em 2008"}, {
    "id": 1, "imagem": "https://i.ibb.co/S6pvHwg/relogio-icon-1.png", "titulo": "Relogio DOC", "quantidade": 22, "descricao": "Vermelho, feito em 2008"}]


def item_ok(dic):
    return type(dic) == dict \
        and "id" in dic \
        and "imagem" in dic \
        and "titulo" in dic \
        and "quantidade" in dic \
        and "descricao" in dic \
        and type(dic["id"]) == int \
        and type(dic["imagem"]) == str \
        and type(dic["titulo"]) == str \
        and type(dic["quantidade"]) == int \
        and type(dic["descricao"]) == str \



@app.route('/')
def all():
    return jsonify(database)


@app.route('/pedidos')
def pedidos():
    return jsonify(database['PEDIDOS'])


@app.route('/estoque')
def estoque():
    return jsonify(database['ESTOQUE'])


@app.route('/estoque/adicionarItemEstoque', methods=['POST'])
def adiciona_item_estoque():
    novo_item_estoque = request.json
    ids = [e["id"] for e in database["ESTOQUE"]]
    if ids:
        nid = max(ids) + 1
    else:
        nid = 1
    novo_item_estoque["id"] = nid
    if not item_ok(novo_item_estoque):
        raise BadRequest
    database["ESTOQUE"].append(novo_item_estoque)
    return jsonify(database["ESTOQUE"])


@app.route('/estoque/<int:id_estoque>', methods=['PUT'])
def alterar_item_estoque(id_estoque):
    novo_item_estoque = request.json
    if not item_ok(database["ESTOQUE"]):
        raise BadRequest
    if id_estoque not in database["ESTOQUE"]:
        raise NOT_FOUND
    database["ESTOQUE"][id_estoque] = novo_item_estoque
    return database["ESTOQUE"]


@app.route('/estoque/<int:id_estoque>', methods=['GET'])
def localiza_item_estoque(id_estoque):
    for item in database["ESTOQUE"]:
        if item['id'] == id_estoque:
            return jsonify(item)
    return 'Não encontrado', 404


@app.route('/estoque/<int:id_estoque>', methods=['DELETE'])
def deleta_item_estoque(id_estoque):
    database["ESTOQUE"].pop(id_estoque)
    return jsonify(database['ESTOQUE'])


@app.route('/reseta', methods=['POST'])
def reseta():
    database = {}
    database['PEDIDOS'] = [{"id": 0, "imagem": "www.google.com", "titulo": "Relogio BIC", "quantidade": 28, "descricao": "Preto, feito em 2008"}, {
        "id": 1, "imagem": "www.globo.com", "titulo": "Relogio DOC", "quantidade": 22, "descricao": "Vermelho, feito em 2008"}]
    database['ESTOQUE'] = [{"id": 0, "imagem": "www.google.com", "titulo": "Relogio BIC", "quantidade": 28, "descricao": "Preto, feito em 2008"}, {
        "id": 1, "imagem": "www.globo.com", "titulo": "Relogio DOC", "quantidade": 22, "descricao": "Vermelho, feito em 2008"}]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)