import tkinter as tk

def count_letters(text):
    # Count the number of letters in the text
    letters = [char for char in text if char.isalpha()]
    return len(letters)

def update_count():
    input_text = text_entry.get("1.0", tk.END).strip()
    letter_count = count_letters(input_text)
    result_label.config(text=f"Letter count: {letter_count}")

def clear_text():
    text_entry.delete("1.0", tk.END)
    result_label.config(text="Letter count: 0")

def exit_program():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Text Counter")

label_title = tk.Label(window, text="Letter Counter", fg='white', bg='#154360', font=('Helvetica', 15))
label_title.pack()

text_entry = tk.Text(window, height=10, width=50, bg="#76D7C4")
text_entry.pack(pady=10)

#count button
count_button = tk.Button(window, text="Count Letters", command=update_count, fg='white', bg="#2874A6")
count_button.pack()

result_label = tk.Label(window, text="Letter count: 0", height=2, width=15, fg='white', bg="#21618C")
result_label.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(side="bottom", pady=15)

#clear button
clear_button = tk.Button(button_frame, text="Clear", height=1, width=5, command=clear_text, fg='white', bg="#1D8348")
clear_button.pack(side="left", padx=5)

#exit button
exit_button = tk.Button(button_frame, text="Exit", height=1, width=5, command=exit_program, fg='white', bg="#C0392B")
exit_button.pack(side="left", padx=5)

# Start the Tkinter event loop
window.mainloop()
