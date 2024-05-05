import tkinter as tk
import tkinter.font as tkfont
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"+{x}+{y}")

def BotonAlgoritmoDDA():
    root.withdraw()
    VentanaDDA.deiconify()
    center_window(VentanaDDA)  

def BotonAlgoritmoBresenham():
    root.withdraw()
    VentanaBresenham.deiconify()
    center_window(VentanaBresenham)  

def BotonAlgoritmoCircunferencia():
    root.withdraw()
    VentanaCircunferencia.deiconify()
    center_window(VentanaCircunferencia)  

def BotonAlgoritmoElipse():
    root.withdraw()
    VentanaElipse.deiconify()
    center_window(VentanaElipse)   

def close_window(window):
    window.withdraw()
    root.deiconify()  

def algoritmo_DDA():
    
    x1 = int(entry_x1.get())
    y1 = int(entry_y1.get())
    x2 = int(entry_x2.get())
    y2 = int(entry_y2.get())
    
    # Calcular deltas
    delta_x = x2 - x1
    delta_y = y2 - y1

    # Calcular pendiente
    if delta_x != 0:
        m = round(delta_y / delta_x, 1)
    else:
        m = "ND"

    # Número de pasos
    if abs(delta_x) > abs(delta_y):
        num_pasos = abs(delta_x)
    else:
        num_pasos = abs(delta_y)

    # Pasos de delta x e y
    if num_pasos != 0:
        paso_x = round(delta_x / num_pasos, 1)
        paso_y = round(delta_y / num_pasos, 1)
    else:
        paso_x = 0
        paso_y = 0

    # Array para almacenar los puntos almacenados de x e y
    puntos_x = [x1]
    puntos_y = [y1]

    # Generar los puntos de x e y
    for _ in range(round(num_pasos)):  
        x1 += paso_x
        y1 += paso_y
        puntos_x.append(round(x1))
        puntos_y.append(round(y1))

    fig = plt.figure(figsize=(5, 5), dpi=100)
    plt.plot(puntos_x, puntos_y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.title('DDA Algorithm Graph')

    canvas = FigureCanvasTkAgg(fig, master=DDAFrame)
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=4, pady=20)

    
    return list(zip(puntos_x, puntos_y))

def algoritmo_Bresenham():
    
    x1 = int(entry_x1.get())
    y1 = int(entry_y1.get())
    x2 = int(entry_x2.get())
    y2 = int(entry_y2.get())
    
    #Calcular deltas
    delta_x = x2 - x1
    delta_y = y2 - y1

    # Determinar la magnitud de los incrementos
    if delta_x < 0:
        inc_x = -1
    else:
        inc_x = 1
    if delta_y < 0:
        inc_y = -1
    else:
        inc_y = 1
        
    delta_x = abs(delta_x)
    delta_y = abs(delta_y)

    # Calcular las constantes
    if delta_y > delta_x:
        delta_x, delta_y = delta_y, delta_x
        interchange = True
    else:
        interchange = False
        
    #Calcular los deltas * 2 y la p    
    two_dx = 2 * delta_x
    two_dy = 2 * delta_y
    p = two_dy - delta_x

    # Variables de inicio
    x = x1
    y = y1

    # Inicializar las listas para almacenar los puntos
    puntos_x = []
    puntos_y = []
    pk = []

    # Generar puntos usando el algoritmo de Bresenham
    for _ in range(delta_x):
        puntos_x.append(x)
        puntos_y.append(y)
        pk.append(p)

        if p >= 0:
            if interchange:
                x += inc_x
            else:
                y += inc_y
            p -= two_dx
        if p < 0:
            if interchange:
                y += inc_y
            else:
                x += inc_x
            p += two_dy

    fig = plt.figure(figsize=(5, 5), dpi=100)
    plt.plot(puntos_x, puntos_y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.title('Gráfica Algoritmo Bresenham')

    canvas = FigureCanvasTkAgg(fig, master=BresenhamFrame)
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=4, pady=20)

    
    return list(zip(puntos_x, puntos_y))


root = tk.Tk()

titulos = tkfont.Font(family="Consolas", size=20, weight="bold")
textos = tkfont.Font(family="Consolas", size=16)


root.title("Algoritmos de trazado de Líneas")
root.minsize(530,800)
root.resizable(False, False)
root.config(background="#DEBFA9")
center_window(root)

FirstFrame = tk.Frame(root, width=510, height=780, background="#DEBFA9")
FirstFrame.pack()
FirstFrame.place(relx=0.5, rely=0.5, anchor="center")


tk.Label(FirstFrame, text="Seleccione un algoritmo", font=titulos, background="#DEBFA9").place(relx=0.5, anchor="center", y=40)


Botones = [
    ("Algoritmo DDA", BotonAlgoritmoDDA, 130),
    ("Algoritmo Bresenham", BotonAlgoritmoBresenham, 200),
    ("Algoritmo Circunferencia", BotonAlgoritmoCircunferencia, 270),
    ("Algoritmo Elipse", BotonAlgoritmoElipse, 340)
]

