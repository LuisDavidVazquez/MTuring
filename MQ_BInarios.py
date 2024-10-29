import tkinter as tk
from tkinter import messagebox, ttk

# Función para realizar la suma binaria de dos números
def sumar_binarios(bin1, bin2):
    # Convertir binarios a enteros, realizar la suma y convertir el resultado a binario
    suma = bin(int(bin1, 2) + int(bin2, 2))[2:]
    return suma

# Función para calcular la suma final de acuerdo a la estructura indicada
def calcular_suma_acumulada():
    # Limpiar tabla antes de agregar nuevos resultados
    for row in tabla.get_children():
        tabla.delete(row)

    # Obtener los primeros dos binarios y los binarios adicionales como secuencia
    bin1 = entry_binario1.get()
    bin2 = entry_binario2.get()
    binarios_adicionales = entry_lista_binarios.get()

    # Validar que los primeros dos binarios estén presentes
    if not bin1 or not bin2:
        messagebox.showerror("Error", "Ingresa los primeros dos números binarios.")
        return

    # Concatenar el primer y segundo binario, y sumar el número adicional completo
    input_completo = f"{bin1}{bin2}+{binarios_adicionales}"
    resultado = sumar_binarios(f"{bin1}{bin2}", binarios_adicionales)

    # Insertar el input completo y el resultado en la tabla en el formato solicitado
    tabla.insert("", "end", values=(input_completo, resultado))

    # Mostrar mensaje de éxito
    messagebox.showinfo("Resultados", "La suma final se ha calculado exitosamente.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Máquina de Turing para Suma Acumulativa de Números Binarios")
root.geometry("600x400")

# Etiquetas y entradas para los primeros dos números binarios
label_binario1 = tk.Label(root, text="Primer binario:")
label_binario1.pack(pady=5)
entry_binario1 = tk.Entry(root, width=10)
entry_binario1.pack(pady=5)

label_binario2 = tk.Label(root, text="Segundo binario:")
label_binario2.pack(pady=5)
entry_binario2 = tk.Entry(root, width=10)
entry_binario2.pack(pady=5)

# Etiqueta y entrada para la lista de binarios adicionales en secuencia
label_lista_binarios = tk.Label(root, text="Números binarios adicionales (sin comas ni espacios):")
label_lista_binarios.pack(pady=5)
entry_lista_binarios = tk.Entry(root, width=25)
entry_lista_binarios.pack(pady=5)

# Botón para realizar el cálculo
btn_calcular = tk.Button(root, text="Calcular Suma Acumulativa", command=calcular_suma_acumulada)
btn_calcular.pack(pady=10)

# Tabla para mostrar los resultados con el input completo y la suma acumulativa
tabla = ttk.Treeview(root, columns=("Input", "Suma Acumulada"), show="headings", height=10)
tabla.heading("Input", text="Input")
tabla.heading("Suma Acumulada", text="Suma Acumulada")
tabla.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
