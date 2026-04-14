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
        s += random.choice(printable[10:36])
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
        
        # Преобразуем числа обратно в символы
        res = ''
        for block in encrypted_blocks:
            for num in block:
                res += index_to_char[int(num)]
        
        print(f"Зашифрованный текст: {res}")
        return res, key

    elif b == '1':  # РАСШИФРОВАНИЕ
        import ast
        
        def mod_inverse(a, m):
            """Находит обратное число к a по модулю m"""
            for x in range(1, m):
                if (a * x) % m == 1:
                    return x
            return None
        
        def matrix_mod_inv(matrix, mod=27):
            """Находит обратную матрицу по модулю mod"""
            n = len(matrix)
            # Вычисляем определитель
            det = int(round(np.linalg.det(matrix))) % mod
            
            # Проверяем, что определитель обратим
            det_inv = mod_inverse(det, mod)
            if det_inv is None:
                return None
            
            # Матрица алгебраических дополнений (присоединенная матрица)
            adjugate = np.zeros((n, n), dtype=int)
            
            for i in range(n):
                for j in range(n):
                    # Минор
                    minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                    minor_det = int(round(np.linalg.det(minor)))
                    adjugate[j, i] = ((-1) ** (i + j)) * (minor_det % mod) % mod
            
            # Обратная матрица по модулю
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















def Recur_Hill_cipher():
    import numpy as np
    from string import printable
    import random
    from math import gcd

    b = input("Введите, какую операцию хотите произвести цифрой (где 0 - шифрование, 1 - расшифрование) :\n")
    s = input("Введите ваш текст:\n")
    lb = int(input("Введите длину блока: \n"))

    ost = len(s) % lb
    while ost != 0:
        s += random.choice(printable[10:36])
        ost -= 1

    char_to_index = {char: i for i, char in enumerate(printable[10:36])}
    char_to_index[' '] = 26
    index_to_char = {i: char for i, char in enumerate(printable[10:36])}
    index_to_char[26] = ' '

    if b == '0':  # ШИФРОВАНИЕ
        # Генерация обратимых ключей
        while True:
            key1 = np.random.randint(0, 27, (lb, lb))
            det_mod = int(round(np.linalg.det(key1))) % 27
            if det_mod != 0 and gcd(det_mod, 27) == 1:
                break
                
        while True:
            key2 = np.random.randint(0, 27, (lb, lb))
            det_mod = int(round(np.linalg.det(key2))) % 27
            if det_mod != 0 and gcd(det_mod, 27) == 1:
                break
        
        print(f"key1:\n{key1}")
        print(f"key2:\n{key2}")
        
        # Создаем кэш вручную для производительности
        key_cache = {}
        
        def key_i_cached(i):
            if i in key_cache:
                return key_cache[i]
            if i == 0:
                result = key1
            elif i == 1:
                result = key2
            else:
                result = (key_i_cached(i-2) @ key_i_cached(i-1)) % 27
            key_cache[i] = result
            return result
        
        # Разбиваем текст на блоки
        dafault_blocks = []
        block = []
        
        for i in range(len(s)):
            block.append(char_to_index[s[i]])
            if len(block) == lb:
                block_array = np.array(block).reshape(1, lb)
                dafault_blocks.append(block_array)
                block = []
        
        # Шифрование
        encrypted_blocks = []
        for i in range(len(dafault_blocks)):
            current_key = key_i_cached(i)
            encrypted = (dafault_blocks[i] @ current_key) % 27
            encrypted_blocks.append(encrypted.flatten())

        # Преобразуем в текст
        res = ''
        for block in encrypted_blocks:
            for num in block:
                res += index_to_char[int(num)]
        
        print(f"Зашифрованный текст: {res}")
        return res
    
    elif b == '1':  # РАСШИФРОВАНИЕ
        import ast
        
        def mod_inverse(a, m):
            """Находит обратное число к a по модулю m"""
            for x in range(1, m):
                if (a * x) % m == 1:
                    return x
            return None
        
        def matrix_mod_inv(matrix, mod=27):
            """Находит обратную матрицу по модулю mod"""
            n = len(matrix)
            # Вычисляем определитель
            det = int(round(np.linalg.det(matrix))) % mod
            
            # Проверяем, что определитель обратим
            det_inv = mod_inverse(det, mod)
            if det_inv is None:
                return None
            
            # Матрица алгебраических дополнений (присоединенная матрица)
            adjugate = np.zeros((n, n), dtype=int)
            
            for i in range(n):
                for j in range(n):
                    # Минор
                    minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                    minor_det = int(round(np.linalg.det(minor)))
                    adjugate[j, i] = ((-1) ** (i + j)) * (minor_det % mod) % mod
            
            # Обратная матрица по модулю
            return (det_inv * adjugate) % mod

        try:
            # Ввод ключей
            key_input = input("Введите первый ключ шифрования (исходную первую матрицу): \n")
            key1 = ast.literal_eval(key_input)
            key1 = np.array(key1)

            key_input2 = input("Введите второй ключ шифрования (исходную вторую матрицу): \n")
            key2 = ast.literal_eval(key_input2)
            key2 = np.array(key2)

            # Вычисляем обратные матрицы по модулю 27
            key_inv1 = matrix_mod_inv(key1, 27)
            if key_inv1 is None:
                print("Ошибка: первая матрица необратима по модулю 27")
                return None
            
            key_inv2 = matrix_mod_inv(key2, 27)
            if key_inv2 is None:
                print("Ошибка: вторая матрица необратима по модулю 27")
                return None
            
            #print(f"Обратная key1:\n{key_inv1}")
            #print(f"Обратная key2:\n{key_inv2}")
            
            # Создаем кэш для обратных ключей
            inv_key_cache = {}
            
            def inv_key_i_cached(i):
                """Возвращает обратную матрицу для i-го ключа"""
                if i in inv_key_cache:
                    return inv_key_cache[i]
                if i == 0:
                    result = key_inv1
                elif i == 1:
                    result = key_inv2
                else:
                    result = (inv_key_i_cached(i-1) @ inv_key_i_cached(i-2)) % 27
                inv_key_cache[i] = result
                return result
            
            # Разбиваем зашифрованный текст на блоки
            encrypted_blocks_list = []
            block = []
            
            for i in range(len(s)):
                block.append(char_to_index[s[i]])
                if len(block) == lb:
                    block_array = np.array(block).reshape(1, lb)
                    encrypted_blocks_list.append(block_array)
                    block = []
            
            # Расшифрование
            decrypted_blocks = []
            for i in range(len(encrypted_blocks_list)):
                current_inv_key = inv_key_i_cached(i)
                decrypted = (encrypted_blocks_list[i] @ current_inv_key) % 27
                decrypted_blocks.append(decrypted.flatten().astype(int))
            
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



        