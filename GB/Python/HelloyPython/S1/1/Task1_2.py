count_list = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
txt_expression = "¬(X ∨ Y ∨ Z)=¬X ∧ ¬Y ∧ ¬Z"
print('Проверка истинности утверждения: ' + txt_expression)
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
            print("************************ ц и к л " + (str(r)) + " ***************************")
            r=r+1
            m=0
            left_z = i
            #print("left_z: "+str(left_z))
            right_z = i
            #print("right_z: " +str(right_z))
            #txt_expression = "¬(X ∨ Y ∨ Z)=¬X ∧ ¬Y ∧ ¬Z"

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
                print (part_right2 +" = ЛОЖЬ")