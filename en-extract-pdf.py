from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
# MMDDYYYY
month_day_year = now.strftime("%m%d%Y")


website = "https://www.thesun.co.uk/sport/football/"
path = "C:/Users/vipul/Downloads/chromedriver-win64/chromedriver.exe"

# Chrome options to ignore SSL errors
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service, options=chrome_options)
driver.get(website)

# Use WebDriverWait to wait until the elements are present
wait = WebDriverWait(driver, 10)
containers = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="teaser__copy-container"]')))

titles = []
subtitles = []
links = []

for container in containers:
    try:
        title_element = container.find_element(by='xpath', value='./a/span')
        subtitle_element = container.find_element(by='xpath', value='./a/h3')
        link_element = container.find_element(by='xpath', value='./a')

        title = title_element.text if title_element else 'No Title'
        subtitle = subtitle_element.text if subtitle_element else 'No Subtitle'
        link = link_element.get_attribute('href') if link_element else 'No Link'

        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)

    except Exception as e:
        print(f"Error processing container: {e}")

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'headline-{month_day_year}.csv'

final_path = os.path.join(application_path, file_name)

df_headlines.to_csv(final_path)

driver.quit()
