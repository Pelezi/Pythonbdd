# **Sistema de RPG com Banco de Dados SQLite**

| **Aluno**                     | **Matrícula**     |
|-------------------------------|-------------------|
| Alessandro Cardoso da Costa   | 202051317043      |
| Maíra Fernando da Silva       | 202402412141      |
| Victor José Cavalcante da Silva | 202403521938    |
| João Augusto de Brito Silva   | 202402412116      |

## **1\. Descrição do Projeto**

Este projeto é um sistema de gerenciamento de personagens de RPG, desenvolvido em **Python** utilizando o **SQLite** como banco de dados. O sistema permite **criar, listar, atualizar, deletar e buscar personagens** com diferentes atributos.

---

## **2\. Estrutura da Tabela (Banco de Dados)**

**Nome do Banco:** `Games.db`  
**Tabela:** `personagens`

| Coluna | Tipo | Descrição |
| ----- | ----- | ----- |
| `id` | INTEGER | Chave primária, autoincrementada |
| `classe_personagem` | TEXT | Classe do personagem (ex: Guerreiro) |
| `armadura_equipamento` | TEXT | Tipo de armadura (ex: Couro, Metal) |
| `arma_equipamento` | TEXT | Arma usada pelo personagem |
| `ouro` | REAL | Quantidade de ouro que o personagem possui |

---

## **3\. Funcionalidades Implementadas**

* **Criação da Tabela**  
  * Opção de deletar e recriar a tabela `personagens`.  
* **Menu Interativo**  
  * Interface em terminal que guia o usuário pelas opções.  
* **CRUD Completo**  
  * **Criar**: Insere um novo personagem com os dados informados.  
  * **Ler**: Lista todos os personagens salvos.  
  * **Atualizar**: Permite editar qualquer campo de um personagem específico.  
  * **Deletar**: Remove um personagem com base no ID.  
  * **Buscar**: Procura por personagens usando parte do nome da classe.

---

## **4\. Prints do Sistema**

* Pressionado i : mostra menu de opções	![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/inicio.png)  
  
* Listagem dos personagens:  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/lista_de_personagens.png)
* Tela de criação de um novo personagem:  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/criacao_novo_personagem.png)
* Tela de atualização de um personagem:  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/atualizacao_de_personagem.png)
* Tela de exclusão de um personagem:  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/exclusao_de_personagem.png)
* Busca de um personagem:  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/busca_de_personagem.png)
* Resetando o banco de dados:  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/exclusa_banco.png)  
* Sair do sistema:  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/sair_do_sistema.png)

---

## **5\. Bibliotecas Utilizadas**

| Biblioteca | Função no Projeto |
| :---- | :---- |
| `sqlite3` | Conectar e manipular o banco de dados SQLite |
