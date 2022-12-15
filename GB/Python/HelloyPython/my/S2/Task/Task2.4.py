#Реализуйте механизм нахождения(генерации) рандомного (случайного) числа(Не используя библиотеки связанные с рандомом


def collector(x, y, c):
 m=""
 h = y
 b1=casual(h)
 for i in b1:
    if x <= int(i) <= y:
        m = m + i
 return m

def casual(h):
    a={}
    d=[]
    s=0
    t=0
    b=(list(str(id(a))))
    b=b[3:len(b)] # значение первых трех элементов исключаем т.к. их значения при вызовах id существенно не обнавляются
    if h < 10:
        b

    elif 9 < h < 100:
        for j in b:
            d = d + [b[s - 1] + j]
            s = s + 1

        for y in b:
            d.insert(t, y)
            t = t + 2
        b = d
    return b

def ccontrole(m_n, m_x, c_t):
    ssum = []
    result = []
    while len(ssum) < c_t:
        ssum = ssum + list(collector(m_n, m_x, c_t))
        result = ssum[len(ssum) - count : len(ssum)]
    return result 
    
count = 10
max = 9
min = 0
print (ccontrole (min, max, count))

