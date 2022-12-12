lst=[0]
def ran():
 lst.append(lst[-1]+1)
 a=str(id(lst[-1]))
 num = 0
 for i in (a):
    num = int(i)
    n=(str(num)[1])
    n=int(n)
    return(n)
#calling the ran()function gives you 10 random numbers.
for i in range(10):
    print(ran())