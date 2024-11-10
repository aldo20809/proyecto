import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agencia de Autos - Menú Principal")
ventana.geometry("400x400")

# Lista para almacenar automóviles
automoviles = []

# Función para agregar un automóvil
def agregar_automovil():
    # Crear una nueva ventana para agregar un automóvil
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Automóvil")
    ventana_agregar.geometry("300x300")
    
    # Etiquetas y campos de entrada para los datos del automóvil
    tk.Label(ventana_agregar, text="Marca del automóvil:").pack()
    entrada_marca = tk.Entry(ventana_agregar)
    entrada_marca.pack(pady=5)
    
    tk.Label(ventana_agregar, text="Modelo del automóvil:").pack()
    entrada_modelo = tk.Entry(ventana_agregar)
    entrada_modelo.pack(pady=5)
    
    tk.Label(ventana_agregar, text="Año del automóvil:").pack()
    entrada_año = tk.Entry(ventana_agregar)
    entrada_año.pack(pady=5)
    
    tk.Label(ventana_agregar, text="Precio del automóvil:").pack()
    entrada_precio = tk.Entry(ventana_agregar)
    entrada_precio.pack(pady=5)
