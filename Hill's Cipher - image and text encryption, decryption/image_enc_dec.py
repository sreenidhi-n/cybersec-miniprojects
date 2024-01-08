from PIL import Image
import numpy as np

''' 
What is padding and why do we need it?
Ans: Padding refers to the addition of non-important or non-informative characters to a given string.
There could be situations where in the key matrix taken can turn out to be singular (i.e. determinant is 0)
This could arise as a result of the following: 
- The key matrix taken isn't a square matrix (Hill Cipher requires the key matrix to be a non-singular square matrix)
- Key matrix turns out to be non-invertible
- Key matrix is poorly chosen and has repeating values or the key matrix is not randomly generated. 

Sometimes as a result of a poorly chosen key matrix, the matrices generated could be of different dimensions thus rendering them impossible to
multiply in accordance with the rules of encryption. Using a function to pad ensures that if the message length is not divisible by the size
of the key matrix, the message can be padded to make the length a multiple of the key matrix size. 

'''
def hill_cipher_encrypt(matrix, key):
    key = np.array(key).reshape((3, 3))     # Convert the key to a numpy array
    # Pad the matrix with zeros if necessary to make its dimensions multiples of 3
    padded_matrix = np.pad(matrix, ((0, 3 - matrix.shape[0] % 3), (0, 3 - matrix.shape[1] % 3)), mode='constant') 
    reshaped_matrix = padded_matrix.reshape((-1, 3)) # Reshape the padded matrix to have dimensions that are multiples of 3
    encrypted_matrix = np.dot(reshaped_matrix, key) % 256 #Multiply with Key
    encrypted_matrix = encrypted_matrix.reshape(padded_matrix.shape) # Reshape the encrypted matrix back to the original shape of the padded matrix
    encrypted_matrix = encrypted_matrix[:matrix.shape[0], :matrix.shape[1]] # Remove any padding that was added 
    return encrypted_matrix.astype(np.uint8)

def hill_cipher_decrypt(matrix, key):
    key = np.array(key).reshape((3, 3)) # Convert the key to a numpy array
    inverted_key = np.linalg.inv(key) # inverting the key
    # Pad the matrix with zeros if necessary to make its dimensions multiples of 3
    padded_matrix = np.pad(matrix, ((0, 3 - matrix.shape[0] % 3), (0, 3 - matrix.shape[1] % 3)), mode='constant') 
    reshaped_matrix = padded_matrix.reshape((-1, 3)) # Reshaping the padded matrix
    decrypted_matrix = np.dot(reshaped_matrix, inverted_key) % 256 # Multiply with key
    decrypted_matrix = decrypted_matrix.reshape(padded_matrix.shape) # Reshape the decrypted matrix back to the original shape of the padded matrix
    decrypted_matrix = decrypted_matrix[:matrix.shape[0], :matrix.shape[1]] # Remove any padding that was added
    return decrypted_matrix.astype(np.uint8)

# Load the image and convert it to a numpy array
image = Image.open('demo_2.jpg') 
image_matrix = np.array(image)

# Extracting data from each of the R,G,B colour channels
r_channel = image_matrix[:, :, 0]
g_channel = image_matrix[:, :, 1]
b_channel = image_matrix[:, :, 2]

key = [1, 2, 1, 2, 3, 2, 2, 2, 1] # 3x3 encryption key as colour scheme is RGB

# Encrypting each colour channel
encrypted_r_channel = hill_cipher_encrypt(r_channel, key)
encrypted_g_channel = hill_cipher_encrypt(g_channel, key)
encrypted_b_channel = hill_cipher_encrypt(b_channel, key)

# Merge the encrypted channels into an image matrix and convert the image matrix to an image object and save
encrypted_image_matrix = np.dstack((encrypted_r_channel, encrypted_g_channel, encrypted_b_channel))
encrypted_image = Image.fromarray(encrypted_image_matrix)
encrypted_image.save('encrypted_image.jpg')

#Decrypt the encrypted colour channels using the Hill Cipher
decrypted_r_channel = hill_cipher_decrypt(encrypted_r_channel, key)
decrypted_g_channel = hill_cipher_decrypt(encrypted_g_channel, key)
decrypted_b_channel = hill_cipher_decrypt(encrypted_b_channel, key)

#Merge the decrypted RGB channels back into an image matrix and convert the decrypted matrix to an image and save.
decrypted_image_matrix = np.dstack((decrypted_r_channel, decrypted_g_channel, decrypted_b_channel))
decrypted_image = Image.fromarray(decrypted_image_matrix)
decrypted_image.save('decrypted_image.jpg')