from functools import lru_cache
@lru_cache(None)
def recur_a(n,a0,a1,m):
    if n==0:
        return a0%m
    if n==1:
        return a1%m
    else:
        return (recur_a(n-1,a0,a1,m) * recur_a(n-2,a0,a1,m))%m
@lru_cache(None)
def inv_a(n,a0,a1,m):
    if n==0:
        inv_a_n = None
        for i in range(m):
            if (a0*i)%m==1:
                inv_a_n=i
                break
        return inv_a_n
    elif n==1:
        inv_a_n = None
        for i in range(m):
            if (a1*i)%m==1:
                inv_a_n=i
                break
        return inv_a_n
    else:
        return (inv_a(n-2,a0,a1,m)*inv_a(n-1,a0,a1,m))%m
@lru_cache(None)
def recur_b(n,b0,b1,m):
    if n==0:
        return b0%m
    if n==1:
        return b1%m
    else:
        return (recur_b(n-1,b0,b1,m) + recur_b(n-2,b0,b1,m))%m
    





    
def recur_Afin_cipher(): 
    from string import printable
    from math import gcd

    f = input("Введите какую операцию хотите произвести цифрой (где 0 - шифрование, а 1 - дешифрование):\n")
    print("В афинном рекурентом шифре y_i = (a_i*x + b_i)%m (где m - мощьность алфавита<=100) , введите a0 и a1; b0 и b1; m так, чтобы НОД(a1,m)=1\n и НОД(a0,m)=1")

    a0 = int(input("Введите a0:\n"))
    a1 = int(input("Введите a1:\n"))
    b0 = int(input("Введите b0:\n"))
    b1 = int(input("Введите b1:\n"))
    m = int(input("Введите m:\n"))

    if ( gcd(a0,m)!=1 ) or ( gcd(a1,m)!=1 ) :
        print("введите корректные a1 и a0")
        return 0

    char_to_index = {char: i for i, char in enumerate(printable)}
    index_to_char = {i: char for i, char in enumerate(printable)}

    s = input("Введите ваш текст:\n")

    if f == "0":
        chars = []
        for i in range(len(s)):
            chars.append( index_to_char[( char_to_index[s[i]] * recur_a(i,a0,a1,m) + recur_b(i,b0,b1,m) )%m] )
            

        res = ''.join(chars)
        print("Ваше закодированое сообщение:",res)
        return res

    elif f == '1':
        chars=[]
        for i in range(len(s)):
            a_i = recur_a(i,a0,a1,m)
            b_i = recur_b(i,b0,b1,m)

            #a_inv_i = inv_a(i,a0,a1,m)

            chars.append(index_to_char[( ( char_to_index[s[i]] - b_i )*pow(a_i, -1, m) )%m])
            print(pow(a_i, -1, m))

        res=''.join(chars)

        print("Ваше декодированое сообщение:",res)
        return res
    

    else:
        print("введите корректную цифру операции")
        return 0
    

