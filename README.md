# 🔐 Caesar Cipher Encryption Tool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple Python-based Caesar Cipher tool that allows users to encrypt and decrypt messages via a command-line interface. This classic cipher shifts alphabetic characters by a specified number of positions while preserving non-letter characters like punctuation and spaces.

---

## 💡 Features

- Encrypt or decrypt messages
- Supports uppercase and lowercase letters
- Non-alphabet characters are left unchanged
- Simple terminal interaction (no external libraries required)

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.x installed on your system


## ▶️ Run the Script

```bash
python caesar_cipher.py
```

You'll be prompted to:

* Enter your message
* Enter a shift value (e.g., 3)
* Choose between **encrypt** or **decrypt**

---

## 🧪 Example

**Input:**

```
Enter your message: Hello, World!
Enter shift value (e.g., 3): 3
Type 'encrypt' or 'decrypt': encrypt
```

**Output:**

```
Result: Khoor, Zruog!
```

---

## 🧠 How It Works

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.
For example, with a shift of 3:

* A → D
* B → E
* ...
* X → A

Non-letter characters are not changed.

---

## 📚 References

* [Wikipedia: Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

---

## 📜 License

This project is licensed under the MIT License.
