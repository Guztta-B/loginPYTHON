import customtkinter
import sqlite3
import subprocess
from customtkinter import CTkImage, CTkLabel
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("300x300")

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

def validar_login():
    usuario = email.get()
    senha_digitada = senha.get()

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha_digitada))
    usuario_encontrado = cursor.fetchone()  
    conn.close()

    if usuario_encontrado:  
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')  
        abrir_outro_arquivo() 
    else:  
        resultado_login.configure(text='Login errado!', text_color='red')

def abrir_outro_arquivo():
    subprocess.run(["python", "tela2.py"])  

# Carregar a imagem corretamente
imagem_pil = Image.open("icone.png").resize((50, 50), Image.Resampling.LANCZOS)
imagem = CTkImage(light_image=imagem_pil)
imagem = CTkImage(light_image=imagem_pil, size=(100, 100))


# Criar um CTkLabel para exibir a imagem
label_imagem = CTkLabel(janela, image=imagem, text="")
label_imagem.pack(pady=10)  

email = customtkinter.CTkEntry(janela, placeholder_text="E-mail")  
senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")  
botao = customtkinter.CTkButton(janela, text="Login", command=validar_login)   
resultado_login = customtkinter.CTkLabel(janela, text="")   

email.pack(padx=10, pady=10)  
senha.pack(padx=10, pady=10)  
botao.pack(padx=10, pady=10)  
resultado_login.pack(pady=10)  

janela.mainloop()
