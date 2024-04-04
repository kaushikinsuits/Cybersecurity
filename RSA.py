import random

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while mod_inverse(e, phi) == 0:
        e = random.randrange(1, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    e, n = pk
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    d, n = pk
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

if __name__ == "__main__":
    p = 61
    q = 53
    public_key, private_key = generate_keypair(p, q)
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = "Hello, World!"
    print("Original Message:", message)

    encrypted_message = encrypt(public_key, message)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted Message:", decrypted_message)
