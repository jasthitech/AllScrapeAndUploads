from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import time

# Set up Chrome options
chrome_options = Options()
ua = UserAgent()
user_agent = ua.random
print(user_agent)
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.headless = False  # Set to True for headless mode (no GUI)

try:
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to a Facebook page
    url = "https://www.facebook.com/"
    driver.get(url)

    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "pass")
    login_button = driver.find_element(By.NAME, "login")

    # Enter your credentials
    email_field.send_keys("rathnagiri47@gmail.com")
    password_field.send_keys("Test123t1t2t3")

    # Click the login button
    login_button.click()

    # Navigate to a Facebook page
    url = "https://www.facebook.com/profile.php?id=100065130643111"
    driver.get(url)
    time.sleep(15)  # Wait for the page to load (adjust as needed)

    # Initialize last_scroll_position before the loop
    last_scroll_position = 0

    # Function to scroll down to the bottom of the page
    def scroll_to_bottom(driver):
        while True:
            # Get the initial page height
            initial_height = driver.execute_script("return document.body.scrollHeight")
            # Scroll down to the bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)  # Wait for the page to load (adjust as needed)

            # Capture the HAR file
            # You can use browser developer tools to capture HAR and save it here

            # Get the new page height
            new_height = driver.execute_script("return document.body.scrollHeight")

            # Check if we have reached the end of the page
            if new_height == initial_height:
                break

    # Call the scroll_to_bottom function
    scroll_to_bottom(driver)
    time.sleep(10)  # Wait for the page to load (adjust as needed)

    # Open the DevTools panel
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F12)

    # Wait for some time to ensure developer tools open (you can adjust the wait time)
    time.sleep(10)

    # Wait for the DevTools panel to open
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.export-button")))

    # Click the button to save HAR file
    driver.find_element(By.CSS_SELECTOR, "button.export-button").click()

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Ensure the WebDriver is properly closed, even in case of an exception
    driver.quit()
