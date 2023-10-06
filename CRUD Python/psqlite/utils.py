import sqlite3


def conectar():
    """
    Função para conectar ao servidor
    """
    conn = sqlite3.connect('psqlite3.roni')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        );
    ''')
    return conn


def desconectar(conn):
    """
    Função para desconectar do servidor.
    """
    conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando produtos:\n')
        for produto in produtos:
            print(f'ID: {produto[0]};')
            print(f'Produto: {produto[1]};')
            print(f'Preço: {produto[2]};')
            print(f'Estoque: {produto[3]}.')
            print()
    else:
        print("Não existem produtos cadastrados.")

    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """
    conn = conectar()

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))

    cursor = conn.cursor()
    cursor.execute(
        f'''INSERT INTO produtos (nome, preco, estoque)
        VALUES ('{nome}', {preco}, {estoque})'''
    )

    conn.commit()

    if cursor.rowcount == 1:
        print(f"O produto '{nome}' foi inserido com sucesso!")
    else:
        print("Erro ao inserir produto.")

    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()

    id = int(input("Digite o ID do produto: "))
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))

    cursor = conn.cursor()
    cursor.execute(
        f'''UPDATE produtos
        SET nome='{nome}',
            preco={preco},
            estoque={estoque}
        WHERE id={id}'''
    )

    conn.commit()

    if cursor.rowcount == 1:
        print(f"O produto '{nome}' foi atualizado com sucesso!")
    else:
        print("Erro ao atualizar produto.")

    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()

    id = int(input("Digite o ID do produto: "))

    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM produtos WHERE id={id}')

    conn.commit()

    if cursor.rowcount == 1:
        print("O produto foi deletado com sucesso!")
    else:
        print("Erro ao deletar produto.")

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
