# Conexao.py
import sqlite3 as db

class Conexao:
    
    def __init__(self):
        self.__conn = db.connect("Locadora/locadora.db")
        
    def conect(self):
        return self.__conn
    
    def fechar(self):
        if self.__conn:
            self.__conn.close()
