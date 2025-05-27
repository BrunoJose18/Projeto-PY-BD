import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('oscar.db')
cursor = conn.cursor()

def buscar_filme():
    titulo = entry_titulo.get()

    if not titulo.strip():
        messagebox.showwarning("Atenção", "Digite um título de filme.")
        return

    cursor.execute("SELECT id, pais_origem FROM Filmes WHERE LOWER(titulo) = LOWER(?)", (titulo,))
    filme = cursor.fetchone()

    if not filme:
        messagebox.showerror("Erro", "Filme não encontrado.")
        return

    filme_id, pais = filme

    cursor.execute("SELECT COUNT(*) FROM Premiacoes WHERE filme_id = ? AND vencedor = 1 AND nome_premiacao = 'Oscar'", (filme_id,))
    oscars = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Premiacoes WHERE filme_id = ? AND vencedor = 1", (filme_id,))
    total_premiacoes = cursor.fetchone()[0]

    label_resultado.config(
        text=f"🎬 País de origem: {pais}\n🏆 Oscars ganhos: {oscars}\n🏅 Total de premiações: {total_premiacoes}",
        fg="navy"
    )

janela = tk.Tk()
janela.title("Consulta de Filmes Premiados")
janela.geometry("400x250")
janela.configure(bg="#f0f0f0")

tk.Label(janela, text="Consulta de Premiações do Oscar", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

frame_input = tk.Frame(janela, bg="#f0f0f0")
frame_input.pack()

tk.Label(frame_input, text="Título do Filme:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_titulo = tk.Entry(frame_input, width=30, font=("Arial", 12))
entry_titulo.grid(row=0, column=1, padx=5, pady=5)

tk.Button(janela, text="Buscar", command=buscar_filme, bg="#4CAF50", fg="white", font=("Arial", 11), width=15).pack(pady=5)

label_resultado = tk.Label(janela, text="", font=("Arial", 12), justify="left", bg="#f0f0f0")
label_resultado.pack(pady=10)

janela.mainloop()