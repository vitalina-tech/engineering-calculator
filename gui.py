import tkinter as tk
from conversions import convert
from config import UNITS, COLORS, WINDOW_SIZE

def create_gui():
    window = tk.Tk()
    window.title("Unit Converter")
    window.geometry("500x400")
    window.config(bg=COLORS['background'])

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

    title_label = tk.Label(window, 
                        text="Length Unit Converter", 
                        font=('Arial', 16, 'bold'),
                        bg=COLORS['background'], fg='white')
    title_label.pack(pady=20)

    tk.Label(window, text="Enter value:", bg=COLORS['background'], fg='white').pack()
    value_entry = tk.Entry(window, width=20, font=('Arial', 12))
    value_entry.pack(pady=5)

    tk.Label(window, text="From:", bg=COLORS['background'], fg='white').pack(pady=(10,0))
    from_var = tk.StringVar(value='m')
    from_frame = tk.Frame(window, bg=COLORS['background'])
    from_frame.pack(pady=5)

    units = UNITS

    for unit in units:
        tk.Radiobutton(from_frame, text=unit, variable=from_var, value=unit, 
                    bg=COLORS['background'], fg='white', selectcolor=COLORS['background']).pack(side='left', padx=5)

    tk.Label(window, text="To:", bg=COLORS['background'], fg='white').pack(pady=(10,0))
    to_var = tk.StringVar(value='m')
    to_frame = tk.Frame(window, bg=COLORS['background'])
    to_frame.pack(pady=5)

    for unit in units:
        tk.Radiobutton(to_frame, text=unit, variable=to_var, value=unit, 
                    bg=COLORS['background'], fg='white', selectcolor=COLORS['background']).pack(side='left', padx=5)


    value_entry.bind('<Return>', lambda event: convert_units())

    convert_button = tk.Button(window, 
                            text="Convert", 
                            font=('Arial', 12, 'normal'),
                            bg=COLORS['button'],
                            command=convert_units)
    convert_button.pack(pady=20)

    result_label = tk.Label(window, 
                        text="Enter value and click Convert",
                        font=('Arial', 12),
                        bg=COLORS['background'], fg='white')
    result_label.pack(pady=10)

    window.mainloop()