from selenium.webdriver import Firefox, FirefoxProfile
import time, random

username = input("Enter your username: ")
password = input("Enter your password: ")

# Initialize driver
profile = FirefoxProfile('/home/dsrf/.mozilla/firefox/fgf9rqog.selenium')
driver = Firefox(profile)
driver.implicitly_wait(5)

# Load the website
driver.get("https://www.tribalwars.co.uk/")

# Login
textbox_username = driver.find_element_by_xpath("//input[@name='username']")
textbox_username.send_keys(username)

textbox_password = driver.find_element_by_xpath("//input[@name='password']")
textbox_password.send_keys(password)

driver.find_element_by_xpath("//a[@class='btn-login']").click()
time.sleep(5)
# Enter World 49
driver.find_element_by_xpath("//span[@class='world_button_active' and text()='World 49']").click()
time.sleep(5)

while True:
    driver.get("https://uk49.tribalwars.co.uk/game.php?village=11304&screen=place&mode=scavenge")
    time.sleep(10 + random.randint(0,15))
