from PIL import Image
import numpy as np # type: ignore

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Generate a key array of the same shape as the image
    key_array = np.full_like(img_array, key, dtype=np.uint8)

    # Encrypt the image using XOR
    encrypted_array = np.bitwise_xor(img_array, key_array)

    # Convert the array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save('encrypted_image.png')
    print("Encryption complete. Encrypted image saved as 'encrypted_image.png'.")

def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Generate a key array of the same shape as the image
    key_array = np.full_like(img_array, key, dtype=np.uint8)

    # Decrypt the image using XOR
    decrypted_array = np.bitwise_xor(img_array, key_array)

    # Convert the array back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save('decrypted_image.png')
    print("Decryption complete. Decrypted image saved as 'decrypted_image.png'.")

def main():
    action = input("Do you want to encrypt or decrypt an image? (e/d): ").strip().lower()
    image_path = input("Enter the path to the image: ").strip()
    key = int(input("Enter a numeric key for encryption/decryption (0-255): ").strip())

    if action == 'e':
        encrypt_image(image_path, key)
    elif action == 'd':
        decrypt_image(image_path, key)
    else:
        print("Invalid action. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()

