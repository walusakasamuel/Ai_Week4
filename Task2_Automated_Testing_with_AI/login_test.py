from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

chrome_options = Options()
# Commented out headless so browser is visible
# chrome_options.add_argument('--headless')  
service = Service()

def test_login(url, username, password, expect_success=True, screenshot_dir="screenshots", pause_before_quit=5):
    # Create screenshot directory if it doesn't exist
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get(url)
        driver.find_element(By.ID, 'username').send_keys(username)
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(1)
        success = "You logged into a secure area!" in driver.page_source

        if success != expect_success:
            screenshot_path = os.path.join(screenshot_dir, f"{username}_{password}.png")
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")

        assert success == expect_success
        print(f"Test {'passed' if success else 'failed'} for {username}")

        # Pause so you can take screenshots manually
        print(f"Browser will stay open for {pause_before_quit} seconds...")
        time.sleep(pause_before_quit)

        return success
    finally:
        driver.quit()

if __name__ == '__main__':
    url = 'https://the-internet.herokuapp.com/login'

    # Pause 10 seconds for the first test to take screenshots
    print('Valid credentials:', test_login(url, 'tomsmith', 'SuperSecretPassword!', True, pause_before_quit=10))
    
    # Pause 10 seconds for the second test to take screenshots
    print('Invalid credentials:', test_login(url, 'tomsmith', 'wrongpass', False, pause_before_quit=10))
