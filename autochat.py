import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

chromedriver="insert path to selenium chrome driver "

browser = webdriver.Chrome(chromedriver)

browser.get("http://www.facebook.com")

time.sleep(3)

elem = browser.find_element_by_name('email')

time.sleep(1)

elem.send_keys('insert your faebook username ')

elem = browser.find_element_by_name('pass')

elem.send_keys('insert your facebook password')

login_attempt=browser.find_element_by_xpath("//*[@type='submit']")

login_attempt.submit()

time.sleep(25)

openchatsidebar=browser.find_element_by_xpath("//div[contains(@class,'uiToggle _50-v fbNub _4mq3 hide_on_presence_error')]")
 
if(!openchatsidebar)
{
openchatsidebar.click()
time.sleep(1)
}

openchatbox = browser.find_element_by_xpath("//div[contains(@class,'_55lr')and text()='Tanmay Bangale']")

time.sleep(5)

openchatbox.click()

time.sleep(3)

entermessage=browser.find_element_by_xpath("//textarea[contains(@title,'Type a message...')]")

time.sleep(3)

entermessage.send_keys("Hi.!")

time.sleep(1)

entermessage.send_keys(Keys.RETURN)

while not recieve :
time.sleep(5)

entermessage.send_keys("How are you ?"+Keys.RETURN)

time.sleep(5)

entermessage.send_keys("Hope you are doing very well.!"+Keys.RETURN)
 
