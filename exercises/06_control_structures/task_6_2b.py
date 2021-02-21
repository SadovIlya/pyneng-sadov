# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
correct = False
while correct == False:
	ip = input('вод IP-адреса в формате 10.0.1.1: ')
	ip1 = ip.split('.')
	if len(ip1) == 4:
		correct = True
	for element in ip1:
			if not ((element.isdigit() and int(element) in range(256))):
				correct = False
	
	
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
			
