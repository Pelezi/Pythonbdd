import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('meubanco.db')
cursor = conexao.cursor()

# Criar a tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')
conexao.commit()

# Adicionar um usuário
def adicionar_usuario(nome, email):
    try:
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conexao.commit()
        print("Usuário adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Email já cadastrado!")

# Listar todos os usuários
def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

# Atualizar um usuário
def atualizar_usuario(id_usuario, novo_nome, novo_email):
    cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, id_usuario))
    conexao.commit()
    print("Usuário atualizado com sucesso!")

# Deletar um usuário
def deletar_usuario(id_usuario):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conexao.commit()
    print("Usuário removido com sucesso!")

# Testando as funções
if __name__ == "__main__":
    adicionar_usuario("Alice", "alice@email.com")
    adicionar_usuario("Bob", "bob@email.com")
    listar_usuarios()
    atualizar_usuario(1, "Alice Silva", "alice.silva@email.com")
    listar_usuarios()
    deletar_usuario(2)
    listar_usuarios()

# Fechar conexão
conexao.close()
