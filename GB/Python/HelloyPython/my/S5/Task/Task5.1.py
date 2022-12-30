print("Game 111 candy")
reserve = 111
player_num = 1
reserve_and_player_num = ""
while reserve > 0:
       
    def round(r, p, h = 28):
        remainder = int(r)
        r_and_n =""
        while remainder == int(r):
            if remainder < h:
                h = remainder
            have_taken = int(input(f'Ход игрока {p}. Осталось конфет: {r} шт. Возьмите от 1 до {h} конфет : '))
            if 1 <= have_taken <= h:
                if p == 1:
                    p = 2
                elif p == 2:
                    p =1
                remainder -=  have_taken
                r_and_n = str(remainder) + str(p)
        return r_and_n
                
    reserve_and_player_num = round(reserve, player_num)
    reserve = int(reserve_and_player_num[0 :-1])
    player_num = int(reserve_and_player_num[-1])
   #    print(f'reserve {reserve} player_num {player_num}')

if reserve == 0:
    print(f'Все конфеты достаются Игроку {player_num}')

