from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date
import os, sys, shelve, pprint
import db_file_handling as dfh

#One file for user input, one file for adding to .db
#Everytime wishlist delete is called, .db file pops value from wishlist list

book_file = ''
file_name = 'Books.txt'
book_file = shelve.open(file_name)

new_book_list = []
finished_book_list = []
# wishlist_add_list = []
# wishlist_delete_list = []


decision_val = input("Do you want to start a new book, update wish list or report a finished book? (N, W, F). Q to quit.\n")
user_input_book = ''
wishlist_val = ''
delete_wl = False

while decision_val.upper() != 'Q':
    if decision_val.upper() == 'N':
        user_input_book = input("What book do you want to start?\n")
        new_book_list.append(user_input_book)
        #new_book(user_input_book)
    elif decision_val.upper() == 'F':
        user_input_book = input('What book did you just finish?\n')
        finished_book_list.append(user_input_book)
        #finished_book(user_input_book)

        ''' elif decision_val.upper() == 'W':
        while wishlist_val != 'Q':
            wishlist_val = input("Did you want to delete (D) or add (A) to the wishlist? Q to quit.")
            if wishlist_val.upper() == 'D':
                del_in = input('What book do you want to delete?')
                wishlist_delete_list.append(del_in)
                #wish_list_del(wishlist_val)
            elif wishlist_val.upper() == 'A':
                add_in = input("What book do you want to add?")
                wishlist_add_list.append(add_in)
                #wish_list_add(wishlist_val)
            elif wishlist_val.upper() == 'Q':
                print('Exiting wish list modification.')
                break
            else:
                print("\nUnrecognized keyword.\n")
        print("MOdified wishlist.\n")
    '''
    else:
        print('Unrecognized value, please try again.\n')
    print('...\n')

    decision_val = input('N, W, F or Q?')

def print_lists(str_temp):
    if str_temp == "New":
        print(dfh.print_new())
    elif str_temp == "Finished":
        print(dfh.print_fininshed())


dfh.new_book(new_book_list)
dfh.finished_book(finished_book_list)
#dfh.wish_list_add(wishlist_add_list)
#dfh.wish_list_del(wishlist_delete_list)

print_lists(input("What lists should we print out? (New/Finished)"))

for x in new_book_list:
    dfh.find_book(x)

#create file if file doesn't exist, open file if file exists


#enter name of book into file for want to read/


#post review into


'''
if input('Add or delete WL item? (A, D)').upper() == 'A':
    user_input_book = input("What book did you want to add to the wishlist?\n")
    wish_list(user_input_book, True)
elif input('Add or delete WL item? (A, D').upper() == 'D':
    user_input_book = input("What book did you want to delete from the wishlist?\n")
    wish_list(user_input_book, False)
    '''