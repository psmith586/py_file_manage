#Phillip Smith
#Hmwrk 6
#this module searches coffee inventory records

def search_coffee():
	#flag
	found = False
	
	#enter search
	search = input('Enter a description to search for: ')
	
	#open file
	coffee_file = open('coffee.txt','r')
	
	#read first record description
	descr = coffee_file.readline()
	
	#read the rest of file loop
	while descr != '':
		qty = float(coffee_file.readline())
		descr = descr.rstrip('\n')
		
		#match search
		if descr == search:
			print('Description:',descr)
			print('Quantity:',qty)
			print()
			found = True
			
		#continue reading
		descr = coffee_file.readline()
		
	#close file
	coffee_file.close()
	
	#not found message
	if not found:
		print('That item was not found in this file.')