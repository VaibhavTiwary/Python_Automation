from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

userProfileName = input("Enter insta username to download pic :- ")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

input

try:
    driver.get("https://www.instagram.com/" + userProfileName + "/")
    # driver.get("hhttps://www.instagram.com/vaibhav_tiwary_/")

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt*='profile picture']"))
    )

    time.sleep(5)

    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")

    print(page[:2000])

    user_image_tag = soup.find(
        "img", {"alt": f"{userProfileName}'s profile picture", "src": True}
    )

    if user_image_tag:
        image_url = user_image_tag["src"]
        print("Image URL:", image_url)

        urllib.request.urlretrieve(image_url, "profile.jpg")
        print("Profile picture downloaded successfully.")
    # else:
    #     print("Profile picture not found.")
    if not user_image_tag:
        user_image_tag = soup.select(
            ".xz74otr x972fbf xcfux6l x1qhh985 xm0m39n x5yr21d x10l6tqk x17qophe x13vifvy x11njtxf xh8yej3"
        )

finally:
    driver.quit()
