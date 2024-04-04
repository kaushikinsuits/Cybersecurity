initial_permutation = [2, 6, 3, 1, 4, 8, 5, 7]
final_permutation = [4, 1, 3, 5, 7, 2, 8, 6]

s_boxes = {
    0: [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]],
    1: [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
}

def des_round(input_block, subkey):
    expanded_block = [input_block[i - 1] for i in [4, 1, 2, 3, 2, 3, 4, 1]]
    xored_block = [expanded_block[i] ^ subkey[i] for i in range(8)]
    
    substituted_block = []
    for i in range(0, 8, 4):
        row = int(str(xored_block[i]) + str(xored_block[i + 3]), 2)
        column = int(str(xored_block[i + 1]) + str(xored_block[i + 2]), 2)
        substituted_block.extend([int(x) for x in format(s_boxes[i // 4][row][column], '02b')])

    permuted_block = [substituted_block[i - 1] for i in [2, 4, 3, 1]]
    return permuted_block

def des_encrypt(plain_text, key):
    plain_text = [int(x) for x in plain_text]
    key = [int(x) for x in key]
    
    plain_text = [plain_text[i - 1] for i in initial_permutation]
    
    subkey = key[:8]
    
    for i in range(2):
        plain_text = des_round(plain_text, subkey)
    
    cipher_text = [plain_text[i - 1] for i in final_permutation if i <= len(plain_text)]
    
    return ''.join(map(str, cipher_text))

if __name__ == "__main__":
    plaintext = "10101010"
    key = "1010101010101010"

    ciphertext = des_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)
