import sqlite3
import customtkinter as ctk
from tkinter import *

janela = ctk.CTk()  # Criação da Janela principal


class Application():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela_login()
        janela.mainloop()


    def tema(self):    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")  
    
    def tela_login(self):
        #trabalhando com a imagem da tela
        title_label = ctk.CTkLabel(master=janela, text="Entre na sua conta e tenha \na plataforma", font=("Roboto", 20), fg_color= "green", text_color="#000000")
        title_label.place(x=15, y=10)
        #Imagem 
        img = PhotoImage(file="trocar1.png", width=500, height=500, master=janela) 
        label_img = ctk.CTkButton(master=janela, image=img, fg_color="#1a1a1a",text = None, hover = False,)
        label_img.place(x=-15, y=0)

        # Configurações da janela
        janela.resizable(False, False)
        janela.geometry("806x400")
        janela.title("Login")
        janela.iconbitmap("oscares.ico")  # Ícone da janela
        # Cor de fundo da janela

        #Imagem da tela

        #frame
        login_frame = ctk.CTkFrame(master=janela, width=400, height=500, fg_color="#000000")
        login_frame.pack(side=RIGHT)
        

        # widgets dentro do framde da tela de login
        label = ctk.CTkLabel(master= login_frame, text="Log in with your account", font=("Roboto", 30), text_color="#D8D8D8", width=350, height=80,)
        label.place(x=25, y=5)

        username_entry = ctk.CTkEntry(master= login_frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14)).place(x=50, y=95)
        username_label = ctk.CTkLabel(master= login_frame, text="*O campo de usuário é de caratér obrigatório", text_color="green", font=("Roboto", 14)).place(x=50, y=135)

        password_entry = ctk.CTkEntry(master= login_frame, placeholder_text="Senha de Usuário", width=300, font=("Roboto", 14), show="*").place(x=50, y=175)
        password_label = ctk.CTkLabel(master= login_frame, text="*O campo de senha é de caratér obrigatório", text_color="green", font=("Roboto", 14)).place(x=50, y=205)

        checkbox = ctk.CTkCheckBox(master= login_frame, text="Lembrar-se de mim", font=("Roboto", 16)).place(x=50, y=235)

        login_button = ctk.CTkButton(master= login_frame, text="Login", width=300, fg_color="#145da1").place(x=50, y=270)

        register_span = ctk.CTkLabel(master= login_frame, text="Não tem uma conta? ", font=("Roboto", 15), text_color="#FFFFFF").place(x=50, y=320)
        register_button = ctk.CTkButton(master= login_frame, text="Registrar-se", width=150, font=("Roboto", 15), fg_color= "#145da1").place(x=200, y=320)




Application()