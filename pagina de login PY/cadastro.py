import customtkinter
import sqlite3
import subprocess

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x350")

# Conectar ao banco de dados e criar a tabela se não existir
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    senha TEXT NOT NULL
)
""")
conn.commit()
conn.close()

def abrir_outro_arquivo():
           subprocess.run(["python", "telalogin.PY"])  

def cadastrar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario and senha:  
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
        conn.commit()
        conn.close()

        resultado_cadastro.configure(text="Cadastro realizado com sucesso!", text_color="green")
        abrir_outro_arquivo() 

     
    else:
        resultado_cadastro.configure(text="Preencha todos os campos!", text_color="red")

texto = customtkinter.CTkLabel(janela, text="Tela de Cadastro")
entry_usuario = customtkinter.CTkEntry(janela, placeholder_text="Usuário")
entry_senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
botao_cadastrar = customtkinter.CTkButton(janela, text="Cadastrar", command=cadastrar)
resultado_cadastro = customtkinter.CTkLabel(janela, text="")

texto.pack(pady=10)
entry_usuario.pack(padx=10, pady=5)
entry_senha.pack(padx=10, pady=5)
botao_cadastrar.pack(pady=10)
resultado_cadastro.pack(pady=10)

janela.mainloop()
