password = 'abc'
i = 3
while True:
	passw = input('enter your password: ')
	if passw == password:
		print('right password')
		break
	else:
		passw != password
		print('wrong password')
		print('you still have ', i ,'chance.')
		i = i - 1
		if i < 0:
			print('chance end')
			break


