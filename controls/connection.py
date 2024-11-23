#importar o conector do MySQL
import mysql.connector
from mysql.connector import Error


class GerenciadorConexao:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        # Conecta ao banco de dados ao entrar no bloco with
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conexao.cursor()
        return self.cursor  # Retorna o cursor para ser usado no bloco with

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Fecha o cursor e a conexão ao sair do bloco with
        if self.cursor: 
            self.cursor.close()
        if self.conexao.is_connected():
            self.conexao.close()

