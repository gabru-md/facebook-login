from selenium import webdriver
import time

def test():
	browser=webdriver.PhantomJS() # this will be the path to your webbrowser's WEBDRIVER
	browser.get('https://google.co.in')
	time.sleep(10)
	#user credentials
	#lst = browser.find_element_by_css_selector('#lst-ib')
	print "Done"

print "starting"
test()
print "idk"
