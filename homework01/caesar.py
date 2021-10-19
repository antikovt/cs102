import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    en_process = list(map(ord, plaintext))
    ciphered = []
    for i in range(len(en_process)):
        if 65 <= en_process[i] <= 90:
            en_process[i] += shift
            while en_process[i] > 90:
                en_process[i] -= 26
        elif 97 <= en_process[i] <= 122:
            en_process[i] += shift
            while en_process[i] > 122:
                en_process[i] -= 26
        ciphered.append(chr(en_process[i]))
    line = ""
    ciphertext = line.join(ciphered)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    de_process = list(map(ord, ciphertext))
    deciphered = []
    for i in range(len(de_process)):
        if 65 <= de_process[i] <= 90:
            de_process[i] -= shift
            while de_process[i] < 65:
                de_process[i] += 26
        elif 97 <= de_process[i] <= 122:
            de_process[i] -= shift
            while de_process[i] < 97:
                de_process[i] += 26
        deciphered.append(chr(de_process[i]))
    line = ""
    plaintext = line.join(deciphered)
    return plaintext
