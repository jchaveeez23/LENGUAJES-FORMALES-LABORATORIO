#Importando Libreria
import tkinter as tk

#Metodo para acciones de botones
def evento_boton1(text:tk.Label, texto):
    text.set(texto)
    

#Cerrar Ventana
ventana = tk.Tk()

#Dar Tamaño a la Ventana
ventana.geometry('800x600')

#Agregar Titulo a Ventana
ventana.title("Ejemplo de Lab LFP")

#Etiqueta
label1 = tk.Label(ventana, text='CARNÉ',font=("Arial Black", 18), fg="Navy Blue")
label1.place(x = 100, y = 100)

label2 = tk.Label(ventana, text='NOMBRE',font=("Arial Black", 18), fg="Navy Blue")
label2.place(x = 100, y = 200)

texto = tk.StringVar()
texto.set("ASIGNADO")
label3 = tk.Label(ventana, textvariable=texto,font=("Arial Black", 18), fg="Black")
label3.place(x = 100, y = 300)

#Botones
boton1 = tk.Button(ventana,text='Enviar',font=("Arial Black", 18), fg="Black", command= lambda: evento_boton1(texto,textbox1.get()))
boton1.place(x = 600, y = 400)

#TextBox
textbox1 = tk.StringVar()
entrada1 = tk.Entry(ventana,textvariable=textbox1,font=("Arial", 16))
entrada1.place(x = 300, y = 100)

#Mostrar ventana
ventana.mainloop()