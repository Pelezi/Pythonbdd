# **Sistema de RPG com Banco de Dados SQLite**

**Alunos:** Alessandro Cardoso da Costa,  Maíra Fernando da Silva, Victor José Cavalcante da Silva, João Augusto de Brito Silva 
**Matrícula:** 202051317043, 202402412141, 202403521938, 202402412116

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

* Deletando o banco de dados:  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/exclusa_banco.png)  
* Pressionado i : mostra menu de opções	![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/inicio.png)  
* Listagem dos personagens  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/lista_de_personagens.png)
  


* Tela de criação  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/criacao_novo_personagem.png)
* Tela de atualização  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/atualizacao_de_personagem.png)
* Resultado da busca  
  ![](https://raw.githubusercontent.com/Pelezi/Pythonbdd/8e40adfabf980d580e283c745090c6a6f251c7da/prints/busca_de_personagem.png)

---

## **5\. Bibliotecas Utilizadas**

| Biblioteca | Função no Projeto |
| :---- | :---- |
| `sqlite3` | Conectar e manipular o banco de dados SQLite |
