from selenium import webdriver
from threading import Thread
import time


global username
global pass1

def fb_login(username, pass1):
	browser=webdriver.PhantomJS() # this will be the path to your webbrowser's WEBDRIVER
	browser.get('http://facebook.com')
	time.sleep(10)
	#user credentials
	user = browser.find_element_by_css_selector('#email')
	user.send_keys(str(username))
	password = browser.find_element_by_css_selector('#pass')
	password.send_keys(str(pass1))
	login = browser.find_element_by_css_selector('#loginbutton')
	login.click()
	print "Done"




username = "1234"
pass1 = "1234"

t1 = Thread(target=fb_login(username,pass1))

#fb_login(user_name, pass_word)

t1.start()


