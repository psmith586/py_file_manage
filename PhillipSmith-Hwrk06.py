#Phillip Smith
#Hmwrk6
#Coffee File Management System

import pSmith_coffee_records
import pSmith_show_records
import pSmith_mod_records
import pSmith_search_records
import pSmith_delete_records

#define menu choices
ADD_COFFEE_CHOICE = 1
SHOW_COFFEE_CHOICE = 2
MODIFY_COFFEE_CHOICE = 3
SEARCH_COFFEE_CHOICE = 4
DELETE_COFFEE_CHOICE = 5
QUIT_CHOICE = 6

def main():
	choice = 0
	while choice != QUIT_CHOICE:
		disply_menu()
		choice = int(input('Enter your choice: '))
		if choice == ADD_COFFEE_CHOICE:
			pSmith_coffee_records.add_coffee()
		elif choice == SHOW_COFFEE_CHOICE:
			pSmith_show_records.show_coffee()
		elif choice == MODIFY_COFFEE_CHOICE:
			pSmith_mod_records.mod_coffee()
		elif choice == SEARCH_COFFEE_CHOICE:
			pSmith_search_records.search_coffee()
		elif choice == DELETE_COFFEE_CHOICE:
			pSmith_delete_records.delete_coffee()
		elif choice == QUIT_CHOICE:
			print('Exiting the program...')
		else:
			print('Error: Invalid Selection.')
			
#define menu function
def disply_menu():
	print('PHILLIP SMITH COFFEE MANAGEMENT MENU')
	print('1) Add more Coffee Choices to List')
	print('2) Display all Coffee Choices')
	print('3) Modify Coffee Choices')
	print('4) Search Coffee Choices')
	print('5) Delete a Coffee Choice')
	print('6) Quit')

#call main function	
main()