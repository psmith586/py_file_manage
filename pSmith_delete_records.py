#Phillip Smith
#Hmwrk 6
#this module deletes coffee inventory records

import os

def delete_coffee():
	found = False
	search = input('Which coffee do you want to delete? ')
	
	#open file
	coffee_file = open('coffee.txt','r')
	
	#open temp file
	temp_file = open('temp.txt','w')
	
	#read first line
	descr = coffee_file.readline()
	
	#continue reading
	while descr != '':
		qty = float(coffee_file.readline())
		
		#strip newline char
		descr = descr.rstrip('\n')
		
		#if not to be deleted, write to temp
		if descr != search:
			temp_file.write(descr + '\n')
			temp_file.write(str(qty) + '\n')
		else:
			found = True
		
		#read next line
		descr = coffee_file.readline()

	#close files
	coffee_file.close()
	temp_file.close()
	
	#delete original
	os.remove('coffee.txt')
	
	#rename temp
	os.rename('temp.txt','coffee.txt')
	
	#error message for search not found
	if found:
		print('The file has been updated.')
	else:
		print('That item was not found in this file.')