import tkinter as tk
from tkinter import messagebox, scrolledtext

class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transitions):
        self.tape = list(tape)
        self.head_position = 0
        self.current_state = initial_state
        self.final_states = final_states
        self.transitions = transitions

    def step(self):
        current_symbol = self.tape[self.head_position]
        action = self.transitions.get((self.current_state, current_symbol))

        if action is None:
            raise Exception("Cadena no aceptada")

        new_state, new_symbol, direction = action

        # Escribir el nuevo símbolo en la cinta
        self.tape[self.head_position] = new_symbol

        # Mover el cabezal a la izquierda o derecha
        if direction == "R":
            self.head_position += 1
        elif direction == "L":
            self.head_position -= 1

        # Actualizar el estado actual
        self.current_state = new_state

    def run(self):
        while self.current_state not in self.final_states:
            self.step()

    def get_tape(self):
        return ''.join(self.tape)

# Función para ejecutar la máquina de Turing
def run_machine():
    input_string = entry.get().strip()
    
    if not input_string:
        messagebox.showerror("Error", "Por favor ingresa una cadena.")
        return
    
    tape = input_string + " "  # Añadir espacio al final para simbolizar la cinta infinita
    initial_state = "q0"
    final_states = {"q4"}
    
    transitions = {
        ("q0", "a"): ("q1", "a", "R"),
        ("q1", "a"): ("q1", "a", "R"),
        ("q1", "b"): ("q2", "b", "R"),
        ("q2", "b"): ("q3", "b", "R"),
        ("q3", "a"): ("q1", "a", "R"),
        ("q3", "b"): ("q2", "b", "R"),
        ("q3", " "): ("q4", " ", "L")  # Estado de aceptación
    }

    try:
        tm = TuringMachine(tape, initial_state, final_states, transitions)
        tm.run()
        result = "Cadena aceptada" if tm.current_state in final_states else "Cadena no aceptada"
        tape_result = tm.get_tape()
        output_text.configure(state='normal')  # Habilitar edición en el área de salida
        output_text.delete(1.0, tk.END)  # Limpiar la salida anterior
        output_text.insert(tk.INSERT, f"Resultado: {result}\n")
        output_text.insert(tk.INSERT, f"Cinta final: {tape_result}\n")
        output_text.configure(state='disabled')  # Deshabilitar edición en el área de salida
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Configurar la interfaz gráfica
root = tk.Tk()
root.title("Máquina de Turing (ab^2)^n")
root.geometry("400x300")

# Etiqueta de instrucciones
instructions = tk.Label(root, text="Ingrese una cadena en el formato (ab^2)^n:")
instructions.pack(pady=10)

# Entrada de texto
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Botón para validar la cadena
validate_button = tk.Button(root, text="Validar cadena", command=run_machine)
validate_button.pack(pady=5)

# Área de texto con scroll para mostrar la salida
output_text = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD, state='disabled')
output_text.pack(pady=10)

# Iniciar la ventana
root.mainloop()
