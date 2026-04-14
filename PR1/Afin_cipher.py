def Afin_cipher(): #готов

    from string import printable
    from math import gcd

    f = input("Введите какую операцию хотите произвести цифрой (где 0 - шифрование, а 1 - дешифрование):\n")
    print("В Афинном шифре y = (a*x + b)%m (где m - мощьность алфавита<=100) , введите a, b, m так, чтобы НОД(a,m)=1\n")
    a = int(input("Введите a:\n"))
    b = int(input("Введите b:\n"))
    m = int(input("Введите m:\n"))

    if (gcd(a,m)!=1):
        print("НОД(a,b) не равен 1!")
        return 0


    
    char_to_index = {char: i for i, char in enumerate(printable[10:36])}
    index_to_char = {i: char for i, char in enumerate(printable[10:36])}
    
    s = input("Введите ваш текст:\n")

    if f=='0':
        chars = []
        for char in s:
            chars.append( index_to_char[(a*char_to_index[char] + b )%m] )

        res = ''.join(chars)

        print("Ваше закодированое сообщение:",res)
        return res

    elif f=='1':
        chars=[]

        a_inv = None
        for i in range(m):
            if (a * i) % m == 1:
                a_inv = i
                break
    
        if a_inv is None:
            print(f"Ошибка: не найдено обратное к a{m}")
            return 0
        
        for char in s:
            chars.append( index_to_char[ ( (char_to_index[char] - b)*a_inv )%m ] )

        res = ''.join(chars)

        print("Ваше декодированое сообщение:",res)
        return res
    

    else:
        print("введите корректную цифру операции")
        return 0


Afin_cipher()
