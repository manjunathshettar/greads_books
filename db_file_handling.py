import shelve, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s= shelve.open('Books.txt')
new_list = []
finished_list = []
goodreads_link = 'https://www.goodreads.com/'
service_val = Service('/Users/manjushettar/PycharmProjects/pp1/chromedriver')
browser = webdriver.Chrome(service=service_val)
browser.get(goodreads_link)
username = 'manjshettar@gmail.com'
password ='3@uGL*5BUus@aKF'

def new_book(temp):
    if len(temp) == 0:
        return
    s['New'] = temp
    print(s['New'])

def finished_book(temp):
    if len(temp) == 0:
        return
    s['Finished'] = temp
    print(s['Finished'])
def print_new():
    new_list = s['New']
    return new_list
def print_finished():
    finished_list = s['Finished']
    return finished_list
def sign_in():
    sign_in = ''
    try:
        sign_in = browser.find_element(By.XPATH, '//*[@id="signIn"]/div/div/a')
    except:
        print("????")
    sign_in.click()

    u_text = browser.find_element(By.ID, 'user_email')
    u_text.send_keys(username)
    p_text = browser.find_element(By.ID, 'user_password')
    p_text.send_keys(password)
    s_button = browser.find_element(By.XPATH, '//*[@id="emailForm"]/form/fieldset/div[5]/input')
    s_button.click()
def refresh():
    browser.get(goodreads_link)

def click_wishlist():
    wl = ''
    try:
        #xpath: //*[@id="1_book_31933977"]/div[1]/form/button
        wl = browser.find_element(By.XPATH, '//*[@id="1_book_12767"]/div[1]/form/button')
    except:
        print("Could not find WL button.")
    wl.click()

def click_find_libraries():
    fl = ''
    try:
        fl = browser.find_element(By.XPATH, '//*[@id="buyButtonContainer"]/ul/li[3]/a')
    except:
        fl = browser.find_element(By.CLASS_NAME, 'buttonBar')
    fl.click()
def find_book(book_to_be_reviewed):
    search_box = ''

    try:
        search_box = browser.find_element(By.XPATH, '/html/body/div[2]/div/header/div[2]/div/div[2]/form/input[1]')
    except:
        print("Could not find.")

    search_box.send_keys(book_to_be_reviewed)
   # time.sleep(100)

    submit_button = ''
    try:
        submit_button = browser.find_element(By.XPATH, '/html/body/div[2]/div/header/div[2]/div/div[2]/form/button')
    except:
        print("???")
    submit_button.click()

    link = ''
    try:
        link = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a/span')
    except:
        print("Bruh wrtf")
    link.click()



def create_review():
    review_text_button = ''
    try:
        review_text_button = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/div[3]/div[2]/div/table/tbody/tr[6]/td[2]/a')
    except:
        print("Could not find review box, you likely already have submitted a review.")
    review_text_button.click()

    r_text_box = ''

    try:
        r_text_box = browser.find_element(By.XPATH, '//*[@id="review_review_usertext"]')
    except:
        print("??????")
    r_text_box.send_keys(input("What do you want to send as a review?"))


    user_review_input = input("How many stars would you rate the book?")
    one = two = three = four = five = ''
    try:
        one = browser.find_element(By.XPATH, '//*[@id="form_review_4351956404"]/div/div[2]/div[1]/a[1]')
        two = browser.find_element(By.XPATH, '//*[@id="form_review_4351956404"]/div/div[2]/div[1]/a[2]')
        three = browser.find_element(By.XPATH, '//*[@id="form_review_4351956404"]/div/div[2]/div[1]/a[3]')
        four = browser.find_element(By.XPATH, '//*[@id="form_review_4351956404"]/div/div[2]/div[1]/a[4]')
        five = browser.find_element(By.XPATH, '//*[@id="form_review_4351956404"]/div/div[2]/div[1]/a[5]')
    except:
        print("Could not rate the book.")

    if user_review_input == '1':
        one.click()
    elif user_review_input == '2':
        two.click()
    elif user_review_input == '3':
        three.click()
    elif user_review_input == '4':
        four.click()
    elif user_review_input == '5':
        five.click()
    else:
        print("Can't rate the book with that rating.")


    time.sleep(1000)



#find_book("The Hobbit")
#create_review()
'''
def wish_list_del(temp):
    if len(temp) == 0:
        return
    s['Delete'] = temp
    print(s['Delete'])

def wish_list_add(temp):
    if len(temp) == 0:
        return
    s['Add'] = temp
    print(s['Add'])'''