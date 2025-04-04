import tkinter as tk
from tkinter import ttk
import cv2
import PIL.Image, PIL.ImageTk
from moviepy import VideoFileClip
import pygame
import threading
import time

# Criar a janela
janela = tk.Tk()
janela.title("Vídeo com Áudio")
janela.geometry("640x480")

# Caminho do vídeo
video_path = "videoplayback.mp4"  # Substitua pelo seu arquivo

# Criar um Label para exibir o vídeo
label_video = tk.Label(janela)
label_video.pack()

# Inicializar pygame para tocar o áudio
pygame.mixer.init()

# Função para reproduzir o vídeo
def reproduzir_video():
    cap = cv2.VideoCapture(video_path)

    # Obter FPS do vídeo
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_time = 1 / fps  # Tempo entre os frames

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Sai do loop quando o vídeo termina

        # Converter o frame para um formato que o Tkinter entende
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = PIL.Image.fromarray(frame)
        frame = PIL.ImageTk.PhotoImage(frame)

        # Exibir o frame na interface gráfica
        label_video.configure(image=frame)
        label_video.image = frame

        # Respeitar o tempo do vídeo
        time.sleep(frame_time)
        janela.update_idletasks()
        janela.update()

    cap.release()

# Função para tocar o áudio do vídeo
def tocar_audio():
    clip = VideoFileClip(video_path)
    audio_path = "temp_audio.mp3"  # Salvar o áudio temporariamente

    # Extrair áudio do vídeo e salvar como MP3
    clip.audio.write_audiofile(audio_path, codec="mp3")

    # Tocar o áudio extraído
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

# Botão para iniciar o vídeo e o áudio simultaneamente
def iniciar_video():
    threading.Thread(target=reproduzir_video, daemon=True).start()
    threading.Thread(target=tocar_audio, daemon=True).start()

botao_iniciar = ttk.Button(janela, text="Reproduzir Vídeo", command=iniciar_video)
botao_iniciar.pack(pady=10)

janela.mainloop()
