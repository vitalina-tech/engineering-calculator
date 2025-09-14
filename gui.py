import tkinter as tk
from tkinter import ttk
from conversions import convert
from config import CONVERSIONS, COLORS, WINDOW_SIZE
import datetime
from log import LOG
from navigation import haversine_distance

def create_conversion_tab(notebook, conversion_type, data):
    tab_frame = tk.Frame(notebook, bg=COLORS['background'])
    notebook.add(tab_frame, text=conversion_type)
    
    title_label = tk.Label(tab_frame, 
                          text=f"{conversion_type} Unit Converter", 
                          font=('Arial', 16, 'bold'),
                          bg=COLORS['background'], fg=COLORS['text'])
    title_label.pack(pady=20)

    tk.Label(tab_frame, text="Enter value:", bg=COLORS['background'], fg=COLORS['text']).pack()
    value_entry = tk.Entry(tab_frame, width=20, font=('Arial', 12))
    value_entry.pack(pady=5)

    conversion_frame = tk.Frame(tab_frame, bg=COLORS['background'])
    conversion_frame.pack(pady=10)

    from_frame = tk.Frame(conversion_frame, bg=COLORS['background'])
    from_frame.pack(side='left', padx=20)
    
    tk.Label(from_frame, text="From:", bg=COLORS['background'], fg=COLORS['text']).pack()
    from_var = tk.StringVar(value=data['units'][0])
    from_combo = ttk.Combobox(from_frame, textvariable=from_var, values=data['units'], state="readonly")
    from_combo.pack(pady=5)
    from_combo.bind('<<ComboboxSelected>>', lambda event: convert_units())

    to_frame = tk.Frame(conversion_frame, bg=COLORS['background'])
    to_frame.pack(side='left', padx=20)
    
    tk.Label(to_frame, text="To:", bg=COLORS['background'], fg=COLORS['text']).pack()
    to_var = tk.StringVar(value=data['units'][0])
    to_combo = ttk.Combobox(to_frame, textvariable=to_var, values=data['units'], state="readonly")
    to_combo.pack(pady=5)
    to_combo.bind('<<ComboboxSelected>>', lambda event: convert_units())



    def convert_units():
        try:
            value = float(value_entry.get())
            from_unit = from_var.get()
            to_unit = to_var.get()
            result = convert(value, from_unit, to_unit, conversion_type)
            if result is not None:
                result_label.config(text=f'{value:.4f} {from_unit} = {result:.4f} {to_unit}')

            else:
                result_label.config(text="Error in conversion")
        except ValueError:
            result_label.config(text="Please enter a valid number")
    
    def save_data():
        try:
            value = float(value_entry.get())
            from_unit = from_var.get()
            to_unit = to_var.get()
            result = convert(value, from_unit, to_unit, conversion_type)
            
            if result is not None:
                record = {
                    'timestamp': datetime.datetime.now(),
                    'category': conversion_type,
                    'value': value,
                    'from_unit': from_unit,
                    'to_unit': to_unit,
                    'result': result
                }
                LOG.append(record)
                print(f"Saved: {len(LOG)} records")
            else:
                print("Cannot save - conversion error")
        except ValueError:
            print("Cannot save - invalid input")

    value_entry.bind('<KeyRelease>', lambda event: convert_units())

    result_label = tk.Label(tab_frame, 
                           text="Enter value",
                           font=('Arial', 12),
                           bg=COLORS['background'], fg=COLORS['text'])
    result_label.pack(pady=10)

    save_button = tk.Button(tab_frame, 
                            text="Save", 
                            font=('Arial', 12, 'normal'),
                            bg=COLORS['button'],
                            fg=COLORS['button_text'],
                            command=lambda: save_data())
    save_button.pack(pady=20)

