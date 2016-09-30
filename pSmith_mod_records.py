#Phillip Smith
#Hmwrk 6
#this module modifies coffee inventory records

import os

def mod_coffee():
	found = False
	
	#get search value and new qty
	search = input('Enter a description to search for: ')
	new_qty = float(input('Enter the new quantity: '))
	
	#open the file 
	coffee_file = open('coffee.txt', 'r')
	
	#open temp file
	temp_file = open('temp.txt', 'w')
	
	#read first description
	descr = coffee_file.readline()
	
	#continue reading
	while descr != '':
		qty = float(coffee_file.readline())
		descr = descr.rstrip('\n')
		
		#write to temp or modify this record 
		if descr == search:
			temp_file.write(descr + '\n')
			temp_file.write(str(new_qty) + '\n')
			
			found = True
		
		else:
			temp_file.write(descr + '\n')
			temp_file.write(str(qty) + '\n')
		
		descr = coffee_file.readline()
	
	#close file
	coffee_file.close()
	temp_file.close()
	
	#delete original file
	os.remove('coffee.txt')
	
	#rename temp
	os.rename('temp.txt','coffee.txt')
	
	if found:
		print('The file has been updated.')
	else:
		print('That item was not found in this file.')