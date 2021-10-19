def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    keyword = keyword.lower()
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[: len(plaintext)]
    keyword = list(map(ord, keyword))
    plaintext = list(map(ord, plaintext))
    for i in range(len(plaintext)):
        shift = keyword[i] - 97
        if 65 <= plaintext[i] <= 90:
            plaintext[i] += shift
            while plaintext[i] > 90:
                plaintext[i] -= 26
        elif 97 <= plaintext[i] <= 122:
            plaintext[i] += shift
            while plaintext[i] > 122:
                plaintext[i] -= 26
        plaintext[i] = chr(plaintext[i])
    line = ""
    ciphertext = line.join(plaintext)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    keyword = keyword.lower()
    keyword = (keyword * (len(ciphertext) // len(keyword) + 1))[: len(ciphertext)]
    keyword = list(map(ord, keyword))
    ciphertext = list(map(ord, ciphertext))
    for i in range(len(ciphertext)):
        shift = keyword[i] - 97
        if 65 <= ciphertext[i] <= 90:
            ciphertext[i] -= shift
            while ciphertext[i] < 65:
                ciphertext[i] += 26
        elif 97 <= ciphertext[i] <= 122:
            ciphertext[i] -= shift
            while ciphertext[i] < 97:
                ciphertext[i] += 26
        ciphertext[i] = chr(ciphertext[i])
    line = ""
    plaintext = line.join(ciphertext)
    return plaintext