def distance_tab(notebook):
    distance_frame = tk.Frame(notebook, bg=COLORS['background'])
    notebook.add(distance_frame, text='Distance')

    title_label = tk.Label(distance_frame, 
                          text="Distance calculation", 
                          font=('Arial', 16, 'bold'),
                          bg=COLORS['background'], fg=COLORS['text'])
    title_label.pack(pady=20)

    coordinates_frame = tk.Frame(distance_frame, bg=COLORS['background'])
    coordinates_frame.pack(pady=10)

    first_point_frame = tk.Frame(coordinates_frame, bg=COLORS['background'])
    first_point_frame.pack(side='left', padx=20)

    tk.Label(first_point_frame, text="First Point", bg=COLORS['background'], fg=COLORS['text'], font=('Arial', 12, 'bold')).pack()

    tk.Label(first_point_frame, text="Enter latitudes:", bg=COLORS['background'], fg=COLORS['text']).pack()
    lat1_entry = tk.Entry(first_point_frame, width=20, font=('Arial', 12))
    lat1_entry.pack(pady=5)

    tk.Label(first_point_frame, text="Enter  longitudes:", bg=COLORS['background'], fg=COLORS['text']).pack()
    lon1_entry = tk.Entry(first_point_frame, width=20, font=('Arial', 12))
    lon1_entry.pack(pady=5)

    second_point_frame = tk.Frame(coordinates_frame, bg=COLORS['background'])
    second_point_frame.pack(side='left', padx=20)

    tk.Label(second_point_frame, text="Second Point", bg=COLORS['background'], fg=COLORS['text'], font=('Arial', 12, 'bold')).pack()

    tk.Label(second_point_frame, text="Enter latitudes:", bg=COLORS['background'], fg=COLORS['text']).pack()
    lat2_entry = tk.Entry(second_point_frame, width=20, font=('Arial', 12))
    lat2_entry.pack(pady=5)

    tk.Label(second_point_frame, text="Enter  longitudes:", bg=COLORS['background'], fg=COLORS['text']).pack()
    lon2_entry = tk.Entry(second_point_frame, width=20, font=('Arial', 12))
    lon2_entry.pack(pady=5)

    distance_label = tk.Label(distance_frame, 
                           text="Enter values",
                           font=('Arial', 12),
                           bg=COLORS['background'], fg=COLORS['text'])
    distance_label.pack(pady=10)

    def calculate_distance():
        try:
            lat1 = float(lat1_entry.get())
            lat2 = float(lat2_entry.get())
            lon1 = float(lon1_entry.get())
            lon2 = float(lon2_entry.get())
            if -90<=lat1<=90 and -90<=lat2<=90 and -180<=lon1<=180 and -180<=lon2<=180:
                result = haversine_distance(lat1, lat2, lon1, lon2)
                distance_label.config(text=f'The distance is {result:.2f} km/{result * 0.621371:.2f} miles')
            else:
                distance_label.config(text="Latitude from -90 to +90 degrees\nLongitude from -180 to +180 degrees")
        except ValueError:
            distance_label.config(text="Please enter a valid number")

    calculate_button = tk.Button(distance_frame, 
                            text="Calculate", 
                            font=('Arial', 12, 'normal'),
                            bg=COLORS['button'],
                            fg=COLORS['button_text'],
                            command=calculate_distance)
    calculate_button.pack(pady=20)

def create_gui():
    window = tk.Tk()
    window.title("Unit Converter")
    window.geometry(WINDOW_SIZE)
    window.config(bg='#f0f0f0')

    notebook = ttk.Notebook(window)
    notebook.pack(expand=True, fill='both', padx=2, pady=2)

    for conversion_type, data in CONVERSIONS.items():
        create_conversion_tab(notebook, conversion_type, data)

    history_frame = tk.Frame(notebook, bg=COLORS['background'])
    notebook.add(history_frame, text='History')

    history_listbox=tk.Listbox(history_frame)
    history_listbox.pack(expand=True, fill='both', padx=10, pady=10)

    def update_history():
        history_listbox.delete(0, tk.END)
        for record in LOG:
            time_str = record['timestamp'].strftime("%H:%M")
            text = f"{time_str} - {record['category']}: {record['value']:.2f} {record['from_unit']} = {record['result']:.2f} {record['to_unit']}"
            history_listbox.insert(tk.END, text)

    def on_tab_changed(event):
        selected_tab = event.widget.tab('current')['text']
        if selected_tab == 'History':
            update_history()

    notebook.bind('<<NotebookTabChanged>>', on_tab_changed)

    distance_tab(notebook)

    window.mainloop()

create_gui()