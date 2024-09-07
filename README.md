# PRODIGY_CS_02 Pixel Manipulation - Image Encryption & Decryption 🖼️🔐

This Python code implements a simple image encryption and decryption mechanism using the **XOR operation**. The process involves manipulating the pixel values of an image to encrypt or decrypt it based on a key. This is a fast and reversible encryption method, making it easy to securely transform and restore images. 📸

## ✨ Features

- **XOR Encryption/Decryption**: Efficient, reversible encryption method using XOR operation 🔄.
- **Customizable Key**: Allows the use of an integer key between 0 and 255 for encryption 🔑.
- **Image Compatibility**: Handles image manipulation using the `Pillow` and `NumPy` libraries.

## 🚀 How It Works

### XOR Encryption 🔒

- The encryption process uses the **XOR (exclusive OR)** operation on the pixel values of an image.
- **Reversible**: The same operation is used for both encryption and decryption. Applying XOR with the same key again will restore the original image.

### Key Constraints 🔑

- The key must be an integer between **0 and 255**, as it is used to generate a key array.
- This key array is then applied to the pixel values of the image, making it essential for both encryption and decryption.

### Image Handling 🖼️

- The code assumes the input image is in a format compatible with the **Pillow** library.
- The image is converted into a **NumPy array** for pixel manipulation.
- After encryption/decryption, the image is saved back .


## 🛠️ How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Pixel_Manipulation.git

2. Install dependencies:
    ```bash
    pip install pillow
    pip install numpy
3. Run the script:
   ```
   python3 PixelManipulation.py

🔑 Example Usage
   ```
Do you want to encrypt or decrypt an image? (e/d): e
Enter the path to the image: C:\Users\PREDATOR\Pictures\images horizon\burgershot.png
Enter a numeric key for encryption/decryption (0-255): 123
Encryption complete. Encrypted image saved as 'encrypted_image.png'.
