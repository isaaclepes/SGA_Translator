import tkinter as tk
from tkinter import font

# Create the window
root = tk.Tk()
root.title("English to SGA Translator")

# Set window parameters
window_width = 450
window_height = 175
root.geometry(f"{window_width}x{window_height}")
background_color = "#2e2e2e"
foreground_color = "#ffffff"
input_background_color = "#4d4d4d"
input_foreground_color = "#ffffff"
root.configure(bg=background_color)

# Define fonts
standard_font = ("Arial", 12)
sga_smooth_regular = ("SGA Smooth Regular", 12)

# Update preview with the input text
def update_preview(*args):
    preview_text.set(input_text.get())

# Text input
input_label = tk.Label(root, text="Translate:", font=standard_font,
                       bg=background_color, fg=foreground_color)
input_label.pack(pady=10)
input_text = tk.StringVar()
input_text.trace_add("write", update_preview)
input_entry = tk.Entry(root, textvariable=input_text, font=standard_font, width=50,
                       bg=input_background_color, fg=input_foreground_color, insertbackground=foreground_color, justify="center")
input_entry.pack(pady=10)

# SGA View
preview_text = tk.StringVar()
preview_label = tk.Label(root, text="Standard Galactic:", font=standard_font,
                         bg=background_color, fg=foreground_color)
preview_label.pack(pady=10)
preview_display = tk.Label(root, textvariable=preview_text, font=sga_smooth_regular, width=50,
                           bg=background_color, fg=foreground_color)
preview_display.pack(pady=10)


# Run mainloop
root.mainloop()
