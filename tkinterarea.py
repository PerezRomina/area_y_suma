import tkinter as tk
from tkinter import messagebox

def calcular_area():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        area = (base * altura) / 2
        label_resultado.config(text=f"El area es de : {area:.2f}")
    except ValueError:
        messagebox.showerror("error .")

ventana = tk.Tk()
ventana.title(" Área del Triángulo")
ventana.geometry("300x200")

label_base = tk.Label(ventana, text="Ingresa la base :")
label_base.pack()

entry_base = tk.Entry(ventana)
entry_base.pack()

label_altura = tk.Label(ventana, text="Ingresa la altua:")
label_altura.pack()

entry_altura = tk.Entry(ventana)
entry_altura.pack()

boton_calcular = tk.Button(ventana, text="Calcular Área", command=calcular_area)
boton_calcular.pack(pady=10)

label_resultado = tk.Label(ventana, text="Área: ")
label_resultado.pack()

ventana.mainloop()