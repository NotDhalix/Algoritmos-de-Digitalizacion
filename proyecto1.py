import tkinter as tk
import tkinter.font as tkfont
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import sys


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

def BotonIntegrantes():
    root.withdraw()
    VentanaIntegrantes.deiconify()
    center_window(VentanaIntegrantes)   

def close_window(window):
    window.withdraw()
    root.deiconify()

def cerrar_app():
    root.destroy()
    sys.exit()  

def algoritmo_DDA():     
    if entry_x1_dda.get() == '' or entry_y1_dda.get() == '' or entry_x2_dda.get() == '' or entry_y2_dda.get() == '':
        tk.messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    
    x1 = int(entry_x1_dda.get())
    y1 = int(entry_y1_dda.get())
    x2 = int(entry_x2_dda.get())
    y2 = int(entry_y2_dda.get())
    
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
    plt.xticks(np.arange(min(puntos_x), max(puntos_x)+1, 1.0))
    plt.yticks(np.arange(min(puntos_y), max(puntos_y)+1, 1.0))
    plt.title('Grafica de Algoritmo DDA')

    canvas = FigureCanvasTkAgg(fig, master=DDAFrame)
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=4, pady=20)

    
    return list(zip(puntos_x, puntos_y))

def algoritmo_Bresenham():
    
    if entry_x1_bresenham.get() == '' or entry_y1_bresenham.get() == '' or entry_x2_bresenham.get() == '' or entry_y2_bresenham.get() == '':
        tk.messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    x1 = int(entry_x1_bresenham.get())
    y1 = int(entry_y1_bresenham.get())
    x2 = int(entry_x2_bresenham.get())
    y2 = int(entry_y2_bresenham.get())
    
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


def CircunferenciaBresenham():

    if entry_radio_circunferencia.get() == '' or entry_x0_circunferencia.get() == '' or entry_y0_circunferencia.get() == '':
        tk.messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    
    x = int(entry_radio_circunferencia.get())
    y = 0
    err = 0
    xc = int(entry_x0_circunferencia.get())
    yc = int(entry_y0_circunferencia.get())

    fig = plt.figure(figsize=(5, 5), dpi=100)  
    plt.grid(True)  
    plt.title('Circunferencia con Algoritmo Bresenham') 

    while x >= y:
        plt.scatter(xc + x, yc + y) 
        plt.scatter(xc + y, yc + x)
        plt.scatter(xc - y, yc + x)
        plt.scatter(xc - x, yc + y)
        plt.scatter(xc - x, yc - y)
        plt.scatter(xc - y, yc - x)
        plt.scatter(xc + y, yc - x)
        plt.scatter(xc + x, yc - y)

        y += 1
        err += 1 + 2 * y
        if 2 * (err - x) + 1 > 0:
            x -= 1
            err += 1 - 2 * x

    canvas = FigureCanvasTkAgg(fig, master=CircunferenciaFrame) 
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=4, pady=20)  

def plot_ellipse_points(x, y, xc, yc):
    plt.scatter(xc + x, yc + y)
    plt.scatter(xc - x, yc + y)
    plt.scatter(xc + x, yc - y)
    plt.scatter(xc - x, yc - y)

