from random import *
s=nol=pos=neg=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",nol)
    kesk=keskmine(p)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)

def vahetus(a:int,b:int):
    """Kui a>b siis vahetame neid
    :param int a: Arv mis on suurem kui b
    :param int b: Arv mis on vaiksem kui a
    :rtype:int, int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """ Genereerib arvu
    :param int n: Mittu numbrid genereerib list
    :param list loend: list numbridega
    :param int a: Arv mis on suurem kui b
    :param int b: Arv mis on vaiksem kui a
    :rtype: int, list, int, int
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:int,n:int,nol:list):
    """Jagab numbreid listis
    :param list loend: list numbridega
    :param p int: positivne numbridega list
    :paran n int: negativne numbridega list
    :param nol list: nulliga list
    :rtype: list, int, int, list
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend:list)->list:
    """ 
    :param loend list: list numbridega
    :rtype: list
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
            kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:int):
    """ Lisab numbrid algsele listi
    :param loend list: list numbridega
    :param el int: numbrid mis lisakse ei algsele listi
    :rtype: list, int
    """
    loend.append(el)
    loend.sort()

arvud_loendis()
