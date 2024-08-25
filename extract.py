from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "C:/Users/vipul/Downloads/chromedriver-win64/chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

wait = WebDriverWait(driver, 10)

containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')

titles = driver.find_elements(By.XPATH, '//div[@class="teaser__copy-container"]/a/span/text()')

# //div[@class="teaser__copy-container"]

print(len(titles))

for i in titles:
    print(i)

# titles = []
# subtitles = []
# links = []

# for container in containers:
#     title = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a/span').text
#     subtitle = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a/h3').text
#     link = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a').get_dom_attribute("href")

#     titles.append(title)
#     subtitles.append(subtitle)
#     links.append(link)
# # //div[@class="teaser__copy-container"]/a/span
# # //div[@class="teaser__copy-container"]/a/h3

# my_dict = {'titles': titles, 'subtitles': subtitles, 'links': links}

# df_headlines = pd.DataFrame(my_dict)
# df_headlines.to_csv('headline.csv')

driver.quit()

