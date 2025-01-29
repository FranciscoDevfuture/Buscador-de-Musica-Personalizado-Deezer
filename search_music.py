import tkinter as tk
from tkinter import messagebox
from deezer import Client

# Criando ambiente do cliente Deezer
deezer = Client()

# Função para buscar música
def buscar_musica():
    nome_musica = entrada_musica.get()

    if not nome_musica.strip():
        messagebox.showwarning("Erro", "Digite o nome de uma música!")
        return
    
    try:
        results = deezer.search(nome_musica)

        # Limpa os resultados anteriores
        lista_resultados.delete(0, tk.END)

        # Adiciona novos resultados
        for music in results:
            lista_resultados.insert(tk.END, f"{music.title} - {music.artist.name}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criando a Janela principal
root = tk.Tk()
root.title("Buscador de Música Personalizado(By-Francisco)\nGratidão por ter conseguido")
root.geometry("500x500")

# Criando Widgets da Interface
tk.Label(root, text="Digite o nome da música", font=("Arial", 12)).pack(pady=10)
entrada_musica = tk.Entry(root, width=40)
entrada_musica.pack(pady=5)

botao_buscar = tk.Button(root, text="Buscar", command=buscar_musica, font=("Arial", 12), bg="lightblue")
botao_buscar.pack(pady=10)

lista_resultados = tk.Listbox(root, width=50, height=15)
lista_resultados.pack(pady=10)

# Inicia o loop da interface
root.mainloop()