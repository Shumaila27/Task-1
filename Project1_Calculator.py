import tkinter as tk  # The tkinter library in Python is used to create GUIs.

calculation = ""  # An empty string for calculations

# Function to add symbols to the calculation
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")  # Clear the display area
    text_result.insert(1.0, calculation)  # Display the updated calculation

# Function to evaluate the calculation
def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))  # Evaluate the calculation and convert to string
        calculation = ""  # Clear the calculation after evaluating
        text_result.delete(1.0, "end")  # Clear the display area
        text_result.insert(1.0, result)  # Display the result
    except:
        clear_field()  # Call clear_field to reset the display
        text_result.insert(1.0, "Error")  # Display an error message

# Function to clear the calculation
def clear_field():
    global calculation
    calculation = ""  # Reset the calculation string
    text_result.delete(1.0, "end")  # Clear the display area

# Create the main window
root = tk.Tk()
root.title("My first Calculator")
root.geometry("365x420")  # Set window size
root.configure(bg="#2d2d2d")  #  dark background color

# Display area for the result
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), bg="#444444", fg="#ffffff", bd=0, padx=10, pady=10)
text_result.grid(row=0, column=0, columnspan=5, padx=10, pady=20)
# Button styling
button_bg = "#666666"  # Button background color
button_fg = "#ffffff"  # Button text color
button_font = ("Arial", 18)

# Number buttons
btn_1 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_1.grid(row=2, column=1, padx=5, pady=5)
btn_2 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_2.grid(row=2, column=2, padx=5, pady=5)
btn_3 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_3.grid(row=2, column=3, padx=5, pady=5)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_4.grid(row=3, column=1, padx=5, pady=5)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_5.grid(row=3, column=2, padx=5, pady=5)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_6.grid(row=3, column=3, padx=5, pady=5)
btn_7 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_7.grid(row=4, column=1, padx=5, pady=5)
btn_8 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_8.grid(row=4, column=2, padx=5, pady=5)
btn_9 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_9.grid(row=4, column=3, padx=5, pady=5)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_0.grid(row=5, column=2, padx=5, pady=5)

# Operation buttons
btn_Div = tk.Button(root, text="÷", command=lambda: add_to_calculation("/"), width=5, font=button_font, bg="#ff6600", fg=button_fg)
btn_Div.grid(row=2, column=4, padx=5, pady=5)
btn_Mul = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=5, font=button_font, bg="#ff6600", fg=button_fg)
btn_Mul.grid(row=3, column=4, padx=5, pady=5)
btn_Add = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=button_font, bg="#ff6600", fg=button_fg)
btn_Add.grid(row=4, column=4, padx=5, pady=5)
btn_Min = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=button_font, bg="#ff6600", fg=button_fg)
btn_Min.grid(row=5, column=4, padx=5, pady=5)

# Additional buttons
btn_Open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_Open.grid(row=5, column=1, padx=5, pady=5)
btn_Close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=button_font, bg=button_bg, fg=button_fg)
btn_Close.grid(row=5, column=3, padx=5, pady=5)
btn_Equal = tk.Button(root, text="=", command=evaluate_calculation, width=10, font=button_font, bg="#00cc66", fg=button_fg)
btn_Equal.grid(row=6, column=3, columnspan=2, padx=5, pady=5)
btn_Clear = tk.Button(root, text="C", command=clear_field, width=10, font=button_font, bg="#cc0000", fg=button_fg)
btn_Clear.grid(row=6, column=1, columnspan=2, padx=5, pady=5)

# Start the application
root.mainloop()
