
import sqlite3
import pandas as pd
import gzip

# Abrir o arquivo CSV compactado
with gzip.open('world_ampas_oscar_winner_demographics.csv.gz', 'rt', encoding='utf-8') as f:
    df = pd.read_csv(f)

# Conectar ao banco
conn = sqlite3.connect('oscar.db')
cursor = conn.cursor()

# Limpar valores nulos e evitar duplicatas
df = df.dropna(subset=['movie', 'year_edition', 'category', 'birthplace'])

filmes_inseridos = {}

for _, row in df.iterrows():
    titulo = row['movie']
    pais = row['birthplace'].split(',')[-1].strip()  # Usa o último item como país
    ano = int(row['year_edition'])
    categoria = row['category']

    # Inserir filme se ainda não foi inserido
    if titulo not in filmes_inseridos:
        cursor.execute("INSERT INTO Filmes (titulo, pais_origem) VALUES (?, ?)", (titulo, pais))
        filme_id = cursor.lastrowid
        filmes_inseridos[titulo] = filme_id
    else:
        filme_id = filmes_inseridos[titulo]

    # Inserir premiação
    cursor.execute(
        "INSERT INTO Premiacoes (nome_premiacao, ano, categoria, vencedor, filme_id) VALUES (?, ?, ?, ?, ?)",
        ("Oscar", ano, categoria, True, filme_id)
    )

conn.commit()
conn.close()
print("Dados importados com sucesso!")
