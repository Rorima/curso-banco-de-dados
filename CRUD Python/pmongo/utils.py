from bson import errors as berrors
from bson.objectid import ObjectId
from pymongo import MongoClient, errors


def conectar():
    """
    Função para conectar ao servidor
    """
    conn = MongoClient('localhost', 27017)

    return conn


def desconectar(conn):
    """
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    db = conn.pmongo

    try:
        if db.produtos.count_documents({}) > 0:
            produtos = db.produtos.find()
            print('Listando produtos:\n')
            for produto in produtos:
                print(f"ID: {produto['_id']}")
                print(f"Produto: {produto['nome']}")
                print(f"Preço: {produto['preco']}")
                print(f"Estoque: {produto['estoque']}")
                print()
        else:
            print('Não existem produtos cadastrados.')
    except errors.PyMongoError as e:
        print(f'Erro ao acessar o banco de dados: {e}')

    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """
    conn = conectar()
    db = conn.pmongo

    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    estoque = int(input('Digite a quantidade em estoque: '))

    try:
        db.produtos.insert_one(
            {
                "nome": nome,
                "preco": preco,
                "estoque": estoque
            }
        )

        print(f'O produto "{nome}" foi inserido com sucesso!')
    except errors.PyMongoError as e:
        print(f'Não foi possível inserir o produto. Erro: {e}')

    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    db = conn.pmongo

    _id = input('Digite o id do produto: ')
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    estoque = int(input('Digite a quantidade em estoque: '))

    try:
        if db.produtos.count_documents({}) > 0:
            res = db.produtos.update_one(
                {"_id": ObjectId(_id)},
                {
                    "$set": {
                        "nome": nome,
                        "preco": preco,
                        "estoque": estoque
                    }
                }
            )

            if res.modified_count == 1:
                print(f'O produto "{nome}" foi atualizado com sucesso!')
            else:
                print('Não foi possível atualizar o produto.')
        else:
            print('Não existem documentos para serem atualizados.')
    except errors.PyMongoError as e:
        print(f"Erro ao atulizar o banco de dados: {e}.")
    except berrors.InvalidId as f:
        print(f"Object ID inválido: {f}.")

    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    db = conn.pmongo

    _id = input('Digite o ID do produto: ')

    try:
        if db.produtos.count_documents({}) > 0:
            res = db.produtos.delete_one(
                {"_id": ObjectId(_id)}
            )

            if res.deleted_count > 0:
                print('Produto deletado com sucesso!')
            else:
                print("Não foi possível deletr o produto.")
        else:
            print("Não existem produtos para serem deletados.")
    except errors.PyMongoError as e:
        print(f"Erro ao acessar o banco de dados: {e}.")
    except berrors.InvalidId as f:
        print(f"Object ID inválido: {f}.")

    desconectar(conn)


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
