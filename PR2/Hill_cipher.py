def Hill_cipher(): ### ГОТОВ
    import numpy as np
    from string import printable
    import random
    from math import gcd

    b = input("Введите, какую операцию хотите произвести цифрой (где 0 - шифрование, 1 - расшифрование) :\n")
    s = input("Введите ваш текст:\n")
    lb = int(input("Введите длину блока: \n"))

    
    ost = len(s) % lb
    while ost != 0:
        s+=' '
        #s += random.choice(printable[10:36])
        ost -= 1

    char_to_index = {char: i for i, char in enumerate(printable[10:36])}
    char_to_index[' '] = 26
    index_to_char = {i: char for i, char in enumerate(printable[10:36])}
    index_to_char[26] = ' '

    if b == '0':  # ШИФРОВАНИЕ
        # Генерация обратимого ключа
        while True:
            key = np.random.randint(0, 27, (lb, lb))
            det_mod = int(round(np.linalg.det(key))) % 27
            if det_mod != 0 and gcd(det_mod, 27) == 1:
                break
        
        print(f"Ключ шифрования:\n{key}")
        
        blocks = []
        encrypted_blocks = []
        
        for i in range(len(s)):
            blocks.append(char_to_index[s[i]])
            if len(blocks) == lb:
                block_array = np.array(blocks).reshape(1, lb)
                encrypted = (block_array @ key) % 27
                encrypted_blocks.append(encrypted.flatten())
                blocks = []

        res = ''
        for block in encrypted_blocks:
            for num in block:
                res += index_to_char[int(num)]
        
        print(f"Зашифрованный текст: {res}")
        return res, key

    elif b == '1':  # РАСШИФРОВАНИЕ
        import ast
        
        def mod_inverse(a, m):
            for x in range(1, m):
                if (a * x) % m == 1:
                    return x
            return None
        
        def matrix_mod_inv(matrix, mod=27):
            n = len(matrix)
            det = int(round(np.linalg.det(matrix))) % mod
            
            # Проверяем, что определитель обратим
            det_inv = mod_inverse(det, mod)
            if det_inv is None:
                return None
            
            # Матрица алгебраических дополнений
            adjugate = np.zeros((n, n), dtype=int)
            
            for i in range(n):
                for j in range(n):
                    minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                    minor_det = int(round(np.linalg.det(minor)))
                    adjugate[j, i] = ((-1) ** (i + j)) * (minor_det % mod) % mod
            
            return (det_inv * adjugate) % mod
        
        try:
            # Ввод ключа
            key_input = input("Введите ключ шифрования (исходную матрицу): \n")
            key = ast.literal_eval(key_input)
            key = np.array(key)
            
            # Вычисляем обратную матрицу по модулю 27
            key_inv = matrix_mod_inv(key, 27)
            
            if key_inv is None:
                print("Ошибка: матрица необратима по модулю 27")
                return None
            
            #print(f"Обратная матрица по модулю 27:\n{key_inv}")
            
            # Расшифрование
            decrypted_blocks = []
            blocks = []
            
            for i in range(len(s)):
                blocks.append(char_to_index[s[i]])
                if len(blocks) == lb:
                    block_array = np.array(blocks).reshape(1, lb)
                    decrypted = (block_array @ key_inv) % 27
                    decrypted_blocks.append(decrypted.flatten().astype(int))
                    blocks = []
            
            # Преобразуем числа обратно в символы
            res = ''
            for block in decrypted_blocks:
                for num in block:
                    res += index_to_char[num]
            
            print(f"Расшифрованный текст: {res}")
            return res
            
        except Exception as e:
            print(f"Ошибка ввода ключа: {e}")
            return
    else:
        print("Введите корректную цифру операции\n")
        return None
    
Hill_cipher()
