import shelve, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import db_file_handling as d


find_book_list = []
def get_user_input():
    d.sign_in()
    str = ''
    while str.upper() != "Q":
        str = input("What book would you like to add to your wishlist? (Q to quit)")
        if str == 'q' or str == 'Q':
            break
        if str == '':
            continue
        find_book_list.append(str)
    print(find_book_list)

    counter =0

    for x in find_book_list:
        find_book(x)
        counter+=1
        print(counter)
def find_book(val):
    d.refresh()
    d.find_book(val)
    #d.click_wishlist()
    time.sleep(5)
    d.click_find_libraries()
get_user_input()