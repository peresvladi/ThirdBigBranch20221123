print('Вас приветствует телефонный справочник !')
select_recording_format = ""
with open ('/home/vladi/Education/GB/Python/HelloyPython/my/S7/select_rec_format', "a+" ) as data:
  data.close
with open ('/home/vladi/Education/GB/Python/HelloyPython/my/S7/select_rec_format', "r" ) as data:
  for line in data:
    select_recording_format = line
if select_recording_format == "":
  print('Вы можете выбрать один из двух форматов записи данных. \n Формат 1. : Предлагает каждай элемент записи вносить с новой строки. \n Формат 2. : Предалагает использовать в качестве разделителя - ; (точку с запятой )')
  select_recording_format = input('Для выбора формата введите 1 или 2 :') # дописать проверку на ввод только 1 или 2
  with open ('/home/vladi/Education/GB/Python/HelloyPython/my/S7/select_rec_format', "w") as data:
      data.write (select_recording_format)
choosing_an_action = input('Что бы перейти в модуль запросов нажмите f (find - находить), \n для перехода в модуль ввода данных нажмите a (add - добавить).') # дописать проверку на ввод





