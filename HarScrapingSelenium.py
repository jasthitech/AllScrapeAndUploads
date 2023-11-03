from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fake_useragent import UserAgent
import time
import logging



logging.basicConfig(level=logging.DEBUG)

# Set up Firefox options 
firefox_options = Options()
ua = UserAgent()
user_agent = ua.random
print(user_agent)
firefox_options.add_argument(f'--user-agent={user_agent}')
firefox_options.headless = False  # Set to True for headless mode (no GUI)
firefox_options.binary = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
firefox_options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

try:
    
    driver = webdriver.Firefox(options=firefox_options)

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


            # Get the new page height
            new_height = driver.execute_script("return document.body.scrollHeight")

            # Check if we have reached the end of the page
            if new_height == initial_height:
                break

    # Call the scroll_to_bottom function
    scroll_to_bottom(driver)
    time.sleep(10)  # Wait for the page to load (adjust as needed)

    # # Open the HAR panel in the developer tools
    # driver.execute_script("UI.inspectorView.showPanel('har');")

    # # Wait for some time to ensure the HAR panel is open (you can adjust the wait time)
    # time.sleep(10)

    # # Trigger the export of the HAR file
    # driver.execute_script("HAR.triggerExport();")

    # ... (your existing code)

    # Trigger the export of the HAR file and save it to disk
    # Replace "test" with your content API token
    # Replace "my_har_file.har" with the desired file name
    js_code = """
    var options = {
        token: "test",
        getData: true,
    };

    HAR.triggerExport(options).then(result => {
    // Save the HAR data to a file
    var blob = new Blob([result.data], { type: 'application/json' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = "my_har_file.har"; // Set the desired file name here
    a.style.display = 'none';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    });
    """

    # Execute the JavaScript code within the page
    driver.execute_script(js_code)

     # ... (rest of your code)



except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Ensure the WebDriver is properly closed, even in case of an exception
    driver.quit()
