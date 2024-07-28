import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def rocket_equation(m0, m1, ve):
    return ve * np.log(m0 / m1)

def calculate():
    try:
        m0 = float(entry_m0.get())
        m1 = float(entry_m1.get())
        ve = float(entry_ve.get())
        delta_v = rocket_equation(m0, m1, ve)
        
        label_result.config(text=f"Delta-v: {delta_v:.2f} m/s")

        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, delta_v], marker='o')
        ax.set_title('Rocket Equation Delta-v')
        ax.set_xlabel('Time')
        ax.set_ylabel('Delta-v (m/s)')

        canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        canvas.draw()
        canvas.get_tk_widget().pack()
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values")

# Create the main window
root = tk.Tk()
root.title("Rocket Equation Calculator")

# Create and place the input fields and labels
frame_inputs = tk.Frame(root)
frame_inputs.pack(padx=10, pady=10)

tk.Label(frame_inputs, text="Initial Mass (m0):").grid(row=0, column=0, sticky="e")
entry_m0 = tk.Entry(frame_inputs)
entry_m0.grid(row=0, column=1, pady=5)

tk.Label(frame_inputs, text="Final Mass (m1):").grid(row=1, column=0, sticky="e")
entry_m1 = tk.Entry(frame_inputs)
entry_m1.grid(row=1, column=1, pady=5)

tk.Label(frame_inputs, text="Exhaust Velocity (ve):").grid(row=2, column=0, sticky="e")
entry_ve = tk.Entry(frame_inputs)
entry_ve.grid(row=2, column=1, pady=5)

# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=10)

# Create and place the result label
label_result = tk.Label(root, text="Delta-v: ")
label_result.pack(pady=5)

# Create a frame to hold the graph
frame_graph = tk.Frame(root)
frame_graph.pack(padx=10, pady=10)

# Run the application
root.mainloop()
