import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

# Função de animação
def animate(i):
    ax.clear()
    ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], 'g-')
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    ax.set_title("Resolução Exercícios Física 1")
    ax.set_xlabel("Missão: Aprender Física de forma descomplicada")

# Criando a janela
root = tk.Tk()
root.title("Resolução Exercícios Física 1")

# Criando o frame do gráfico
frame = ttk.Frame(root, width=300, height=300)
frame.grid(row=0, column=0, padx=10, pady=10)

# Criando o gráfico
fig, ax = plt.subplots(figsize=(3, 3))
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Iniciando a animação
ani = FuncAnimation(fig, animate, frames=10, interval=500, repeat=True)

# Rodando o aplicativo
root.mainloop()
