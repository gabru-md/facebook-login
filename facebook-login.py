from selenium import webdriver

def test(username, pass1):
	browser=webdriver.PhantomJS() # this will be the path to your webbrowser's WEBDRIVER
	browser.get('http://facebook.com')
	time.sleep(10)
	#user credentials
	lst = browser.find_element_by_css_selector('#lst-ib')
	print "Done"

print "starting"
test()
print "idk"
