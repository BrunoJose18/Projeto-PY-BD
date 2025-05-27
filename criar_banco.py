
import sqlite3

conn = sqlite3.connect('oscar.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    pais_origem TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Premiacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_premiacao TEXT,
    ano INTEGER,
    categoria TEXT,
    vencedor BOOLEAN,
    filme_id INTEGER,
    FOREIGN KEY (filme_id) REFERENCES Filmes(id)
)
''')

conn.commit()
conn.close()
print("Banco de dados criado com sucesso!")
