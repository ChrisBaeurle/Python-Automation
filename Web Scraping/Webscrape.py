# Web scraping in Firefox using selenium, pandas

from selenium import webdriver
import pandas as pd

website = "https://www.thesun.co.uk/sport/football"
path = "C:\\Users\\Chris\\PycharmProjects\\geckodriver.exe"

driver = webdriver.Firefox(executable_path="C:\\Users\\Chris\\PycharmProjects\\geckodriver.exe")

driver.get(website)
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]') #.find_element() only returns first element

# append each element below to lists
titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/h3').text # website title
    subtitle = container.find_element(by="xpath", value='./a/p').text # website subtitle
    link = container.find_element(by="xpath", value='./a').get_attribute("href")  # website link (typically href)
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title':titles, 'subtitle':subtitles, 'link':links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv')

driver.quit()