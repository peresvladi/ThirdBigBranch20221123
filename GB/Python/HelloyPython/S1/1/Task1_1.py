day_off = int(input('Введите число дня недели : '))

if day_off == 7:
     print('Ура, сегодня воскресенье - выходно ! Можно отдыхать, но не слишком. Завтра на работу.')
elif day_off == 6:
     print('Ура, сегодня суббота - выходной ! Одныхаем по полной !')
elif day_off == 5:
     print('Пятница. Это почти финиш. Еще немного и можно будет наконец раслабиться')
elif day_off == 4:
     print('Четверг. Ну вот и заканчивается рабочая неделя. Продержаться осталось не долго.')
elif day_off == 3:
     print('Среда. Достигли экватора. Да! Мы смогли это сделать!!!')
elif day_off == 2:
     print('Вторник. Еще работать и работать((( ')
elif day_off ==1:
     print('Понедельник. Неделя только началась. Об отдыхе думать еще рано ((( Ни кто так не нуждается в отдыхе, как человек после отдыха((( Мудрость веков...')
else:
     print('Нет такого дня недели. Если будем его указывать. Выходной нам, как не грустно не прибавится')