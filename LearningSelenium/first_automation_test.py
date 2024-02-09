import time
from selenium import webdriver
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest

with open('data1.yaml', 'r') as f:
    contents = yaml.load(f, Loader=yaml.FullLoader)
    username = (contents['USERNAMES_LIST'])
    password = (contents['PASSWORDS_LIST'])
    first_name = (contents['FIRST_NAME_LIST'])
    last_name = (contents['LAST_NAME_LIST'])
    company = (contents['COMPANIES'])
    address = (contents['ADDRESS'])
    phone = (contents['PHONE'])
    city = (contents['CITY'])
    state = (contents['STATE'])
    zip_code = (contents['ZIP_CODE'])
    state_name = (contents['STATE_NAMES'])


    print(address[4])
    # print(username[4])
    # print(password[4])
    # print(first_name[4])
    # print(last_name[4])


    def test_online_shopping_site_login_and_browse():
        for i in range(len(username)):
            driver = webdriver.Firefox()
            driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")
            driver.find_element(By.XPATH, "//input[@id='email']").send_keys(username[i])
            time.sleep(4)
            driver.find_element(By.XPATH, "//input[@title='Password']").send_keys(password[i])
            time.sleep(4)
            driver.find_element(By.XPATH, "//button[@class='action login primary']").click()
            time.sleep(8)
            welcome_text = driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[1]/span").text
            # print(welcome_text)
            assert welcome_text == "Welcome, " + first_name[i] + " " + last_name[i] + "!"
            driver.find_element(By.XPATH,"//span[normalize-space()='Men']").click()
            time.sleep(4)
            driver.find_element(By.XPATH,"//li[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]").click()
            time.sleep(4)
            driver.find_element(By.XPATH, "//li[1]//div[1]//div[1]//div[2]//div[2]//div[1]//div[1]").click()
            time.sleep(4)
            driver.find_element(By.XPATH, "//li[1]//div[1]//div[1]//div[3]//div[1]//div[1]//form[1]//button[1]//span[1]").click()
            time.sleep(2)
            print("Order Added to Cart!!!!")
            driver.close()

    def test_fill_address_details():
        for i in range(len(username)):
            driver = webdriver.Firefox()
            driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")
            time.sleep(4)
            driver.find_element(By.XPATH, "//input[@id='email']").send_keys(username[i])
            time.sleep(4)
            driver.find_element(By.XPATH, "//input[@title='Password']").send_keys(password[i])
            time.sleep(4)
            driver.find_element(By.XPATH, "//button[@class='action login primary']").click()
            time.sleep(4)
            driver.find_element(By.XPATH, "//a[@class='action showcart']").click()
            time.sleep(4)
            driver.find_element(By.XPATH, "//button[@id='top-cart-btn-checkout']").click()
            time.sleep(20)
            driver.find_element(By.XPATH, "//span[normalize-space()='New Address']").click()
            time.sleep(4)
            driver.find_element(By.XPATH, "//input[@name='company']").send_keys(company[i])
            time.sleep(4)
            driver.find_element(By.XPATH, "//div[@class='control']//div[@class='field _required']//div[@class='control']//input[@type='text']").send_keys(address[i])
            time.sleep(4)
            driver.find_element(By.XPATH, "//input[@name='city']").send_keys(city[i])
            time.sleep(4)
            driver.find_element(By.XPATH, "//input[@name='postcode']").send_keys(zip_code[i])
            time.sleep(4)
            select_element2 = driver.find_element(By.XPATH, "//select[@name='country_id']")
            select1 = Select(select_element2)
            select1.select_by_value('IN')
            time.sleep(4)
            select_element1 = driver.find_element(By.XPATH, "//select[@name='region_id']")
            select = Select(select_element1)
            select.select_by_value(state[i])
            time.sleep(4)
            driver.find_element(By.XPATH, "//input[contains(@type,'checkbox')]").click()
            time.sleep(4)
            driver.find_element(By.XPATH, "//input[contains(@type,'checkbox')]").click()
            time.sleep(4)
            driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys(phone[i])
            time.sleep(4)
            driver.find_element(By.XPATH,"//span[normalize-space()='Ship here']").click()
            time.sleep(8)
            driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
            time.sleep(8)
            driver.find_element(By.XPATH, "//span[normalize-space()='Place Order']").click()
            time.sleep(8)
            assert driver.find_element(By.XPATH, "//span[normalize-space()='Continue Shopping']").is_displayed()
            print("Order Placed!!!!")
            driver.close()



    def test_check_all_details():
        for i in range(len(username)):
            driver = webdriver.Firefox()
            driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")
            time.sleep(4)
            driver.find_element(By.XPATH, "//input[@id='email']").send_keys(username[i])
            time.sleep(4)
            driver.find_element(By.XPATH, "//input[@title='Password']").send_keys(password[i])
            time.sleep(4)
            driver.find_element(By.XPATH, "//button[@class='action login primary']").click()
            time.sleep(4)
            driver.find_element(By.XPATH,"//div[@class='panel header']//button[@type='button']").click()
            time.sleep(4)
            driver.find_element(By.XPATH,"//div[@aria-hidden='false']//a[normalize-space()='My Account']").click()
            time.sleep(4)
            driver.find_element(By.XPATH, "//div[@class='box box-billing-address']//span[contains(text(),'Edit Address')]").click()
            time.sleep(4)
            fname = driver.find_element(By.XPATH, "//input[@title='First Name']").get_attribute("value")
            assert fname == first_name[i]
            time.sleep(4)
            lname = driver.find_element(By.XPATH, "//input[@title='Last Name']").get_attribute("value")
            assert lname == last_name[i]
            time.sleep(20)
            comp = driver.find_element(By.XPATH, "//input[@title='Company']").get_attribute("value")
            assert comp == company[i]
            address1 = driver.find_element(By.XPATH, "//input[@title='Street Address']").get_attribute("value")
            assert address1 == address[i]
            city1 = driver.find_element(By.XPATH, "//input[@title='City']").get_attribute("value")
            assert city1 == city[i]
            zip_code1 = driver.find_element(By.XPATH, "//input[@title='Zip/Postal Code']").get_attribute("value")
            assert zip_code1 == zip_code[i]
            phone1 = driver.find_element(By.XPATH, "//input[@title='Phone Number']").get_attribute("value")
            assert phone1 == phone[i]
            time.sleep(4)
            select_element1 = driver.find_element(By.XPATH, "//select[@name='region_id']")
            select = Select(select_element1)
            state1 = select.first_selected_option.text
            print(state1)
            assert state1 == state_name[i]
            time.sleep(4)
            select_element2 = driver.find_element(By.XPATH, "//select[@name='country_id']")
            select1 = Select(select_element2)
            country1 = select1.first_selected_option.text
            assert country1 == 'India'
            time.sleep(4)
            print("All details successfully verified for user ",username[i],"!!!!")
            print("Testing completed")
            driver.close()



