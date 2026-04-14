import string


def cipher_Vigenere():
    operation = input(
        "Введите какую операцию хотите провести, где 0 - шифрование, а 1 - расшифрование: \n")
    type_of_encoding = input(
        "Введите вид гамирования, где 0 - Повторение короткого лозунга, 1 - Самоключ Виженера по открытому тексту, 2 - Самоключ Виженера по шифр: \n")
    char_to_index = {char: index for index,
                     char in enumerate(string.printable[10:36])}
    char_to_index[' '] = 26
    index_to_char = {index: char for index,
                     char in enumerate(string.printable[10:36])}
    index_to_char[26] = ' '

    if operation == '0':

        if type_of_encoding == '0':
            word = input("Введите коротную фразу: \n")
            gamma = word
            plaintext = input("Введите исходный текст: \n")
            i = 0

            while len(gamma) != len(plaintext):
                gamma += word[i % len(word)]
                i += 1

            ciphertext = []
            for i in range(len(plaintext)):
                ciphertext.append(
                    index_to_char[(char_to_index[plaintext[i]] + char_to_index[gamma[i]]) % 27])
            encoding = ''.join(ciphertext)

            print(encoding)
            return encoding

        elif type_of_encoding == '1':
            char = input("Введите ключ - букву: \n")
            if len(char) != 1:
                print("Введите 1 букву!\n")
                return 0

            gamma = char

            plaintext = input("Введите исходный текст: \n")
            i = 0

            while len(gamma) != len(plaintext):
                gamma += plaintext[i]
                i += 1

            ciphertext = []
            for i in range(len(plaintext)):
                ciphertext.append(
                    index_to_char[(char_to_index[plaintext[i]] + char_to_index[gamma[i]]) % 27])
            encoding = ''.join(ciphertext)

            print(encoding)
            return encoding

        elif type_of_encoding == '2':
            char = input("Введите исходную букву: \n")
            if len(char) != 1:
                print("Введите 1 букву!\n")
                return 0

            gamma = char

            plaintext = input("Введите исходный текст: \n")
            i = 1
            pre_ciphertext = index_to_char[(
                char_to_index[plaintext[0]] + char_to_index[char]) % 27]
            while len(gamma) != len(plaintext):
                gamma += pre_ciphertext
                pre_ciphertext = index_to_char[(
                    char_to_index[plaintext[i]] + char_to_index[gamma[i]]) % 27]
                i += 1

            ciphertext = []
            for i in range(len(plaintext)):
                ciphertext.append(
                    index_to_char[(char_to_index[plaintext[i]] + char_to_index[gamma[i]]) % 27])
            encoding = ''.join(ciphertext)

            print(encoding)
            return encoding
        else:
            print("Введите корректную цифру оперции \n")
            return 0

    elif operation == '1':
        ciphertext = input("Введите зашифрованный текст: \n")

        if type_of_encoding == '0':
            word = input("Введите исходную коротную фразу: \n")
            gamma = word

            i = 0
            while len(gamma) != len(ciphertext):
                gamma += word[i % len(word)]
                i += 1

            decrypted = []
            for j in range(len(ciphertext)):
                decrypted.append(
                    index_to_char[(char_to_index[ciphertext[j]] - char_to_index[gamma[j]]) % 27])

            plaintext = ''.join(decrypted)
            print(plaintext)
            return plaintext

        elif type_of_encoding == '1':
            char = input("Введите ключ - букву: \n")

            if len(char) != 1:
                print("Введите 1 букву!\n")
                return 0

            gamma = char

            i = 0

            plaintext_list = []

            while (len(gamma) != len(ciphertext) + 1):
                pre_plaintext = index_to_char[(
                    char_to_index[ciphertext[i]] - char_to_index[gamma[i]]) % 27]
                plaintext_list.append(pre_plaintext)
                gamma += pre_plaintext
                i += 1
            gamma = gamma[:-1]

            plaintext = ''.join(plaintext_list)

            print(plaintext)
            return plaintext

        elif type_of_encoding == '2':
            char = input("Введите ключ - букву: \n")

            if len(char) != 1:
                print("Введите 1 букву!\n")
                return 0

            gamma = char
            i = 0
            while len(gamma) != len(ciphertext):
                gamma += ciphertext[i]
                i += 1
            plaintext_list = []

            for j in range(len(gamma)):
                plaintext_list.append(
                    index_to_char[(char_to_index[ciphertext[j]] - char_to_index[gamma[j]]) % 27])

            plaintext = ''.join(plaintext_list)

            print(plaintext)
            return plaintext


cipher_Vigenere()
