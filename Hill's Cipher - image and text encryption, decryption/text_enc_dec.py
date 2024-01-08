import numpy as np
from numpy.linalg import inv

'''
Key matrix must be invertible, non-singular square matrix
Randomly generated key matrices aren't always beneficial, given that losing the key may mean not being able to decrypt the encrypted image
but since we are implementing both encryption and decryption in the same code, in this case it is feasible.
'''
def generate_key_matrix(key_text, n):
    key_matrix = np.zeros((n,n), dtype=int)
    index = 0
    for i in range(n):
        for j in range(n):
            key_matrix[i][j] = ord(key_text[index]) % 65
            index += 1
    print("Key matrix: \n",key_matrix)
    return key_matrix

'''
For a matrix A, it's modular inverse may be defined as:
(A*A^-1)mod C = 1
'''
def mod_mat_inv(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    adj_matrix = det_inv * np.round(det * inv(matrix)).astype(int)
    return adj_matrix % modulus

def encrypt_text(plaintext, key_matrix):
    plaintext = plaintext.upper() # Convert to uppercase - not necessary only for style points.
    n = key_matrix.shape[0] # length of the key matrix
    # Padding to match dimensions
    if len(plaintext) % n != 0:
        plaintext += 'X' * (n - len(plaintext) % n)
    num_blocks = len(plaintext) // n # Calculating number of blocks
    encrypted_text = np.zeros(num_blocks*n, dtype=int) # Array to store encrypted text
    # Loop where each BLOCK is encrypted.
    for i in range(num_blocks):
        block = np.array([ord(char) % 65 for char in plaintext[i*n:(i+1)*n]])
        encrypted_block = np.dot(key_matrix, block) % 26
        encrypted_text[i*n:(i+1)*n] = encrypted_block
    print("Encrypted text (matrix form): ", encrypted_text)
    encrypted_text = ''.join([chr(num+65) for num in encrypted_text]) # encrypted text to string.
    return encrypted_text

def decrypt_text(ciphertext, key_matrix):
    ciphertext = ciphertext.upper()
    n = key_matrix.shape[0]
    num_blocks = len(ciphertext) // n
    decrypted_text = np.zeros(num_blocks*n, dtype=int) # array to store decrypted text

    # Modular inverse of key matrix to perform the multiplication
    key_matrix_inv = mod_mat_inv(key_matrix, 26)
    print("\n\nInverse Key matrix (modulo 26):\n",key_matrix_inv)
    # Decrypting each BLOCK
    for i in range(num_blocks):
        block = np.array([ord(char) % 65 for char in ciphertext[i*n:(i+1)*n]])
        decrypted_block = np.dot(key_matrix_inv, block) % 26
        decrypted_text[i*n:(i+1)*n] = decrypted_block
    print("Decrypted text (matrix form): ", decrypted_text)
    decrypted_text = ''.join([chr(num+65) for num in decrypted_text]) # Decrypted text to string
    decrypted_text = decrypted_text.rstrip('X') # strip padded characters 
    return decrypted_text

key_text = 'GGGGGGGGG'
print("Key: ",key_text)
key_matrix = generate_key_matrix(key_text, 3)
plaintext = 'ACT'
ciphertext = encrypt_text(plaintext, key_matrix) # encrypted text
print("Encrypted text: ", ciphertext)
decrypted_text = decrypt_text(ciphertext, key_matrix) # decrypted text
print("Decrypted text: ",decrypted_text)
print("\n")  \




















