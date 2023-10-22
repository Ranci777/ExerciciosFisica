import tkinter as tk

def calcular():
    forma = var_forma.get()
    if forma == "Círculo":
        raio = float(entry_raio.get())
        area = 3.14 * (raio**2)
        resultado.set(f"Área do círculo: {area}")
    elif forma == "Quadrado":
        lado = float(entry_lado.get())
        area = lado**2
        perimetro = 4 * lado
        resultado.set(f"Área do quadrado: {area}\nPerímetro do quadrado: {perimetro}")
    elif forma == "Cubo":
        aresta = float(entry_aresta.get())
        volume = aresta**3
        area_superficie = 6 * (aresta**2)
        resultado.set(f"Volume do cubo: {volume}\nÁrea da superfície do cubo: {area_superficie}")
    else:
        resultado.set("Selecione uma forma válida.")

# Criando a janela
root = tk.Tk()
root.title("Calculadora Geométrica")

# Variáveis
var_forma = tk.StringVar(root)
var_forma.set("Círculo")
resultado = tk.StringVar()

# Labels
label_forma = tk.Label(root, text="Selecione a forma:")
label_forma.grid(row=0, column=0, padx=5, pady=5, sticky="w")

label_raio = tk.Label(root, text="Raio:")
label_raio.grid(row=1, column=0, padx=5, pady=5, sticky="w")

label_lado = tk.Label(root, text="Lado:")
label_lado.grid(row=2, column=0, padx=5, pady=5, sticky="w")

label_aresta = tk.Label(root, text="Aresta:")
label_aresta.grid(row=3, column=0, padx=5, pady=5, sticky="w")

label_resultado = tk.Label(root, textvariable=resultado, font=("Arial", 12, "bold"))
label_resultado.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

# Entradas
entry_raio = tk.Entry(root)
entry_raio.grid(row=1, column=1, padx=5, pady=5)

entry_lado = tk.Entry(root)
entry_lado.grid(row=2, column=1, padx=5, pady=5)

entry_aresta = tk.Entry(root)
entry_aresta.grid(row=3, column=1, padx=5, pady=5)

# Menu suspenso para selecionar a forma
menu_forma = tk.OptionMenu(root, var_forma, "Círculo", "Quadrado", "Cubo")
menu_forma.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Botão de cálculo
botao_calcular = tk.Button(root, text="Calcular", command=calcular)
botao_calcular.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

# Rodar o aplicativo
root.mainloop()