def ElipseBresenham():

    if entry_rx_elipse.get() == '' or entry_ry_elipse.get() == '' or entry_xc_elipse.get() == '' or entry_yc_elipse.get() == '':
        tk.messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    rx = int(entry_rx_elipse.get())
    ry = int(entry_ry_elipse.get())
    xc = int(entry_xc_elipse.get())
    yc = int(entry_yc_elipse.get())
    x = 0
    y = ry
    a_sqr = rx * rx
    b_sqr = ry * ry
    d1 = (b_sqr - (a_sqr * ry) + (0.25 * a_sqr))
    dx = 2 * b_sqr * x
    dy = 2 * a_sqr * y

    puntos_x = []
    puntos_y = []

    while dx < dy:
        puntos_x.extend([x, -x, x, -x])
        puntos_y.extend([y, y, -y, -y])
        if d1 < 0:
            x += 1
            dx = dx + (2 * b_sqr)
            d1 = d1 + dx + (b_sqr)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * b_sqr)
            dy = dy - (2 * a_sqr)
            d1 = d1 + dx - dy + b_sqr

    d2 = (b_sqr * ((x + 0.5) * (x + 0.5))) + (a_sqr * ((y - 1) * (y - 1))) - (a_sqr * b_sqr)
    while y >= 0:
        puntos_x.extend([x, -x, x, -x])
        puntos_y.extend([y, y, -y, -y])
        if d2 > 0:
            y -= 1
            dy = dy - (2 * a_sqr)
            d2 = d2 + (a_sqr) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * b_sqr)
            dy = dy - (2 * a_sqr)
            d2 = d2 + dx - dy + a_sqr

    puntos_x = [p + xc for p in puntos_x]
    puntos_y = [p + yc for p in puntos_y]

    fig = plt.figure(figsize=(6, 6))
    plt.grid(True)
    plt.title('Elipse con Algoritmo Bresenham')
    plt.scatter(puntos_x, puntos_y)

    canvas = FigureCanvasTkAgg(fig, master=ElipseFrame)
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=4, pady=20)

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
    ("Algoritmo Elipse", BotonAlgoritmoElipse, 340),
    ("Integrantes", BotonIntegrantes, 550)
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
entry_x1_dda = tk.Entry(DDAFrame, font=textos, width=10)
entry_x1_dda.grid(row=1, column=1, pady=5)

tk.Label(DDAFrame, text="y1:", font=textos, background="#DEBFA9").grid(row=1, column=2, pady=5)
entry_y1_dda = tk.Entry(DDAFrame, font=textos, width=10)
entry_y1_dda.grid(row=1, column=3, pady=5)

tk.Label(DDAFrame, text="x2:", font=textos, background="#DEBFA9").grid(row=2, column=0, pady=5)
entry_x2_dda = tk.Entry(DDAFrame, font=textos, width=10)
entry_x2_dda.grid(row=2, column=1, pady=5)

tk.Label(DDAFrame, text="y2:", font=textos, background="#DEBFA9").grid(row=2, column=2, pady=5)
entry_y2_dda = tk.Entry(DDAFrame, font=textos, width=10)
entry_y2_dda.grid(row=2, column=3, pady=5)

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
entry_x1_bresenham = tk.Entry(BresenhamFrame, font=textos, width=10)
entry_x1_bresenham.grid(row=1, column=1, pady=5)

tk.Label(BresenhamFrame, text="y1:", font=textos, background="#DEBFA9").grid(row=1, column=2, pady=5)
entry_y1_bresenham = tk.Entry(BresenhamFrame, font=textos, width=10)
entry_y1_bresenham.grid(row=1, column=3, pady=5)

tk.Label(BresenhamFrame, text="x2:", font=textos, background="#DEBFA9").grid(row=2, column=0, pady=5)
entry_x2_bresenham = tk.Entry(BresenhamFrame, font=textos, width=10)
entry_x2_bresenham.grid(row=2, column=1, pady=5)

tk.Label(BresenhamFrame, text="y2:", font=textos, background="#DEBFA9").grid(row=2, column=2, pady=5)
entry_y2_bresenham = tk.Entry(BresenhamFrame, font=textos, width=10)
entry_y2_bresenham.grid(row=2, column=3, pady=5)

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

CircunferenciaFrame = tk.Frame(VentanaCircunferencia, background="#DEBFA9")
CircunferenciaFrame.pack()
CircunferenciaFrame.place(relx=0.5, rely=0, anchor="n")

tk.Label(CircunferenciaFrame, text="Ingrese los datos", font=titulos, background="#DEBFA9").grid(row=0, column=1, columnspan=2, pady=20)

tk.Label(CircunferenciaFrame, text="x0:", font=textos, background="#DEBFA9").grid(row=1, column=0, pady=5)
entry_x0_circunferencia = tk.Entry(CircunferenciaFrame, font=textos, width=10)
entry_x0_circunferencia.grid(row=1, column=1, pady=5)

tk.Label(CircunferenciaFrame, text="y0:", font=textos, background="#DEBFA9").grid(row=1, column=2, pady=5)
entry_y0_circunferencia = tk.Entry(CircunferenciaFrame, font=textos, width=10)
entry_y0_circunferencia.grid(row=1, column=3, pady=5)

