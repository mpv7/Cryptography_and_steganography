def simple_replace(s): #готов
    
    from string import printable
    import random
    
    b = input("Введите какую операцию хотите произвести цифрой (где 0 - шифрование, а 1 - дешифрование):\n")
    chars=[]

    if b == '0':
        unique_chars = []
        for char in s:
            if char not in unique_chars:
                unique_chars.append(char)

        key = {}
        index = random.sample(range(len(printable[10:36])),len(unique_chars))

        for i in range(len(unique_chars)):
            key[unique_chars[i]] = printable[index[i]]
        key[' '] = [' ']
            
        for i in range(len(s)):
            chars.append(key[s[i]])
        
        res = ''.join(chars)

        print("Ваш ключ шифрования:",key)
        print("Ваше закодированое сообщение:",res)
        
        return res
    
    elif b == '1':
        import ast
        user_input = input("Введите ваш ключ шифрования:\n")
        
        try:
            shifr = ast.literal_eval(user_input)

        except (SyntaxError, ValueError) as e:
            print(f"Ошибка преобразования:{e}\n")

        key =  {value: key for key, value in shifr.items()}

        for i in range(len(s)):
            chars.append(key[s[i]])
        res = ''.join(chars)

        print("Ключ дешифрования:",key)
        print("Раскодированное сообщение:",res)
        return res
    else:
        print("Вы ввели неправильнкю цифру, повторите выполнение функции")
        return 0


s='two roads diverged in a yellow wood and sorry i could not travel both and be one traveler long i stood and looked down one as far as i could to where it bent in the undergrowth then took the other as just as fair and having perhaps the better claim because it was grassy and wanted wear though as for that the passing there had worn them really about the same'
simple_replace(s)




