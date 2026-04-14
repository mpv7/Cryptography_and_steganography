import numpy as np 
import string

plaintext = input("введите открытый текст: \n")
if len(plaintext) % 2 != 0:
    plaintext += ' '

encrypted_text = input("Введите шифртекст: \n")

char_to_index = {char: i for i, char in enumerate(string.printable[10:36])}
char_to_index[' '] = 26
index_to_char = {i: char for i, char in enumerate(string.printable[10:36])}
index_to_char[26] = ' '

crypted_chars = []
crypted_bloks = []
for x in plaintext:
    crypted_chars.append(char_to_index[x])
    if len(crypted_chars) == 2:
        block_array = np.array(crypted_chars).reshape(1, 2)
        crypted_bloks.append(block_array)
        crypted_chars = []

encrypted_chars = []
encrypted_bloks = []
for x in encrypted_text:
    encrypted_chars.append(char_to_index[x])
    if len(encrypted_chars) == 2:
        block_array = np.array(encrypted_chars).reshape(1, 2)
        encrypted_bloks.append(block_array)
        encrypted_chars = []

print("Блоки открытого текста:", crypted_bloks)
print("Блоки шифртекста:", encrypted_bloks)

key = np.zeros((2, 2), dtype=int)
found = False

for i in range(27):
    for j in range(27):
        for k in range(27):
            for r in range(27):
                key[0][0], key[0][1], key[1][0], key[1][1] = i, j, k, r
                
                # Проверяем, что ключ подходит для ВСЕХ блоков
                valid = True
                for block_idx in range(len(crypted_bloks)):
                    if ((crypted_bloks[block_idx] @ key)%27 != encrypted_bloks[block_idx]).any():
                        valid = False
                        break
                
                if valid:
                    print("Найден ключ:")
                    print(key)
                    found = True
                    break
            if found: break
        if found: break
    if found: break

if not found:
    print("Ключ не найден")