tk.Label(CircunferenciaFrame, text="radio:", font=textos, background="#DEBFA9").grid(row=2, column=0, pady=5)
entry_radio_circunferencia = tk.Entry(CircunferenciaFrame, font=textos, width=10)
entry_radio_circunferencia.grid(row=2, column=1, pady=5)


button = tk.Button(CircunferenciaFrame, text="Generar Circunferencia", command=CircunferenciaBresenham, font=textos, relief="flat", bg="#2E8F62", activebackground="#486148", activeforeground="#FFFFFF", cursor="hand2")
button.grid(row=3, column=0, columnspan=4, pady=20)
button.place(relx=0.5, rely=1.0, anchor="s")



for widget in CircunferenciaFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


VentanaElipse = tk.Toplevel(root)
VentanaElipse.title("Algoritmo Elipse")
VentanaElipse.minsize(530,800)
VentanaElipse.resizable(False, False)
VentanaElipse.config(background="#DEBFA9")
VentanaElipse.withdraw()

ElipseFrame = tk.Frame(VentanaElipse, background="#DEBFA9")
ElipseFrame.pack()
ElipseFrame.place(relx=0.5, rely=0, anchor="n")

tk.Label(ElipseFrame, text="Ingrese los datos", font=titulos, background="#DEBFA9").grid(row=0, column=1, columnspan=2, pady=20)

tk.Label(ElipseFrame, text="Radio X:", font=textos, background="#DEBFA9").grid(row=1, column=0, pady=5)
entry_rx_elipse = tk.Entry(ElipseFrame, font=textos, width=10)
entry_rx_elipse.grid(row=1, column=1, pady=5)

tk.Label(ElipseFrame, text="Radio Y:", font=textos, background="#DEBFA9").grid(row=1, column=2, pady=5)
entry_ry_elipse = tk.Entry(ElipseFrame, font=textos, width=10)
entry_ry_elipse.grid(row=1, column=3, pady=5)

tk.Label(ElipseFrame, text="Centro X:", font=textos, background="#DEBFA9").grid(row=2, column=0, pady=5)
entry_xc_elipse = tk.Entry(ElipseFrame, font=textos, width=10)
entry_xc_elipse.grid(row=2, column=1, pady=5)

tk.Label(ElipseFrame, text="Centro Y:", font=textos, background="#DEBFA9").grid(row=2, column=2, pady=5)
entry_yc_elipse = tk.Entry(ElipseFrame, font=textos, width=10)
entry_yc_elipse.grid(row=2, column=3, pady=5)

button = tk.Button(ElipseFrame, text="Generar Elipse", command=ElipseBresenham, font=textos, relief="flat", bg="#2E8F62", activebackground="#486148", activeforeground="#FFFFFF", cursor="hand2")
button.grid(row=3, column=0, columnspan=4, pady=20)
button.place(relx=0.5, rely=1.0, anchor="s")


for widget in ElipseFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

VentanaIntegrantes = tk.Toplevel(root)
VentanaIntegrantes.title("Integrantes")
VentanaIntegrantes.minsize(530,800)
VentanaIntegrantes.resizable(False, False)
VentanaIntegrantes.config(background="#DEBFA9")
VentanaIntegrantes.withdraw()
tk.Label(VentanaIntegrantes, text="Integrantes", font=titulos, background="#DEBFA9").place(relx=0.5, anchor="center", y=40)
tk.Label(VentanaIntegrantes, text="Gonzalez, Alejandro      E-8-182476", font=textos, background="#DEBFA9").place(relx=0.5, anchor="center", y=150)
tk.Label(VentanaIntegrantes, text="Rodriguez, Alfonso       8-994-2393", font=textos, background="#DEBFA9").place(relx=0.5, anchor="center", y=200)
tk.Label(VentanaIntegrantes, text="Rosales, Jordy           3-750-898", font=textos, background="#DEBFA9").place(relx=0.5, anchor="center", y=250)
tk.Label(VentanaIntegrantes, text="Valdes, Nicole           9-987-2665", font=textos, background="#DEBFA9").place(relx=0.5, anchor="center", y=300)


for window in [VentanaDDA, VentanaBresenham, VentanaCircunferencia, VentanaElipse, VentanaIntegrantes]:
    window.protocol("WM_DELETE_WINDOW", lambda window=window: close_window(window))

root.protocol("WM_DELETE_WINDOW", cerrar_app)

root.mainloop()