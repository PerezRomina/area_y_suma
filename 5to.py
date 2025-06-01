import tkinter as tk

def suma():
   valoa = int(entrada_prim.get())
   valorb = int(entrada_seg.get())
   resultado = valoa + valorb
   etiqueta_resultado.config(text=f"El num1 es {valoa}, el num2 es {valorb}, y su resultado de la suma es  {resultado}") 


ventana = tk.Tk()
ventana.title("operacion de suma y resta ")
ventana.geometry("500x400")



etiqueta = tk.Label(ventana, text="Ingresa el primer numero:")
etiqueta.pack()

entrada_prim = tk.Entry(ventana)
entrada_prim.pack()

etiqueta = tk.Label(ventana, text="ingresa el segundo numero")
etiqueta.pack()

entrada_seg = tk.Entry(ventana)
entrada_seg.pack()

boton = tk.Button(ventana, text="suma", command=suma)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()