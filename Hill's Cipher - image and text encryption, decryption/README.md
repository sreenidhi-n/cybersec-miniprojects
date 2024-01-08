This mini-project was completed as instructed for a Linear Algebra course. Below is taken from my own project report.

# Hill's Cipher
Developed in 1929 by the renowned American mathematician Lester S. Hill, the Hill Cipher is a popularly used method of encryption and decryption of text and images, built on the principles of Linear Algebra.
The cipher follows a polygraphic substitution cipher – there is uniform substitution across all block and it was the first polygraphic cipher in which it was possible to operate on more than three symbol at once The Hill Cipher uses a matrix as its key and operates on blocks of plaintext. 
The plaintext is first converted to numerical values, which are then grouped into a vector. The vector is then multiplied by the matrix key modulo a number, producing a ciphertext vector. The ciphertext vector is then converted back to letters to produce the final encrypted message. The security of the Hill Cipher is based on the difficulty of factoring the matrix key into its constituent parts. The larger the size of the matrix key, the more secure the cipher becomes. (source: wikipedia)

## Text Encryption 
One special feature of the Hill Cipher is that it is based entirely on the concepts of Linear Algebra thus it can be extended to blocks of any size. What does the process normally look like? 
1. **Key Generation**: The encryption key is a square matrix of size n x n, where n is the block size. The matrix must be invertible, meaning that it has a multiplicative inverse modulo a chosen modulus (usually 26 for the English alphabet). 
2. **Plaintext Conversion**: The plaintext message is converted to a numerical sequence. Each letter is assigned a numerical value based on its position in the alphabet (e.g., A=0, B=1, C=2, ..., Z=25). 
3. **Message Padding**: If the length of the plaintext message is not a multiple of n, the message is padded with dummy characters (e.g., X) until it reaches a multiple of n. 
4. **Block Processing**: The padded message is then divided into blocks of size n. Each block is represented as a column vector of size n x 1. 
5. **Matrix Multiplication**: Each column vector is multiplied by the encryption key matrix modulo the chosen modulus (e.g., 26). The resulting product is another column vector of size n x 1. 
6. **Ciphertext Conversion**: The resulting column vector is then converted back to a sequence of numerical values (i.e., ciphertext).
7. **Ciphertext Output**: The ciphertext values are then converted back to their corresponding letters using the same alphabetical mapping used in step 2. 

The resulting ciphertext is a sequence of characters that can be transmitted securely over an insecure channel. To decrypt the message, the recipient must have the same encryption key used by the sender and perform the inverse operation on each block of ciphertext.

## Text Decryption
Decryption in Hill Cipher involves the following steps: 
1. **Key Generation**: The decryption key is the inverse of the encryption key matrix modulo the chosen modulus (usually 26 for the English alphabet). 
2. **Ciphertext Conversion**: The ciphertext message is converted to a numerical sequence using the same alphabetical mapping used in encryption. 
3. **Block Processing**: The ciphertext message is divided into blocks of size n. Each block is represented as a column vector of size n x 1. 
4. **Matrix Multiplication**: Each column vector is multiplied by the decryption key matrix modulo the chosen modulus. The resulting product is another column vector of size n x 1. 
5. **Plaintext Conversion**: The resulting column vector is then converted back to a sequence of numerical values. 
6. **Plaintext Output**: The plaintext values are then converted back to their corresponding letters using the same alphabetical mapping used in encryption.

## Image Encryption
1. **Choose a key matrix**: The first step in encrypting an image using the Hill Cipher is to choose a key matrix. The key matrix should be an n x n matrix of integers, where n is the size of the blocks you want to encrypt. 
2. **Convert the image into numerical values**: To encrypt an image, you first need to convert it into numerical values. You can do this by representing each pixel in the image as a number between 0 and 255. For example, a black pixel might be represented as 0, while a white pixel might be represented as 255. 
3. **Divide the image into blocks**: Next, you need to divide the image into blocks of n x n pixels. Each block should be represented as a column vector of length n^2^ . 
4. **Multiply the block by the key matrix**: To encrypt each block, you need to multiply it by the key matrix modulo the size of the alphabet. The result of this multiplication will be a new column vector of length n^2^. 
5. **Convert the encrypted block back into image format**: Finally, you need to convert the encrypted block back into image format. To do this, you need to reshape the column vector into an n x n matrix and replace the original pixels in the image with the encrypted pixels. 
6. **Repeat for all blocks**: Repeat steps 3-5 for all blocks in the image. 
7. **Save the encrypted image**: Once you have encrypted all the blocks in the image, you can save the encrypted image as a new file.

## Image Decryption
1. **Choose the key matrix**: To decrypt an image encrypted using the Hill Cipher, you need to know the key matrix used for encryption. 
2. **Calculate the inverse of the key matrix**: Next, you need to calculate the inverse of the key matrix modulo the size of the alphabet. The size of the alphabet will depend on the number of possible pixel values in the image. For example, if you are working with an image that has 256 possible pixel values, then the size of the alphabet would be 256. If the key matrix is not invertible, then decryption is not possible. 
3. **Convert the image into numerical values**: Just like with encryption, you need to convert the encrypted image into numerical values. 
4. **Divide the image into blocks**: Divide the image into blocks of n x n pixels. 
5. **Multiply the block by the inverse of the key matrix**: To decrypt each block, you need to multiply it by the inverse of the key matrix modulo the size of the alphabet. The result of this multiplication will be a new column vector of length n^2^. 
6. **Convert the decrypted block back into image format**: Finally, you need to convert the decrypted block back into image format. To do this, you need to reshape the column vector into an n x n matrix and replace the encrypted pixels in the image with the decrypted pixels. 
7. **Repeat for all blocks**: Repeat steps 4-6 for all blocks in the image. 
8. **Save the decrypted image**: Once you have decrypted all the blocks in the image, you can save the decrypted image as a new file

References:
[1] N. Vijayaraghavan, S. Narasimhan, and M. Baskar, "A Study on the Analysis of Hill's Cipher in Cryptography," International Journal of Mathematics Trends and Technology (IJMTT), vol. 54, no. 7, pp. 519-524, Feb. 2018. ISSN: 2231-5373. 
[2] M. D. L. Siahaan and A. P. U. Siahaan, "Application of Hill Cipher Algorithm in Securing Text Messages," International Journal for Innovative Research in Multidisciplinary Field (IJIRMF), vol. 4, no. 10, pp. 55-59, Oct. 2018. ISSN: 2455-0620
