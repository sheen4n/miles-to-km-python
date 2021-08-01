from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=40, pady=40)

# Miles Entry
miles_entry = Entry(width=10)
# Add some text to begin with
miles_entry.insert(END, string="0")
miles_entry.grid(row=0, column=1)

# Mile Label
mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

# Is Equal To Label
is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

# Value Label
km_value_label = Label(text="0")
km_value_label.grid(row=1, column=1)

# Km Label
km_label = Label(text="Km")
km_label.grid(row=1, column=2)


# Calculate Button
# Buttons
def convert_to_km():
    miles = miles_entry.get()
    km = str(round(float(miles) * 1.60934, 2))
    km_value_label.config(text=km)


button = Button(text="Calculate", command=convert_to_km)
button.grid(row=2, column=1)

window.mainloop()
