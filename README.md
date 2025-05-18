# 🔐 XOR Cipher (4-bit Encryption)

This is a simple Python script that implements a **4-bit XOR cipher** to encrypt and decrypt binary data. XOR (exclusive OR) is a common technique used in symmetric encryption systems due to its simplicity and effectiveness.

---

## 📌 Features

- Encrypts a 4-bit binary plaintext using a 4-bit binary key
- Decrypts ciphertext back to original plaintext using the same key
- Validates input to ensure only valid 4-bit binary strings are accepted
- Simple and beginner-friendly implementation

---

## 🧠 How XOR Encryption Works

The XOR operation compares each bit of the plaintext and the key:

| Bit A | Bit B | A ⊕ B |
|-------|-------|--------|
|   0   |   0   |   0    |
|   0   |   1   |   1    |
|   1   |   0   |   1    |
|   1   |   1   |   0    |

Encryption and decryption both use the XOR operation:
- `cipher = plaintext ⊕ key`
- `plaintext = cipher ⊕ key`

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.x

### ▶️ Run the Script

```bash
python xor_cipher.py
