import sqlite3

conexao = sqlite3.connect("Games.db")
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS personagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    classe_personagem TEXT NOT NULL,
    armadura_equipamento TEXT NOT NULL,
    arma_equipamento TEXT NOT NULL,
    ouro REAL NOT NULL
)
''')

cursor.execute("SELECT * FROM personagens")
personagens = cursor.fetchall()  
if not personagens:  # Verifica se a tabela está vazia
    print("Tabela vazia, criando personagens padrão...")

    personagens = [
        ("Guerreiro", "Metal", "Espada&Escudo", 150),
        ("Mago", "Tecido", "Cajado&Pergaminhos", 180),
        ("Arqueiro", "Pele", "Arco&Flechas", 195),
        ("Assassino", "Couro", "Rapieira&Adagas", 165)
    ]

    cursor.executemany('''
    INSERT INTO personagens(classe_personagem, armadura_equipamento, arma_equipamento, ouro) VALUES (?, ?, ?, ?)
    ''', personagens)

    print("Personagens criados com sucesso!")

conexao.commit()
conexao.close()
print("Conexão com o banco de dados encerrada.")

# Loop de inicialização do sistema - aguarda o usuário pressionar 'i' para começar
while True:
    iniciar = input("Pressione 'i' para iniciar o sistema de RPG: ").strip().lower()
    if iniciar == 'i':
        break  # Sai do loop quando o usuário pressiona 'i'
    else:
        print("Entrada inválida. Pressione 'i' para iniciar.")

# Função para validar entradas numéricas positivas
def validate_positive_float(value):
    try:
        value = float(value)
        if value < 0:
            raise ValueError("O valor deve ser positivo.")
        return value
    except ValueError:
        print("Entrada inválida. Por favor, insira um número positivo.")
        return None

# Função principal que exibe o menu e gerencia as opções
def menu():
    while True:
        print("\n===== SISTEMA DE RPG =====")
        print("1 - Listar personagens")
        print("2 - Criar novo personagem")
        print("3 - Atualizar personagem")
        print("4 - Deletar personagem")
        print("5 - Buscar personagem por classe")
        print("s - Sair do sistema")

        # Captura a escolha do usuário, removendo espaços e convertendo para minúsculas
        escolha = input("Escolha uma opção: ").strip().lower()

        # Estrutura condicional para chamar a função correspondente à escolha
        if escolha == "1":
            listar_personagens()
        elif escolha == "2":
            criar_personagem()
        elif escolha == "3":
            atualizar_personagem()
        elif escolha == "4":
            deletar_personagem()
        elif escolha == "5":
            buscar_personagem()
        elif escolha == "s":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Escolha uma opção válida.")

# Função para listar todos os personagens cadastrados
def listar_personagens():
    with sqlite3.connect("Games.db") as conexao:
        cursor = conexao.cursor()

        # Executa a consulta SQL para selecionar todos os registros da tabela
        cursor.execute("SELECT * FROM personagens")
        personagens = cursor.fetchall()  # Recupera todos os resultados da consulta

        if personagens:  # Verifica se há personagens cadastrados
            print("\nLISTA DE PERSONAGENS:")
            print("ID | CLASSE       | ARMADURA       | ARMA               | OURO")

            for id_pers, classe, armadura, arma, ouro in personagens:
                print(f"{id_pers} | {classe} | {armadura} | {arma} | {ouro}")
        else:
            print("\nNenhum personagem cadastrado.")

# Função para criar um novo personagem no banco de dados
def criar_personagem():
    print("\nCRIAR NOVO PERSONAGEM:")

    classe = input("Classe do personagem (ex: Guerreiro, Mago): ")
    armadura = input("Tipo de armadura (ex: Metal, Couro): ")
    arma = input("Arma principal (ex: Espada, Cajado): ")

    while True:
        ouro = input("Quantidade de ouro inicial: ")
        ouro = validate_positive_float(ouro)
        if ouro is not None:
            break

    with sqlite3.connect("Games.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO personagens
            (classe_personagem, armadura_equipamento, arma_equipamento, ouro)
            VALUES (?, ?, ?, ?)
        """, (classe, armadura, arma, ouro))

        conexao.commit()  # Confirma a transação no banco de dados
        print(f"Personagem {classe} criado com sucesso!")

# Função para atualizar os dados de um personagem existente
def atualizar_personagem():
    listar_personagens()

    while True:
        id_pers = input("\nID do personagem que deseja atualizar (ou digite 'sair' para voltar ao menu): ").strip().lower()
        if id_pers == 'sair':
            print("Voltando ao menu principal...")
            return

        with sqlite3.connect("Games.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM personagens WHERE id=?", (id_pers,))
            if cursor.fetchone():
                break
            else:
                print("ID inválido. Por favor, insira um ID existente ou digite 'sair' para voltar ao menu.")

    print("\nDeixe em branco os campos que não deseja alterar:")
    nova_classe = input("Nova classe: ")
    nova_armadura = input("Nova armadura: ")
    nova_arma = input("Nova arma: ")

    while True:
        novo_ouro = input("Novo valor de ouro: ")
        if not novo_ouro:
            break
        novo_ouro = validate_positive_float(novo_ouro)
        if novo_ouro is not None:
            break

    with sqlite3.connect("Games.db") as conexao:
        cursor = conexao.cursor()

        # Atualiza cada campo apenas se foi fornecido um novo valor
        if nova_classe:
            cursor.execute("UPDATE personagens SET classe_personagem=? WHERE id=?", (nova_classe, id_pers))
        if nova_armadura:
            cursor.execute("UPDATE personagens SET armadura_equipamento=? WHERE id=?", (nova_armadura, id_pers))
        if nova_arma:
            cursor.execute("UPDATE personagens SET arma_equipamento=? WHERE id=?", (nova_arma, id_pers))
        if novo_ouro:
            cursor.execute("UPDATE personagens SET ouro=? WHERE id=?", (novo_ouro, id_pers))

        conexao.commit()  # Confirma as alterações
        print("Personagem atualizado com sucesso!")

# Função para remover um personagem do banco de dados
def deletar_personagem():
    listar_personagens()

    while True:
        id_pers = input("\nID do personagem que deseja deletar: ")
        with sqlite3.connect("Games.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM personagens WHERE id=?", (id_pers,))
            if cursor.fetchone():
                break
            else:
                print("ID inválido. Por favor, insira um ID existente.")

    confirmacao = input("Tem certeza que deseja deletar este personagem? (s/n): ").strip().lower()
    if confirmacao == 's':
        with sqlite3.connect("Games.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM personagens WHERE id=?", (id_pers,))
            conexao.commit()
            print("Personagem deletado com sucesso!")
    else:
        print("Operação cancelada.")

# Função para buscar personagens por classe (ou parte do nome da classe)
def buscar_personagem():
    termo_busca = input("Digite a classe ou parte do nome da classe que deseja buscar: ").strip().lower()

    with sqlite3.connect("Games.db") as conexao:
        cursor = conexao.cursor()
        # Busca usando LIKE para correspondência parcial (case-insensitive)
        cursor.execute("""
            SELECT * FROM personagens
            WHERE LOWER(classe_personagem) LIKE ?
        """, ('%' + termo_busca + '%',))

        personagens = cursor.fetchall()

        if personagens:
            print("\nPERSONAGENS ENCONTRADOS:")
            print("ID | CLASSE       | ARMADURA       | ARMA               | OURO")

            for id_pers, classe, armadura, arma, ouro in personagens:
                print(f"{id_pers} | {classe} | {armadura} | {arma} | {ouro}")
        else:
            print("Nenhum personagem encontrado com essa classe.")

# Ponto de entrada do programa - inicia o menu
menu()

# Fechar conexão
conexao.close()
