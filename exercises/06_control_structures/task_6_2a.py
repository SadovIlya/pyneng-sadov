# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP: ')
ip1 = ip.split('.')
#ip = input('вод IP-адреса в формате 10.0.1.1: ')

correct = True

if len(ip1) != 4:
	correct = False
else:
	for element in ip1:
		if not (element.isdigit() and int(element) in range(256)):
			correct = False
			break
if correct == False:
	print("Неправильный IP-адрес")
else:
	if int(ip1[0]) in range(1,224):
		print('unicast')
	elif int(ip1[0]) in range(224,240):
		print('multicast')
	elif ip == '255.255.255.255':
		print('local broadcast')
	elif ip == '0.0.0.0':
		print('unassigned')
	else:
		print('unused')
		




