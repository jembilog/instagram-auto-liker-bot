from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "your_username"
PASSWORD = "your_password"
HASHTAG = "coding"

driver = webdriver.Chrome()  # You can also use Firefox or Edge

def login():
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    user_input = driver.find_element(By.NAME, "username")
    pass_input = driver.find_element(By.NAME, "password")

    user_input.send_keys(USERNAME)
    pass_input.send_keys(PASSWORD)
    pass_input.send_keys(Keys.RETURN)
    time.sleep(5)

def like_posts():
    driver.get(f"https://www.instagram.com/explore/tags/{HASHTAG}/")
    time.sleep(5)
    
    links = driver.find_elements(By.TAG_NAME, 'a')
    post_links = [a.get_attribute('href') for a in links if '/p/' in a.get_attribute('href')]

    for link in post_links[:5]:  # like first 5 posts
        driver.get(link)
        time.sleep(2)
        try:
            like = driver.find_element(By.XPATH, '//span[@class="_aamw"]/div')
            like.click()
            print(f"❤️ Liked: {link}")
            time.sleep(3)
        except Exception as e:
            print(f"❌ Error: {e}")
            continue

if __name__ == "__main__":
    login()
    like_posts()
    driver.quit()
