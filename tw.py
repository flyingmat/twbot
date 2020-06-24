from selenium.webdriver import Firefox, FirefoxProfile
import time, random

# Scavenge with optimal amounts of spears
def scavenge(driver):
    driver.get("https://uk49.tribalwars.co.uk/game.php?village=11304&screen=place&mode=scavenge")
    print("Scavenging page loaded! Waiting...")

    spear_amount = int(driver.find_element_by_xpath("//a[@class='units-entry-all squad-village-required' and @data-unit='spear']").text[1:-1])
    print("You have {} spears.".format(spear_amount))

    time.sleep(10 + random.randint(0,15)) # EVASION 100

    lvl3 = int(spear_amount / 8)
    lvl2 = 2 * lvl3

    textbox_spears = driver.find_element_by_xpath("//input[@name='spear']")

    print("Sending {} spears for LVL3!".format(lvl3))
    textbox_spears.send_keys(str(lvl3))
    time.sleep(1 + random.randint(0,5))
    # TODO: Click the LVL3 scavenge button

    time.sleep(5 + random.randint(0,5))

    print("Sending {} spears for LVL2!".format(lvl2))
    textbox_spears.send_keys(str(lvl2))
    time.sleep(1 + random.randint(0,5))
    # TODO: Click the LVL2 scavenge button

    time.sleep(5 + random.randint(0,5))

    # Fill the remaining spears
    print("Sending all other spears for LVL1!")
    driver.find_element_by_xpath("//a[@class='units-entry-all squad-village-required' and @data-unit='spear']").click()
    time.sleep(1 + random.randint(0,5))
    # TODO: Click the LVL1 scavenge button

# Recruit the maximum amount of spears possible
def recruit(driver):
    driver.get("https://uk49.tribalwars.co.uk/game.php?village=11304&screen=barracks")
    print("Barracks page loaded! Waiting...")

    time.sleep(10 + random.randint(0,15)) # EVASION 100

    # Recruit max amount of spears possible
    driver.find_element_by_xpath("//a[@id='spear_0_a']").click()
    time.sleep(1 + random.randint(0,5))
    driver.find_element_by_xpath("//input[@class='btn btn-recruit']").click()

# Upgrade a building to the next level
def upgrade(driver, building):
    driver.get("https://uk49.tribalwars.co.uk/game.php?village=11304&screen=main")

    time.sleep(5 + random.randint(0,5))

    building_row = driver.find_element_by_xpath("//tr[@id='main_buildrow_{}']".format(building))
    button_build = row.find_element_by_xpath("//a[@class='btn btn-build']")

    if button_build.get_attribute("style") != "display:none":
        button_build.click()
        return True
    else:
        return False

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
    # Scavenge first
    scavenge(driver)
    time.sleep(5 + random.randint(0, 10))

    # If farm doesn't need upgrading
    if int(driver.find_element_by_xpath("//span[@id='pop_max_label'")) - int(driver.find_element_by_xpath("//span['id='pop_current_label]")) >= 50:
        # Recruit more spears
        recruit(driver)
    else:
        # Upgrade farm
        upgrade(driver, "farm")
