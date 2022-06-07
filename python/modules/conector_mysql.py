import mysql.connector

class Interface_db_mysql():

    usuario, senha, host, banco = "", "", "", ""

    def __init__(self, usuario, senha, host, banco):
        """Construtot da classe de interface python x mysql
        
            Args:
                usuario (string): usuario do banco de dados,
                senha (string): senha de acesso ao banco de dados,
                host (string): ip de acesso ao banco de dados,
                banco (string): nome do banco de dados.
        """
        try:
            self.usuario = usuario
            self.senha = senha
            self.host = host
            self.banco = banco
        except Exception as e:
            print(str(e))
    
    def conectar(self):
        """Função genérica para conectar ao banco de dados

        Retorna:
            con: conector mysql
            cursor: cursos para leitura do banco de dados
        """

        try:
            con = mysql.connector.connect(user = self.usuario, password = self.senha, 
                                            host = self.host, database = self.banco)
            
            cursor = con.cursor()
            return con, cursor
        except Exception as e:
            print(str(e))

    def desconectar(self, con, cursor):
        """Função genérica para desconectar do banco

        Argumentos:
            con: conector mysql
            cursor: cursor para leitura do banco de dados
        """
    
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print(str(e))

    def buscar(self, query):
        """Função genérica para consulta ao banco de dados

        Argumentos:
            query (string): query de busca
        Retorna:
            cursor fetchall() retorna tudo que for encontrado pelo cursor
        """
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            return cursor.fetchall() 
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor) 

    def inserir(self, query):
        """Função genérica para inserir dados no banco de dados
        
        Argumentos:
            query (string): Query de inserção
        """   
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
        
    def atualizar(self, query):
        """Função genérica para alterar dados no banco de dados
        
        Argumentos:
            query (string): query de atualização
        Retorna: 
            cursor.fetchall(): retorna tudo que for encontrado pelo cursor
        """
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
        
    def deletar(self, query):
        """Função genérica para deletar algum dado do banco de dados
        
        Argumentos:
            query (string): query para deletar
        """
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
