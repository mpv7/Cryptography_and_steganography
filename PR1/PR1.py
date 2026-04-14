
def simple_replace(s): #готов
    
    from string import printable
    import random
    
    chars=[]
    b='0'
    if b == '0':
        unique_chars = [x for x in printable[10:36]]



        key = {}
        index = random.sample(range(26),26)

        for i in range(26):
            key[unique_chars[i]] = printable[10+index[i]]
            
        for i in range(len(s)):
            if s[i]=='\n' or s[i]=='\xa0' or s[i]=='&' or s[i]=='#' or s[i]=='\t' or s[i]=='…':
                continue

            else:
                chars.append(key[s[i]])
        
        res = ''.join(chars)


        print("Ваш ключ шифрования:",key)
        print(res)

        
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









    
def Afin_cipher(s): #готов

    from string import printable
    from math import gcd

    f = '0'
    a = 3
    b = 17
    m = 26


    
    char_to_index = {char: i for i, char in enumerate(printable[10:36])}
    index_to_char = {i: char for i, char in enumerate(printable[10:36])}
    

    if f=='0':
        chars = []
        for char in s:
            if char=='\n' or char=='\xa0' or char=='&' or char=='#' or char=='\t' or char=='…':
                continue

            else:
                chars.append( index_to_char[(a*char_to_index[char] + b )%m] )
        

        res = ''.join(chars)

        return res



 
        

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
    





    
def recur_Afin_cipher(s): 
    from string import printable
    from math import gcd

    f = '0'
    a0 = 67
    a1 = 81
    b0 = 32
    b1 = 45
    m = 26

    if ( gcd(a0,m)!=1 ) or ( gcd(a1,m)!=1 ) :
        print("введите корректные a1 и a0")
        return 0

    char_to_index = {char: i for i, char in enumerate(printable[10:36])}
    index_to_char = {i: char for i, char in enumerate(printable[10:36])}


    if f == "0":
        chars = []
        for i in range(len(s)):
            if s[i]=='\n' or s[i]=='\xa0' or s[i]=='&' or s[i]=='#' or s[i]=='\t' or s[i]=='…':
                continue
            else:
                chars.append( index_to_char[( char_to_index[s[i]] * recur_a(i,a0,a1,m) + recur_b(i,b0,b1,m) )%m] )

            

        res = ''.join(chars)

        return res

    


from string import printable

            
s = open("cherloc.txt").read()
##alf={}
##for x in printable[10:36]:
##    alf[x] = s.count(x)
##print(alf)
        

##for keys,value in alf.items():
##    print(keys,value)
##
##res= recur_Afin_cipher(s)
##alf1={}
##for x in printable[10:36]:
##    alf1[x] = res.count(x)
##print(alf1)



s='twasbrilligandtheslithytovesdidgyreandgimbleinthewabeallmimsyweretheborogovesandthemomerathsoutgrabebewarethejabberwockmysonthejawsthatbitetheclawsthatcatchbewarethejubjubbirdandshunthefrumiousbandersnatchhetookhisvorpalswordinhandlongtimethemanxomefoehesoughtsorestedhebythetumtumtreeandstoodawhileinthoughtandasinuffishthoughthestoodthejabberwockwitheyesofflamecamewhifflingthroughthetulgeywoodandburbledasitcameonetwoonetwoandthroughandthroughthevorpalbladewentsnickersnackheleftitdeadandwithitsheadhewentgalumphingbackandhastthouslainthejabberwockcometomyarmsmybeamishboyofrabjousdaycalloohcallayhechortledinhisjoytwasbrilligandtheslithytovesdidgyreandgimbleinthewabeallmimsyweretheborogovesandthemomerathsoutgrabe'

#f=simple_replace(s)
#rint(f)

rf='vbgoxwpyypfgdzvkqoypvkhvjtqozpzfhwqgdzfpsxyqpdvkqbgxqgyyspsohbqwqvkqxjwjfjtqogdzvkqsjsqwgvkojcvfwgxqxqbgwqvkqegxxqwbjunshojdvkqegbovkgvxpvqvkquygbovkgvugvukxqbgwqvkqecxecxxpwzgdzokcdvkqawcspjcoxgdzqwodgvukkqvjjnkpotjwlgyobjwzpdkgdzyjdfvpsqvkqsgdrjsqajqkqojcfkvojwqovqzkqxhvkqvcsvcsvwqqgdzovjjzgbkpyqpdvkjcfkvgdzgopdcaapokvkjcfkvkqovjjzvkqegxxqwbjunbpvkqhqojaaygsqugsqbkpaaypdfvkwjcfkvkqvcyfqhbjjzgdzxcwxyqzgopvugsqjdqvbjjdqvbjgdzvkwjcfkgdzvkwjcfkvkqtjwlgyxygzqbqdvodpunqwodgunkqyqavpvzqgzgdzbpvkpvokqgzkqbqdvfgycslkpdfxgungdzkgovvkjcoygpdvkqegxxqwbjunujsqvjshgwsoshxqgspokxjhjawgxejcozghugyyjjkugyyghkqukjwvyqzpdkpoejhvbgoxwpyypfgdzvkqoypvkhvjtqozpzfhwqgdzfpsxyqpdvkqbgxqgyyspsohbqwqvkqxjwjfjtqogdzvkqsjsqwgvkojcvfwgxq'

for i in range (2,10000):
    try :
        s = rf[i-2]+rf[i-1]+rf[i]
        if s == 'vkq':
            rf = rf.replace(s,' the ',1)
    except:
        break

rf=rf.replace('q','e').replace('v','t').replace('k','h')\
    .replace('o','s').replace('d','n').replace('z','d').replace('g','a').replace('j','o')\
    .replace('and',' and ').replace('that',' that ').replace('x','b').\
    replace('p','i').replace('y','l')
print(rf)























































































