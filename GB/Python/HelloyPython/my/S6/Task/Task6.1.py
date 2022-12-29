Sample = '1 * 16 + 10 * 2 - 4 / 2 / 2'
res = 0
result = 0
List_sample = Sample.split()

def val_indexx():
    
    if List_sample.count('*') > 0 and List_sample.count('/') > 0:
        if List_sample.index('*') < List_sample.index('/'):
            i = List_sample.index('*') 
            return i 
        else:
            i = List_sample.index('/') 
            return i 

    elif List_sample.count('*') == 0 and List_sample.count('/') > 0:
        i = List_sample.index('/') 
        return i 
    elif List_sample.count('*') > 0 and List_sample.count('/') == 0:
        i = List_sample.index('*') 
        return i 
    
    if List_sample.count('+') > 0 and List_sample.count('-') > 0:
        if List_sample.index('+') < List_sample.index('-'):
            i = List_sample.index('+') 
            return i 
        else:
            i = List_sample.index('-') 
            return i 
    elif List_sample.count('+') == 0 or List_sample.count('-') > 0:
        i = List_sample.index('-') 
        return i 
    elif List_sample.count('+') > 0 or List_sample.count('-') == 0:
        i = List_sample.index('+') 
        return i 
        
def Calculations(ind):
    if List_sample[ind] == '*':
        r = int(List_sample[ind-1]) * int(List_sample[ind + 1]) 
        return r 
    elif List_sample[ind] == "/":
        r = int(List_sample[ind-1]) / int(List_sample[ind + 1])
        return r 
    elif List_sample[ind] == "+":
        r = int(List_sample[ind-1]) + int(List_sample[ind + 1]) 
        return r 
    elif List_sample[ind] == "-":
        r = int(List_sample[ind-1]) - int(List_sample[ind + 1])  
        return r   


while List_sample.count('*')!= 0 or List_sample.count('/') != 0:
 if List_sample.count('*') != 0 or  List_sample.count('/') != 0:
  indexx = val_indexx()
  res = Calculations(indexx)
  List_sample.pop(indexx-1)
  List_sample.pop(indexx-1)
  List_sample.pop(indexx-1)
  List_sample.insert(indexx-1, res)

while List_sample.count('+')!= 0 or List_sample.count('-') != 0:
 if List_sample.count('+') != 0 or  List_sample.count('-') != 0:
  indexx = val_indexx()
  res = Calculations(indexx)
  List_sample.pop(indexx-1)
  List_sample.pop(indexx-1)
  List_sample.pop(indexx-1)
  List_sample.insert(indexx-1, res)

  print(List_sample)

