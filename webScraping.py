from selenium import webdriver
from bs4 import BeautifulSoup
import time, csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
browser = webdriver.Chrome("./chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ['Name', 'Radius', 'Mass', 'Distance']
    incoming_data = []

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    stars_tables = soup.find_all('table')
    data_table = stars_tables[7].find_all('tr')

    index = 0

    for tr_tag in data_table:

        table_data = tr_tag.find_all('td')

        row = [i.text.rstrip() for i in table_data]
        if index == 0:
            index += 1
        elif index >= 1:
            final_row = [row[0], row[8], row[7], row[5]]
            incoming_data.append(final_row)

    with open('data.csv', 'w', encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(incoming_data)

scrape()