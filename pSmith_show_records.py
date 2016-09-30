#Phillip Smith
#Hmwrk 6
#this module shows coffee inventory records

def show_coffee():
	#open file
	coffee_file = open('coffee.txt','r')
	
	#read first description field
	descr = coffee_file.readline()
	
	#read rest of file loop
	while descr != '':
		qty = float(coffee_file.readline())
		
		#strip newline char
		descr = descr.rstrip('\n')
		
		#Display
		print('Description: ', descr)
		print('Quantity: ', qty)
		print()
		
		#read next description
		descr = coffee_file.readline()
		
	#close file
	coffee_file.close()