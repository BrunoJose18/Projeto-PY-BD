import sqlite3
import customtkinter as ctk
from tkinter import messagebox

# Janela principal
janela = ctk.CTk()
janela.title("Consulta de Filmes Premiados")
janela.geometry("800x500")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# === Funções ===
def buscar_filme():
    titulo = entry_titulo.get()

    if not titulo.strip():
        messagebox.showwarning("Atenção", "Digite um título de filme.")
        return

    conn = sqlite3.connect("oscar.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, pais_origem FROM Filmes WHERE LOWER(titulo) = LOWER(?)", (titulo,))
    filme = cursor.fetchone()

    if not filme:
        messagebox.showerror("Erro", "Filme não encontrado.")
        conn.close()
        return

    filme_id, pais = filme

    cursor.execute("SELECT COUNT(*) FROM Premiacoes WHERE filme_id = ? AND vencedor = 1 AND nome_premiacao = 'Oscar'", (filme_id,))
    oscars = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Premiacoes WHERE filme_id = ? AND vencedor = 1", (filme_id,))
    total_premiacoes = cursor.fetchone()[0]

    label_resultado.configure(
        text=f"\n🎬 País de origem: {pais}\n🏆 Oscars ganhos: {oscars}\n🏅 Total de premiações: {total_premiacoes}"
    )

    conn.close()

def abrir_consulta_avancada():
    janela_avancada = ctk.CTkToplevel(janela)
    janela_avancada.title("Consulta Avançada")
    janela_avancada.geometry("700x500")

    ctk.CTkLabel(janela_avancada, text="Consulta Avançada de Filmes", font=("Roboto", 20, "bold")).pack(pady=10)

    frame_filtros = ctk.CTkFrame(janela_avancada)
    frame_filtros.pack(pady=10)

    # Filtros
    ctk.CTkLabel(frame_filtros, text="Categoria:").grid(row=0, column=0, padx=5, pady=5)
    entry_categoria = ctk.CTkEntry(frame_filtros, placeholder_text="Ex: Melhor Filme", width=180)
    entry_categoria.grid(row=0, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame_filtros, text="Ano:").grid(row=1, column=0, padx=5, pady=5)
    entry_ano = ctk.CTkEntry(frame_filtros, placeholder_text="Ex: 2020", width=180)
    entry_ano.grid(row=1, column=1, padx=5, pady=5)

    resultado_label = ctk.CTkLabel(janela_avancada, text="", font=("Roboto", 14))
    resultado_label.pack(pady=10)

    def executar_filtros():
        categoria = entry_categoria.get().strip().lower()
        ano = entry_ano.get().strip()

        query = """
            SELECT Filmes.titulo, Filmes.pais_origem, Premiacoes.ano, Premiacoes.categoria
            FROM Filmes
            JOIN Premiacoes ON Filmes.id = Premiacoes.filme_id
            WHERE 1=1
        """
        params = []

        if categoria:
            query += " AND LOWER(Premiacoes.categoria) LIKE ?"
            params.append(f"%{categoria}%")
        if ano:
            query += " AND Premiacoes.ano = ?"
            params.append(ano)

        conn = sqlite3.connect("oscar.db")
        cursor = conn.cursor()
        cursor.execute(query, tuple(params))
        resultados = cursor.fetchall()
        conn.close()

        if not resultados:
            resultado_label.configure(text="Nenhum filme encontrado com os filtros selecionados.")
        else:
            texto = "\n".join([f"🎬 {titulo} ({ano}) - {categoria} - {pais}" for titulo, pais, ano, categoria in resultados])
            resultado_label.configure(text=texto)

    ctk.CTkButton(janela_avancada, text="Filtrar", command=executar_filtros).pack(pady=10)

# === Interface Principal ===
titulo_label = ctk.CTkLabel(janela, text="Consulta de Premiações do Oscar", font=("Roboto", 22, "bold"))
titulo_label.pack(pady=10)

frame_input = ctk.CTkFrame(janela)
frame_input.pack(pady=10)

ctk.CTkLabel(frame_input, text="Título do Filme:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_titulo = ctk.CTkEntry(frame_input, width=300, font=("Roboto", 14))
entry_titulo.grid(row=0, column=1, padx=5, pady=5)

ctk.CTkButton(janela, text="Buscar", command=buscar_filme, fg_color="#4CAF50").pack(pady=5)
ctk.CTkButton(janela, text="Consulta Avançada", command=abrir_consulta_avancada, fg_color="#145da1").pack(pady=5)

label_resultado = ctk.CTkLabel(janela, text="", font=("Roboto", 14), justify="left")
label_resultado.pack(pady=10)

janela.mainloop()
