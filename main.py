import tkinter as tk
from tkinter import messagebox

class Calificacion:
    def __init__(self, calificacion_numerica: float):
        self.calificacion_numerica = calificacion_numerica

    def convertir_a_literal(self) -> str:
        if 90 <= self.calificacion_numerica <= 100:
            return "A"
        elif 80 <= self.calificacion_numerica < 90:
            return "B"
        elif 70 <= self.calificacion_numerica < 80:
            return "C"
        elif 60 <= self.calificacion_numerica < 70:
            return "D"
        elif 0 <= self.calificacion_numerica < 60:
            return "F"
        else:
            return "Calificación inválida"

# Función para manejar la lógica de la interfaz
def convertir_calificacion():
    try:
        calificacion_numerica = float(entry_calificacion_numerica.get())
        calificacion = Calificacion(calificacion_numerica)
        calificacion_literal = calificacion.convertir_a_literal()
        label_resultado.config(text=f"Calificación literal: {calificacion_literal}")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingrese un valor numérico válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Conversor de Calificaciones")

# Crear y colocar los widgets
label_calificacion_numerica = tk.Label(root, text="Calificación numérica:")
label_calificacion_numerica.grid(row=0, column=0, padx=10, pady=10)

entry_calificacion_numerica = tk.Entry(root)
entry_calificacion_numerica.grid(row=0, column=1, padx=10, pady=10)

button_convertir = tk.Button(root, text="Convertir", command=convertir_calificacion)
button_convertir.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

label_resultado = tk.Label(root, text="Calificación literal: ")
label_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()

