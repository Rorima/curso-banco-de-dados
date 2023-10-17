import pyrebase


def conectar():
    """
    Função para conectar ao servidor
    """
    config = {
        "apiKey": "zzz",
        "authDomain": "zzz",
        "databaseURL": "zzz",
        "storageBucket": "zzz"
    }

    conn = pyrebase.initialize_app(config)
    db = conn.database()
    return db


def desconectar():
    """
    Função para desconectar do servidor.
    """
    # O Firebase fecha a conexão automaticamente.
    pass


def listar():
    """
    Função para listar os produtos
    """
    db = conectar()

    produtos = db.child("produtos").get()

    if produtos.val():
        print('Listando produtos:\n')
        for produto in produtos:
            print(f'ID: {produto.key()}')
            print(f'Produto: {produto.val()["nome"]}')
            print(f'Estoque: {produto.val()["estoque"]}')
            print(f'Preço: {produto.val()["preco"]}')
            print()
    else:
        print("Não existem produtos cadastrados.")


def inserir():
    """
    Função para inserir um produto
    """
    db = conectar()

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))

    produto = {"nome": nome, "preco": preco, "estoque": estoque}

    res = db.child("produtos").push(produto)

    if 'name' in res:
        print(f"O produto '{nome}' foi cadastrado com sucesso!")
    else:
        print("Não foi possível cadastrar o produto.")


def atualizar():
    """
    Função para atualizar um produto
    """
    db = conectar()

    _id = input("Digite o ID do produto: ")
    produto = db.child("produtos").child(_id).get()

    if produto.val():
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade em estoque: "))

        novo_produto = {"nome": nome, "preco": preco, "estoque": estoque}

        db.child("produtos").child(_id).update(novo_produto)

        print(f"O produto '{nome}' foi atualizado com sucesso!")
    else:
        print("Não existe um produto com o ID informado.")


def deletar():
    """
    Função para deletar um produto
    """
    db = conectar()

    _id = input("Digite o id do produto: ")

    produto = db.child("produtos").child(_id).get()

    if produto.val():
        db.child("produtos").child(_id).remove()

        print("O produto foi deletado com sucesso!")
    else:
        print("Não existe um produto com o ID informado.")


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
