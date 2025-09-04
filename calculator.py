import tkinter as tk

def convert(value, from_unit, to_unit):
    conversions={'m':1, 'in':0.0254, 'ft':0.3048, 'yd':0.9144, 'mi':1609}
    if from_unit not in conversions or to_unit not in conversions:
        return None
    result=value * conversions[from_unit] / conversions[to_unit]
    return result

def convert_units():
    try:
        value=float(value_entry.get())
        from_unit=from_var.get()
        to_unit=to_var.get()
        result=convert(value, from_unit, to_unit)
        if result is not None:
            result_label.config(text = f'{value:.4f} {from_unit} = {result:.4f} {to_unit}')
        else:
            result_label.config(text="Error in conversion")
    except ValueError:
        result_label.config(text="Please enter a valid number")

window = tk.Tk()
window.title("Unit Converter")
window.geometry("500x400")
window.config(bg="#0a1c70")

title_label = tk.Label(window, 
                      text="Length Unit Converter", 
                      font=('Arial', 16, 'bold'),
                      bg="#0a1c70", fg='white')
title_label.pack(pady=20)

tk.Label(window, text="Enter value:", bg="#0a1c70", fg='white').pack()
value_entry = tk.Entry(window, width=20, font=('Arial', 12))
value_entry.pack(pady=5)

tk.Label(window, text="From:", bg="#0a1c70", fg='white').pack(pady=(10,0))
from_var = tk.StringVar(value='m')
from_frame = tk.Frame(window, bg="#0a1c70")
from_frame.pack(pady=5)

tk.Radiobutton(from_frame, text="m", variable=from_var, value='m', bg="#0a1c70", fg='white', selectcolor="#0a1c70").pack(side='left', padx=5)
tk.Radiobutton(from_frame, text="in", variable=from_var, value='in', bg="#0a1c70", fg='white', selectcolor="#0a1c70").pack(side='left', padx=5)
tk.Radiobutton(from_frame, text="ft", variable=from_var, value='ft', bg="#0a1c70", fg='white', selectcolor="#0a1c70").pack(side='left', padx=5)
tk.Radiobutton(from_frame, text="yd", variable=from_var, value='yd', bg="#0a1c70", fg='white', selectcolor="#0a1c70").pack(side='left', padx=5)
tk.Radiobutton(from_frame, text="mi", variable=from_var, value='mi', bg="#0a1c70", fg='white', selectcolor="#0a1c70").pack(side='left', padx=5)

tk.Label(window, text="To:", bg="#0a1c70", fg='white').pack(pady=(10,0))
to_var = tk.StringVar(value='m')
to_frame = tk.Frame(window, bg="#0a1c70")
to_frame.pack(pady=5)

tk.Radiobutton(to_frame, text="m", variable=to_var, value='m', bg="#0a1c70", fg='white', selectcolor="#0a1c70").pack(side='left', padx=5)
tk.Radiobutton(to_frame, text="in", variable=to_var, value='in', bg="#0a1c70", fg='white', selectcolor="#0a1c70").pack(side='left', padx=5)
tk.Radiobutton(to_frame, text="ft", variable=to_var, value='ft', bg="#0a1c70", fg='white', selectcolor="#0a1c70").pack(side='left', padx=5)
tk.Radiobutton(to_frame, text="yd", variable=to_var, value='yd', bg="#0a1c70", fg='white', selectcolor="#0a1c70").pack(side='left', padx=5)
tk.Radiobutton(to_frame, text="mi", variable=to_var, value='mi', bg="#0a1c70", fg='white', selectcolor="#0a1c70").pack(side='left', padx=5)

value_entry.bind('<Return>', lambda event: convert_units())

convert_button = tk.Button(window, 
                          text="Convert", 
                          font=('Arial', 12, 'normal'),
                          bg="#F7DD4A",
                          command=convert_units)
convert_button.pack(pady=20)

result_label = tk.Label(window, 
                       text="Enter value and click Convert",
                       font=('Arial', 12),
                       bg="#0a1c70", fg='white')
result_label.pack(pady=10)

window.mainloop()