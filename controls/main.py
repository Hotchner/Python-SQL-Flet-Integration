from connection import GerenciadorConexao
from connection import Error

def list_tables():
    with GerenciadorConexao("localhost", "root", "Ed22330593*", "me") as cursor:
        try:
            comando = "SELECT nome FROM funcionario;"
            cursor.execute(comando)
            for tabelas in cursor:
                print(tabelas)
        except Error as e:
            print(f"Ocorreu um erro: {e}")

list_tables()

#list_tables()

