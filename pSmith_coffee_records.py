#Phillip Smith
#Hmwrk 6
#this module adds coffee inventory records

def add_coffee():
	another = 'y'
	
	#open file
	coffee_file = open('coffee.txt','a')
	
	#add records to file
	while another == 'y' or another == 'Y':
		print('Enter the following coffee data: ')
		descr = input('Description: ')
		qty = float(input('Quantity [in pounds]: '))
		
		#append data to file
		coffee_file.write(descr + '\n')
		coffee_file.write(str(qty) + '\n')
		
		#ask if user wants to add another
		print('Do you want to add another record?')
		another = input('Y = yes, anything else = no: ')
		
	#close file
	coffee_file.close()
	print('Data appended to coffee.txt.')


	