for texto, redireccion, coordenada_y in Botones:
    button = tk.Button(FirstFrame, text=texto, command=redireccion, font=textos, relief="flat", bg="#2E8F62", activebackground="#486148", activeforeground="#FFFFFF", cursor="hand2")
    button.place(relx=0.5, anchor="center", y=coordenada_y, width=340, height=60)


VentanaDDA = tk.Toplevel(root)
VentanaDDA.title("Algoritmo DDA")
VentanaDDA.minsize(530, 800)
VentanaDDA.resizable(False, False)
VentanaDDA.config(background="#DEBFA9")
VentanaDDA.withdraw()

DDAFrame = tk.Frame(VentanaDDA, background="#DEBFA9")
DDAFrame.pack()
DDAFrame.place(relx=0.5, rely=0, anchor="n")

tk.Label(DDAFrame, text="Ingrese los datos", font=titulos, background="#DEBFA9").grid(row=0, column=1, columnspan=2, pady=20)

tk.Label(DDAFrame, text="x1:", font=textos, background="#DEBFA9").grid(row=1, column=0, pady=5)
entry_x1 = tk.Entry(DDAFrame, font=textos, width=10)
entry_x1.grid(row=1, column=1, pady=5)

tk.Label(DDAFrame, text="y1:", font=textos, background="#DEBFA9").grid(row=1, column=2, pady=5)
entry_y1 = tk.Entry(DDAFrame, font=textos, width=10)
entry_y1.grid(row=1, column=3, pady=5)

tk.Label(DDAFrame, text="x2:", font=textos, background="#DEBFA9").grid(row=2, column=0, pady=5)
entry_x2 = tk.Entry(DDAFrame, font=textos, width=10)
entry_x2.grid(row=2, column=1, pady=5)

tk.Label(DDAFrame, text="y2:", font=textos, background="#DEBFA9").grid(row=2, column=2, pady=5)
entry_y2 = tk.Entry(DDAFrame, font=textos, width=10)
entry_y2.grid(row=2, column=3, pady=5)

button = tk.Button(DDAFrame, text="Generar Línea", command=algoritmo_DDA, font=textos, relief="flat", bg="#2E8F62", activebackground="#486148", activeforeground="#FFFFFF", cursor="hand2")
button.grid(row=3, column=0, columnspan=4, pady=20)
button.place(relx=0.5, rely=1.0, anchor="s")



for widget in DDAFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


VentanaBresenham = tk.Toplevel(root)
VentanaBresenham.title("Algoritmo Bresenham")
VentanaBresenham.minsize(530,800)
VentanaBresenham.resizable(False, False)
VentanaBresenham.config(background="#DEBFA9")
VentanaBresenham.withdraw()  

BresenhamFrame = tk.Frame(VentanaBresenham, background="#DEBFA9")
BresenhamFrame.pack()
BresenhamFrame.place(relx=0.5, rely=0, anchor="n")

tk.Label(BresenhamFrame, text="Ingrese los datos", font=titulos, background="#DEBFA9").grid(row=0, column=1, columnspan=2, pady=20)

tk.Label(BresenhamFrame, text="x1:", font=textos, background="#DEBFA9").grid(row=1, column=0, pady=5)
entry_x1 = tk.Entry(BresenhamFrame, font=textos, width=10)
entry_x1.grid(row=1, column=1, pady=5)

tk.Label(BresenhamFrame, text="y1:", font=textos, background="#DEBFA9").grid(row=1, column=2, pady=5)
entry_y1 = tk.Entry(BresenhamFrame, font=textos, width=10)
entry_y1.grid(row=1, column=3, pady=5)

tk.Label(BresenhamFrame, text="x2:", font=textos, background="#DEBFA9").grid(row=2, column=0, pady=5)
entry_x2 = tk.Entry(BresenhamFrame, font=textos, width=10)
entry_x2.grid(row=2, column=1, pady=5)

tk.Label(BresenhamFrame, text="y2:", font=textos, background="#DEBFA9").grid(row=2, column=2, pady=5)
entry_y2 = tk.Entry(BresenhamFrame, font=textos, width=10)
entry_y2.grid(row=2, column=3, pady=5)

button = tk.Button(BresenhamFrame, text="Generar Línea", command=algoritmo_Bresenham, font=textos, relief="flat", bg="#2E8F62", activebackground="#486148", activeforeground="#FFFFFF", cursor="hand2")
button.grid(row=3, column=0, columnspan=4, pady=20)
button.place(relx=0.5, rely=1.0, anchor="s")



for widget in BresenhamFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)



VentanaCircunferencia = tk.Toplevel(root)
VentanaCircunferencia.title("Algoritmo Circunferencia")
VentanaCircunferencia.minsize(530,800)
VentanaCircunferencia.resizable(False, False)
VentanaCircunferencia.config(background="#DEBFA9")
VentanaCircunferencia.withdraw() 


VentanaElipse = tk.Toplevel(root)
VentanaElipse.title("Algoritmo Elipse")
VentanaElipse.minsize(530,800)
VentanaElipse.resizable(False, False)
VentanaElipse.config(background="#DEBFA9")
VentanaElipse.withdraw()


for window in [VentanaDDA, VentanaBresenham, VentanaCircunferencia, VentanaElipse]:
    window.protocol("WM_DELETE_WINDOW", lambda window=window: close_window(window))

root.mainloop()