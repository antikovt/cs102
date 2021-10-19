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
    encrypted = []
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[: len(plaintext)]
    key = list(map(ord, keyword))
    en_process = list(map(ord, plaintext))
    for i in range(len(en_process)):
        shift = key[i] - 97
        if 65 <= en_process[i] <= 90:
            en_process[i] += shift
            while en_process[i] > 90:
                en_process[i] -= 26
        elif 97 <= en_process[i] <= 122:
            en_process[i] += shift
            while en_process[i] > 122:
                en_process[i] -= 26
        encrypted.append(chr(en_process[i]))
    line = ""
    ciphertext = line.join(encrypted)
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
    decrypted = []
    keyword = (keyword * (len(ciphertext) // len(keyword) + 1))[: len(ciphertext)]
    key = list(map(ord, keyword))
    de_process = list(map(ord, ciphertext))
    for i in range(len(de_process)):
        shift = key[i] - 97
        if 65 <= de_process[i] <= 90:
            de_process[i] -= shift
            while de_process[i] < 65:
                de_process[i] += 26
        elif 97 <= de_process[i] <= 122:
            de_process[i] -= shift
            while de_process[i] < 97:
                de_process[i] += 26
        decrypted.append(chr(de_process[i]))
    line = ""
    plaintext = line.join(decrypted)
    return plaintext
