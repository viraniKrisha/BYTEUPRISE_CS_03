import tkinter as tk
from tkinter import ttk

# Define encryption and decryption functions
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Function to handle encryption button click
def handle_encrypt():
    shift = int(shift_var.get())
    plaintext = input_text.get("1.0", tk.END).strip()
    encrypted_text = encrypt(plaintext, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

# Function to handle decryption button click
def handle_decrypt():
    shift = int(shift_var.get())
    ciphertext = input_text.get("1.0", tk.END).strip()
    decrypted_text = decrypt(ciphertext, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

# Create the main window
root = tk.Tk()
root.title("Encryption and Decryption")

# Set the size and center the window
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Create a frame for input and output text
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create and grid the widgets
ttk.Label(frame, text="Shift:").grid(row=0, column=0, sticky=tk.W)
shift_var = tk.StringVar(value="3")
shift_entry = ttk.Entry(frame, textvariable=shift_var, width=5)
shift_entry.grid(row=0, column=1, sticky=tk.W)

ttk.Label(frame, text="Input Text:").grid(row=1, column=0, sticky=tk.W)
input_text = tk.Text(frame, height=5, width=40)
input_text.grid(row=2, column=0, columnspan=2, pady=5)

ttk.Label(frame, text="Output Text:").grid(row=3, column=0, sticky=tk.W)
output_text = tk.Text(frame, height=5, width=40)
output_text.grid(row=4, column=0, columnspan=2, pady=5)

encrypt_button = ttk.Button(frame, text="Encrypt", command=handle_encrypt)
encrypt_button.grid(row=5, column=0, pady=10)

decrypt_button = ttk.Button(frame, text="Decrypt", command=handle_decrypt)
decrypt_button.grid(row=5, column=1, pady=10)

# Run the main loop
root.mainloop()
