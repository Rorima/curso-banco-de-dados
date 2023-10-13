import socket

import couchdb


def conectar():
    """
    Função para conectar ao servidor
    """
    user = 'admin'
    password = 'admin'

    conn = couchdb.Server(f'http://{user}:{password}@localhost:5984')
    banco = 'pcouch'

    if banco in conn:
        db = conn[banco]
        return db
    else:
        try:
            db = conn.create(banco)
            return db
        except socket.gaierror as e:
            print(f'Erro ao conectar ao servidor: {e}.')
        except couchdb.http.Unauthorized as f:
            print(f'Você não tem permissão de acesso: {f}.')
        except ConnectionRefusedError as g:
            print(f'Não foi possível conectar ao servidor: {g}.')


def desconectar():
    """
    Função para desconectar do servidor.
    """
    # o CouchDB desconecta automaticamente.
    pass


def listar():
    """
    Função para listar os produtos
    """
    db = conectar()

    if db:
        if db.info()["doc_count"] > 0:
            print('Listando produtos:\n')
            for doc in db:
                print(f"ID: {db[doc]['_id']}")
                print(f"Rev: {db[doc]['_rev']}")
                print(f"Nome: {db[doc]['nome']}")
                print(f"Preço: {db[doc]['preco']}")
                print(f"Estoque: {db[doc]['estoque']}")
                print()
        else:
            print('Não existem produtos cadastrados.')
    else:
        print("Não foi possível conectar com o servidor.")


def inserir():
    """
    Função para inserir um produto
    """
    db = conectar()

    if db:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade em estoque: "))

        produto = {'nome': nome, 'preco': preco, 'estoque': estoque}
        res = db.save(produto)

        if res:
            print(f'O produto "{nome}" foi inserido com sucesso!')
        else:
            print("Não foi possível inserir o produto.")
    else:
        print("Não foi possível conectar ao servidor.")


def atualizar():
    """
    Função para atualizar um produto
    """
    db = conectar()

    if db:
        chave = input('Digite o id do produto: ')
        try:
            doc = db[chave]

            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            estoque = int(input("Digite a quantidade em estoque: "))

            doc['nome'] = nome
            doc['preco'] = preco
            doc['estoque'] = estoque
            db[doc.id] = doc

            print(f'O produto "{nome}" foi atualizado com sucesso!')
        except couchdb.http.ResourceNotFound as e:
            print(f'Produto não encontrado: {e}.')
    else:
        print('Não foi possível conectar ao servidor.')


def deletar():
    """
    Função para deletar um produto
    """
    db = conectar()

    if db:
        _id = input('Digite o id do produto: ')

        try:
            db.delete(db[_id])
            print('O produto foi atualizado com sucesso!')
        except couchdb.http.ResourceNotFound as e:
            print(f'Produto não encontrado: {e}.')
    else:
        print('Não foi possível conectar ao servidor.')


def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
