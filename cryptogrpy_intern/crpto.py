import base64
from cryptography.fernet import Fernet
import rsa
from tkinter import *
from tkinter import messagebox

# Function to generate AES key and encrypt message
def aes_encrypt(message):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return key.decode(), encrypted_message.decode()

# Function to decrypt AES encrypted message
def aes_decrypt(key, encrypted_message):
    fernet = Fernet(key.encode())
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

# Function to generate RSA keys and encrypt message
def rsa_encrypt(message):
    public_key, private_key = rsa.newkeys(512)
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    return public_key.save_pkcs1().decode(), private_key.save_pkcs1().decode(), encrypted_message.hex()

# Function to decrypt RSA encrypted message
def rsa_decrypt(public_key_str, private_key_str, encrypted_message):
    public_key = rsa.PublicKey.load_pkcs1(public_key_str.encode())
    private_key = rsa.PrivateKey.load_pkcs1(private_key_str.encode())
    decrypted_message = rsa.decrypt(bytes.fromhex(encrypted_message), private_key).decode()
    return decrypted_message

# GUI setup
def encrypt_text():
    message = input_text.get("1.0", END).strip()
    
    if not message:
        messagebox.showerror("Error", "Please enter text to encrypt.")
        return
    
    key, encrypted_message = aes_encrypt(message)
    output_text.delete("1.0", END)
    output_text.insert(END, f"AES Key: {key}\nEncrypted Message: {encrypted_message} \n")

def decrypt_text():
    key = key_input.get().strip()
    encrypted_message = output_text.get("1.0", END).strip().split("\n")[1].split(": ")[1]
    
    try:
        decrypted_message = aes_decrypt(key, encrypted_message)
        output_text.insert(END, f"\nDecrypted Message: {decrypted_message}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main window setup
root = Tk()
root.title("SecureText Encryption")
root.geometry("700x500")  # Adjusted window size for wider input/output boxes
root.configure(bg="#f0f0f0")

# Header Label
header_label = Label(root, text="SecureText Encryption", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#4A90E2")
header_label.pack(pady=10)

# Input Frame
input_frame = Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

Label(input_frame, text="Enter Text To Encrypt/Decrypt:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=0, column=0)
input_text = Text(input_frame, height=5, width=60, font=("Helvetica", 12))  # Increased width
input_text.grid(row=1, column=0)

Button(input_frame, text="Encrypt", command=encrypt_text, bg="#4A90E2", fg="white", font=("Helvetica", 12)).grid(row=2, column=0, pady=5)
Button(input_frame, text="Decrypt", command=decrypt_text, bg="#E94E77", fg="white", font=("Helvetica", 12)).grid(row=3, column=0)

# Key Input Frame
key_frame = Frame(root, bg="#f0f0f0")
key_frame.pack(pady=10)

Label(key_frame, text="AES Key For Decryption:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=0, column=0)
key_input = Entry(key_frame, width=60, font=("Helvetica", 12))  # Increased width
key_input.grid(row=1, column=0)

# Output Frame
output_frame = Frame(root, bg="#f0f0f0")
output_frame.pack(pady=10)

Label(output_frame, text="Output", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=0, column=0)
output_text = Text(output_frame, height=10, width=60, font=("Helvetica", 12))  # Increased width
output_text.grid(row=1, column=0)

root.mainloop()
