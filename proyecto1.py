import tkinter as tk
import tkinter.font as tkfont

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

def algoritmo_DDA(x1, y1, x2, y2):
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

    return zip(puntos_x, puntos_y)


root = tk.Tk()
root.title("Algoritmos de trazado de Líneas")
root.minsize(530,800)
root.resizable(False, False)
root.config(background="#DEBFA9")
center_window(root)

FirstFrame = tk.Frame(root, width=510, height=780, background="#DEBFA9")
FirstFrame.pack()
FirstFrame.place(relx=0.5, rely=0.5, anchor="center")


tk.Label(FirstFrame, text="Seleccione un algoritmo", font=tkfont.Font(family="Consolas", size=20, weight="bold"), background="#DEBFA9").place(relx=0.5, anchor="center", y=40)


Botones = [
    ("Algoritmo DDA", BotonAlgoritmoDDA, 130),
    ("Algoritmo Bresenham", BotonAlgoritmoBresenham, 200),
    ("Algoritmo Circunferencia", BotonAlgoritmoCircunferencia, 270),
    ("Algoritmo Elipse", BotonAlgoritmoElipse, 340)
]

for texto, redireccion, coordenada_y in Botones:
    button = tk.Button(FirstFrame, text=texto, command=redireccion, font=tkfont.Font(family="Consolas", size=16), relief="flat", bg="#2E8F62", activebackground="#486148", activeforeground="#FFFFFF", cursor="hand2")
    button.place(relx=0.5, anchor="center", y=coordenada_y, width=340, height=60)



VentanaDDA = tk.Toplevel(root)
VentanaDDA.title("Algoritmo DDA")
VentanaDDA.minsize(530,800)
VentanaDDA.resizable(False, False)
VentanaDDA.config(background="#DEBFA9")
VentanaDDA.withdraw()

tk.Label(VentanaDDA, text="Ingrese los datos", font=tkfont.Font(family="Consolas", size=20, weight="bold"), background="#DEBFA9").grid(row=0, column=1, columnspan=4, pady=20)

tk.Label(VentanaDDA, text="x1:", font=tkfont.Font(family="Consolas", size=16), background="#DEBFA9").grid(row=1, column=1, pady=5)
entry_x1 = tk.Entry(VentanaDDA, font=tkfont.Font(family="Consolas", size=16), width=10)
entry_x1.grid(row=1, column=2, pady=5)


tk.Label(VentanaDDA, text="y1:", font=tkfont.Font(family="Consolas", size=16), background="#DEBFA9").grid(row=1, column=3, pady=5)
entry_y1 = tk.Entry(VentanaDDA, font=tkfont.Font(family="Consolas", size=16), width=10)
entry_y1.grid(row=1, column=4, pady=5)


tk.Label(VentanaDDA, text="x2:", font=tkfont.Font(family="Consolas", size=16), background="#DEBFA9").grid(row=2, column=1, pady=5)
entry_x2 = tk.Entry(VentanaDDA, font=tkfont.Font(family="Consolas", size=16), width=10)
entry_x2.grid(row=2, column=2, pady=5)


tk.Label(VentanaDDA, text="y2:", font=tkfont.Font(family="Consolas", size=16), background="#DEBFA9").grid(row=2, column=3, pady=5)
entry_y2 = tk.Entry(VentanaDDA, font=tkfont.Font(family="Consolas", size=16), width=10)
entry_y2.grid(row=2, column=4, pady=5)


for widget in VentanaDDA.winfo_children():
    widget.grid_configure(padx=10, pady=5, sticky="ew")




VentanaBresenham = tk.Toplevel(root)
VentanaBresenham.title("Algoritmo Bresenham")
VentanaBresenham.minsize(530,800)
VentanaBresenham.resizable(False, False)
VentanaBresenham.config(background="#DEBFA9")
VentanaBresenham.withdraw()  


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