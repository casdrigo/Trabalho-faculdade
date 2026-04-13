import tkinter as tk
#variaveis
carroA = 0
carroB = 0
pedestre = 0
estado = "VIA A VERDE"
#Click do botão A
def clickA():
    global carroA
    carroA = 1
#Click do botão B
def clickB():
    global carroB
    carroB = 1
#Click do botão P
def clickP():
    global pedestre
    pedestre = 1
#Click do botão Limpar
def limpar():
    global carroA, carroB, pedestre
    carroA = 0
    carroB = 0
    pedestre = 0

def rodarSemaforo():
    global estado, carroA, carroB, pedestre

    if pedestre == 1:
        
        if estado == "VIA A VERDE":
            novo_estado = "AMARELO A"
        elif estado == "VIA B VERDE":
            novo_estado = "AMARELO B"
        else:
            novo_estado = "PEDESTRE ATIVO"
            
    elif carroA == 1 and carroB == 0:
        
        if estado == "VIA B VERDE":
            novo_estado = "AMARELO B"
        else:
            novo_estado = "VIA A VERDE"
            
    elif carroA == 0 and carroB == 1:
        
        if estado == "VIA A VERDE":
            novo_estado = "AMARELO A"
        else:
            novo_estado = "VIA B VERDE"
            
    elif carroA == 1 and carroB == 1:
        if estado == "VIA A VERDE":
            novo_estado = "AMARELO A"
        elif estado == "AMARELO A":
            novo_estado = "VIA B VERDE"
        elif estado == "VIA B VERDE":
            novo_estado = "AMARELO B"
        elif estado == "AMARELO B":
            novo_estado = "VIA A VERDE"
        else:
            novo_estado = "VIA A VERDE"
    else:
        novo_estado = "AMARELO PISCANTE"

    estado = novo_estado

    texto_sensores["text"] = f"Sensores: A={carroA} | B={carroB} | Ped={pedestre}"
    texto_estado["text"] = "Estado: " + estado

    if estado == "VIA A VERDE":
        cor_a["bg"] = "green"
        cor_b["bg"] = "red"
        cor_p["bg"] = "red"
    elif estado == "VIA B VERDE":
        cor_a["bg"] = "red"
        cor_b["bg"] = "green"
        cor_p["bg"] = "red"
    elif estado == "AMARELO A":
        cor_a["bg"] = "yellow"
        cor_b["bg"] = "red"
        cor_p["bg"] = "red"
    elif estado == "AMARELO B":
        cor_a["bg"] = "red"
        cor_b["bg"] = "yellow"
        cor_p["bg"] = "red"
    elif estado == "PEDESTRE ATIVO":
        cor_a["bg"] = "red"
        cor_b["bg"] = "red"
        cor_p["bg"] = "green"
    else:
        if cor_a["bg"] == "yellow":
            cor_a["bg"] = "black"
            cor_b["bg"] = "black"
        else:
            cor_a["bg"] = "yellow"
            cor_b["bg"] = "yellow"
        cor_p["bg"] = "red"

    janela.after(3000, rodarSemaforo)

janela = tk.Tk()
janela.geometry("300x500")
janela.title("Semáforo")

tk.Button(janela, text="Carro Via A", command=clickA).pack(pady=5)
tk.Button(janela, text="Carro Via B", command=clickB).pack(pady=5)
tk.Button(janela, text="Pedestre", command=clickP).pack(pady=5)
tk.Button(janela, text="Limpar Sensores", command=limpar).pack(pady=5)

texto_sensores = tk.Label(janela, text="Sensores: A=0 | B=0 | Ped=0")
texto_sensores.pack(pady=10)

texto_estado = tk.Label(janela, text="Estado: VIA A VERDE", font=("Arial", 12, "bold"))
texto_estado.pack(pady=10)

tk.Label(janela, text="VIA A").pack()
cor_a = tk.Label(janela, width=10, height=2, bg="gray")
cor_a.pack()

tk.Label(janela, text="VIA B").pack()
cor_b = tk.Label(janela, width=10, height=2, bg="gray")
cor_b.pack()

tk.Label(janela, text="PEDESTRE").pack()
cor_p = tk.Label(janela, width=10, height=2, bg="gray")
cor_p.pack()

janela.after(1000, rodarSemaforo)
janela.mainloop()