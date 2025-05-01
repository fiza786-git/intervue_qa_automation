#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Automated QA Test Script for intervue.io
Description: Automates navigation, login, search, and logout on intervue.io using Selenium.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def login(driver, wait):
    """Performs login on the site"""
    driver.find_element(By.NAME, "email").send_keys("neha@intervue.io")
    driver.find_element(By.NAME, "password").send_keys("Ps@neha@123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

def navigate_main_menu(driver, wait, actions):
    """Navigates through the top menu bar in correct order with appropriate interactions."""
    
    # Step 1: Products (Click)
    products = wait.until(EC.element_to_be_clickable((By.ID, "products")))
    products.click()
    time.sleep(1)

    # Step 2: Solutions (Click)
    solutions = wait.until(EC.element_to_be_clickable((By.ID, "solutions")))
    solutions.click()
    time.sleep(1)

    # Step 3: Pricing (Hover only)
    pricing = wait.until(EC.presence_of_element_located((By.ID, "pricing")))
    actions.move_to_element(pricing).perform()
    time.sleep(1)

    # Step 4: Resources (Click)
    resources = wait.until(EC.element_to_be_clickable((By.ID, "resources")))
    resources.click()
    time.sleep(1)

    # Step 5: Contact Us (Hover only)
    contact_us = wait.until(EC.presence_of_element_located((By.ID, "contact-us")))
    actions.move_to_element(contact_us).perform()
    time.sleep(1)


def perform_search(driver, wait):
    """Clicks search icon, types 'hello', selects suggestion"""
    search_icon = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "HeaderSearch__SearchLensIconWrap-sc-1140h69-2")))
    search_icon.click()
    
    search_input = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".SearchBox__StyledInput-ctnsh0-4.lhwsuL")))
    search_input.send_keys("hello")
    
    dropdown_option = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".SearchThrough__PlaceholderText-sc-8f4vh4-0.fEvpzS")))
    dropdown_option.click()

def logout(driver, wait):
    """Logs out of the platform"""
    profile_icon = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".ant-dropdown-link.ProfileHeader__StyedDropdownHoverLink-sc-1gwp6c1-3.cwhrSp")))
    profile_icon.click()
    
    logout_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@href="/logout"]')))
    logout_btn.click()
    time.sleep(3)

def main():
    """Main execution flow"""
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    actions = ActionChains(driver)

    try:
        driver.get("https://www.intervue.io")
        time.sleep(2)

        navigate_main_menu(driver, wait, actions)

        # Click login button
        login_button = driver.find_element(By.XPATH, '//a[@class="ivhn-contact-link loginBtn"]')
        driver.execute_script("arguments[0].click();", login_button)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])

        second_login_btn = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "AccessAccount-ColoredButton")))
        driver.execute_script("arguments[0].click();", second_login_btn)

        login(driver, wait)
        perform_search(driver, wait)
        logout(driver, wait)

    except Exception as e:
        print(f"[ERROR] {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()


# In[ ]:




