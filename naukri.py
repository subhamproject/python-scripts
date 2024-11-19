
#######################################

export NAUKRI_EMAIL="your_email@example.com"
export NAUKRI_PASSWORD="your_password"
python naukri_upload.py --resume "C:/path/to/resume.pdf" --headless

python naukri_upload.py --email "your_email@example.com" --password "your_password" --resume "C:/path/to/resume.pdf" --headless


#######################################

#/usr/bin/python
import os
import logging
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def login_to_naukri(driver, email, password):
    """
    Logs in to Naukri using provided credentials.
    """
    logging.info("Navigating to login page...")
    driver.get('https://www.naukri.com/nlogin/login')
    wait = WebDriverWait(driver, 20)

    try:
        email_field = wait.until(EC.presence_of_element_located((By.ID, 'usernameField')))
        email_field.send_keys(email)
        logging.info("Email entered successfully.")
    except Exception as e:
        logging.error(f"Error locating email field: {e}")
        return False

    try:
        password_field = wait.until(EC.presence_of_element_located((By.ID, 'passwordField')))
        password_field.send_keys(password)
        logging.info("Password entered successfully.")
    except Exception as e:
        logging.error(f"Error locating password field: {e}")
        return False

    try:
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        login_button.click()
        logging.info("Login button clicked.")
    except Exception as e:
        logging.error(f"Error locating login button: {e}")
        return False

    # Verify login success
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'root')))
        logging.info("Login successful!")
        return True
    except Exception as e:
        logging.error("Login failed, please check credentials or page structure.")
        return False

def upload_resume(driver, resume_path):
    """
    Uploads the resume to the Naukri profile page.
    """
    logging.info("Navigating to profile page...")
    driver.get('https://www.naukri.com/mnjuser/profile')
    wait = WebDriverWait(driver, 20)

    try:
        upload_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
        upload_button.send_keys(resume_path)
        logging.info("Resume uploaded successfully.")
    except Exception as e:
        logging.error(f"Error locating upload button: {e}")
        return False

    return True

def main(email, password, resume_path, headless):
    """
    Main function to execute the script.
    """
    # Configure WebDriver
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        if login_to_naukri(driver, email, password):
            if not upload_resume(driver, resume_path):
                logging.error("Failed to upload resume.")
        else:
            logging.error("Login failed. Exiting script.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()
        logging.info("WebDriver session ended.")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Automate Naukri login and resume upload.')
    parser.add_argument('--email', required=True, help='Your Naukri login email')
    parser.add_argument('--password', required=True, help='Your Naukri login password')
    parser.add_argument('--resume', required=True, help='Full path to the resume file')
    parser.add_argument('--headless', action='store_true', help='Run the browser in headless mode')
    args = parser.parse_args()

    # Run the main function
    main(email=args.email, password=args.password, resume_path=args.resume, headless=args.headless)
