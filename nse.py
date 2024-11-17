# Import necessary libraries
import random
import string
from tkinter import filedialog
from tkinter import Tk

# Step 1: Define helper functions for file upload and save
def upload_file():
    """Allows the user to select and upload a file via a file dialog."""
    # Open a file dialog to select a file
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a file to upload")
    print(f"File selected: {file_path}")

    # Read the selected file content
    with open(file_path, 'r') as file:
        plaintext = file.read().encode()
    
    return plaintext, file_path

# Step 2: Upload the file
plaintext, text_file_name = upload_file()

# Step 3: Simulate Kyber encryption (Mock function)
def kyber_encrypt(plaintext):
    """Simulate Kyber encryption (this is a mock function)"""
    # Simulating Kyber encryption by adding a random string to the text
    encrypted_message = plaintext + b"__encrypted_with_Kyber__"
    return encrypted_message

# Step 4: Simulate Dilithium signing (Mock function)
def dilithium_sign(message):
    """Simulate Dilithium signing (this is a mock function)"""
    # Simulating Dilithium signing by creating a random signature
    signature = ''.join(random.choices(string.ascii_letters + string.digits, k=64)).encode()
    return signature

# Step 5: Encrypt the file using Kyber
ciphertext = kyber_encrypt(plaintext)
print("Message encrypted using Kyber.")

# Step 6: Sign the encrypted message using Dilithium
signature = dilithium_sign(ciphertext)
print("Ciphertext signed using Dilithium.")

# Step 7: Save the encrypted and signed file
output_file_name = "encrypted_signed_file.txt"
with open(output_file_name, 'wb') as file:
    file.write(ciphertext + b'\n' + signature)

print(f"Encrypted and signed file saved as '{output_file_name}'")

# Step 8: Allow user to download the encrypted and signed file
# In Jupyter, you would typically move or copy the file to a known directory to download it
import shutil
import os

# Move the file to a more accessible directory if needed
destination_dir = os.path.expanduser('~')  # Example: Save to the user's home directory
shutil.move(output_file_name, os.path.join(destination_dir, output_file_name))

print(f"File has been moved to {destination_dir} for download.")
