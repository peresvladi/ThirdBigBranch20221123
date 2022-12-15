
def collector(x,y,c):
 m=""
 b1=casual(c)
 for i in b1:
    if x <= int(i) <= y:
        m = m + i
 return m

def casual(c):
    a={}
    b=(list(str(id(a))))
    b=b[3:len(b)] # значение первых трех элементов исключаем т.к. их значения при вызовах id существенно не обнавляются
    return b

def ccontrole(m_n, m_x, c_t):
    ssum = []
    result = []
    while len(ssum) < c_t:
        ssum = ssum + list(collector(m_n, m_x, c_t))
        result = ssum[len(ssum) - count : len(ssum)]
    return result 
    
count = 3
max = 3
min = 0
print (ccontrole (min, max, count))


# def casual(x,y,c):
# 	a={}
# 	b=(list(str(id(a))))
# 	b=b[3:len(b)] # значение первых трех элементов исключаем т.к. их значения при вызовах id существенно не обнавляются
# 	m=""
    
# 	for i in b:
# 		if x <= int(i) <= y:
# 			m = m + i #m = m + " " + i
# 	return m

# def ccontrole(m_n, m_x, c_t):
#     ssum = []
#     result = []
#     while len(ssum) < c_t:
#         ssum = ssum + list(casual(m_n, m_x, c_t))
#         result = ssum[len(ssum) - count : len(ssum)]
#     return result 
    
# count = 3
# max = 3
# min = 0
# print (ccontrole (min, max, count))




# def casual(x,y,c):
# 	a={}
# 	b=(list(str(id(a))))
# 	b=b[3:len(b)] # значение первых трех элементов исключаем т.к. их значения при вызовах id существенно не обнавляются
# 	m=""
# 	for i in b:
# 		if x <= int(i) <= y:
# 			m = m + " " + i
# 	return m


# count = 10
# max = 7
# min = 0

# print(casual(min,max,count))


# def casual(x,y,c):
# 	a={}
# 	b=(list(str(id(a))))
# 	b=b[3:len(b)] # значение первых трех элементов исключаем т.к. их значения при вызовах id существенно не обнавляются
# 	m=""
# 	for i in b*c:
# 		if x <= int(i) <= y:
# 			m = m + " " + i
# 	return m
# count = 10
# max = 3
# min = 0
# print(casual(min,max,count))		


""" a={}
#print(id(a))
c=[]
b=[str((id(a)))]
#b=list(b)
print(b)
#b.remove(0)
c = b.pop(1)
print(c)
print(type(b)) """

""" #a={}
#print(id(a))
c=[]
b=[1, 2, 3, 4]
#b=list(b)
print(f'список{b}')

c = b.pop(1)

print(f'c = b.pop(1), c = {c}')

print(f'c = b.pop(1), b = {b}') """

""" a={}
c=[]
b=(str(id(a)))
c = b.rsplit(sep =", ", maxsplit = 11)
for i in b:
	print(i) """






# from ast import NotIn
# a = NotIn
