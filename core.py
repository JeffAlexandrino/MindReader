import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 
import time
import threading

# Janela "carregando"
def show_loading_window():
    loading_window = tk.Toplevel(root)
    loading_window.title("Lendo sua mente")
    loading_window.geometry("400x150")
    message = tk.Label(loading_window, text="Calculando probabilidades.", font=("Arial", 12))
    message.pack(pady=10)

    # Barra de progresso
    progress = tk.DoubleVar()
    progress_bar = ttk.Progressbar(loading_window, maximum=100, variable=progress)
    progress_bar.pack(pady=10, fill=tk.X, padx=20)

    messages = [
        "Escaneando ondas cerebrais",
        "Lendo seu histórico",
        "Analisando seu comportamento",
        "Rodando algoritmo de intuição artificial",
        "Decodificando seus pensamentos",
        "Conectando ao seu wi-fi mental", 
    ]
    
    def update_progress():
        for i in range(1, 101, 25):
            progress.set(i)
            message.config(text=messages[i // 25])
            loading_window.update_idletasks()  
            time.sleep(1)
        loading_window.destroy()
        show_result()  # Mostra o resultado após a janela de carregamento
    threading.Thread(target=update_progress).start() 

# Janela do resultado
def show_result():
    result_window = tk.Toplevel(root)
    result_window.title("Resultado")

    numEscolhido = entry.get()
    result_label = tk.Label(result_window, text=f"AHÁ! Você pensou no número {numEscolhido}.", font=("Arial", 12))
    result_label.pack(pady=10)

    try:
        original_image = Image.open("imagens\chitoge.png")
        resized_image = original_image.resize((400, 400))  # Ajuste para o tamanho desejado
        image = ImageTk.PhotoImage(resized_image)
        image_width, image_height = image.width(), image.height()   
        result_window.geometry(f"{image_width}x{image_height + 90}")

        # Exibe a imagem
        image_label = tk.Label(result_window, image=image)
        image_label.image = image
        image_label.pack(pady=10)
    except Exception as e:
        error_label = tk.Label(result_window, text=f"Erro ao carregar a imagem: {e}", font=("Arial", 10), fg="red")
        error_label.pack(pady=10)

# Função para iniciar o processo
def read_mind():
    try:
        numEscolhido = int(entry.get())
        if 0 <= numEscolhido <= 100:
            result.set("")
            show_loading_window()
        else:
            result.set("Insira um número entre 0 e 100.")
    except ValueError:
        result.set("Não sabe ler? Insira um NÚMERO entre 0 e 100.")

root = tk.Tk()
root.title("Mind Reader")
root.geometry("320x140") 

instruction = tk.Label(root, text="Pense em um número entre 0 e 100.", font=("Arial", 12))
instruction.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Ler minha mente.", command=read_mind, font=("Arial", 12))
button.pack(pady=5)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()
