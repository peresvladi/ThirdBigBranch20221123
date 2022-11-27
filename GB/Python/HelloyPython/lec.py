

























""" print('Введите значение координаты точки X')

x = int(input())

print('Введите значение координаты точки Y')
y = int(input())

if x > 0 and y > 0:
    print('точка введеных координат расположена в 1 четверти плоскости системы координат')
elif x > 0 and y < 0:
    print('точка введеных координат расположена в 4 четверти плоскости системы координат')
elif x < 0 and y > 0:
    print('точка введеных координат расположена в 2 четверти плоскости системы координат')
elif x < 0 and y < 0:
    print('точка введеных координат расположена в 3 четверти плоскости системы координат')
 """
















""" count_list = [0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1]

r = int(1)
m = int(0)
for i in count_list:
        
                    
        if m==0:
            left_x = i
            #print("left_x: "+str(left_x))
            right_x = i 
            #print("right_x: " +str(right_x))
            m=m+1 
        elif m==1:
            left_y = i
            #print("left_y: "+str(left_y))
            right_y = i
            #print("right_y: " +str(right_y))
            m=m+1 
        elif m==2:
            print("************************ ц и к л" + (str(r)) + " ***************************")
            r=r+1
            m=0
            left_z = i
            #print("left_z: "+str(left_z))
            right_z = i  
            #print("right_z: " +str(right_z))
            txt_expression = "¬(X ∨ Y ∨ Z)=¬X ∧ ¬Y ∧ ¬Z"
           
            if not((bool(left_x) == False and bool(left_y) == False and bool(left_z) == False) != True):
                part_left1 = str(txt_expression[0:12])
                print("left_X = "+str(left_x) + " left_Y = "+str(left_y)+ " left_Z = "+str(left_z))
                print (part_left1 +" = ИСТИНА") 
            else:
                part_left2 = str(txt_expression[0:12])
                print("left_X = "+str(left_x) + " left_Y = "+str(left_y)+ " left_Z = "+str(left_z))
                print (part_left2 +" = ЛОЖЬ") 
            if not(bool(right_x) == True) and not(bool(right_y) == True) and not(bool(right_z) == True):
                part_right1 = str(txt_expression[13:25])
                print("right_X = "+str(right_x) + " right_Y = "+str(right_y)+ " right_Z = "+str(right_z))
                print (part_right1 +" = ИСТИНА") 
            else:
                part_right2 = str(txt_expression[13:25])
                print("right_X = "+str(right_x) + " right_Y = "+str(right_y)+ " right_Z = "+str(right_z))
                print (part_right2 +" = ЛОЖЬ") """ 
            
    
          
        

   
    








































# print('Введите число дня недели. ')
# day_off = int(input())

# if day_off == 7:
#     print('Ура, сегодня воскресенье - выходно ! Можно отдыхать, но не слишком. Завтра на работу.')
# elif day_off == 6:
#     print('Ура, сегодня суббота - выходной ! Одныхаем по полной !')
# elif day_off == 5:
#     print('Пятница. Это почти финиш. Еще немного и можно будет наконец раслабиться')
# elif day_off == 4:
#     print('Четверг. Ну вот и заканчивается рабочая неделя. Продержаться осталось не долго.')
# elif day_off == 3:
#     print('Среда. Достигли экватора. Да! Мы смогли это сделать!!!')
# elif day_off == 2:
#     print('Вторник. Еще работать и работать((( ')
# elif day_off ==1:
#     print('Понедельник. Неделя только началась. Об отдыхе думать еще рано ((( Ни кто так не нуждается в отдыхе, как человек после отдыха((( Мудрость веков...')
# else:
#     print('Нет такого дня недели. Если будем его указывать. Выходной нам, как не грустно не прибавится')























# count_list1 = [0,0,0]
# count_list2 = [0,0,1]
# count_list3 = [0,1,0]
# count_list4 = [0,1,1]
# count_list5 = [1,0,0]
# count_list6 = [1,0,1]
# count_list7 = [1,1,0]
# count_list8 = [1,1,1]









































































































