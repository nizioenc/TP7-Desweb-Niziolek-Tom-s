from flask import Flask
import sqlite3
from threading import Lock

class Database:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._connect()
            return cls._instance

    def _connect(self):
        """Inicializa la conexión a la base de datos"""
        self.connection = sqlite3.connect('app.db')
        self.cursor = self.connection.cursor()
        print("Conexión a la base de datos establecida.")

    def query(self, sql, params=()):
        """Ejecuta una consulta en la base de datos"""
        self.cursor.execute(sql, params)
        self.connection.commit()

    def fetchall(self):
        """Obtiene todos los resultados de la última consulta"""
        return self.cursor.fetchall()

    def close(self):
        """Cierra la conexión a la base de datos"""
        if self.connection:
            self.connection.close()
            print("Conexión a la base de datos cerrada.")
