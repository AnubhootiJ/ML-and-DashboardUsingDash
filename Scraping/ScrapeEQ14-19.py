from bs4 import BeautifulSoup  # to parse the website
import requests  # to gaccess the webpage
import csv

csv_file = open('Earthquake14-19.csv', 'w', newline='')  # opening the CSV files
csv_write = csv.writer(csv_file)
csv_write.writerow(['Date', 'Time(UTC)', 'Time(IST)', 'Lat', 'Lang', 'Depth(KM)', 'Magnitude', 'Region'])  # writing the headers

years = ['2014', '2015', '2016', '2017']  # year list for URLs
for year in years:
    URL = "http://www.imd.gov.in/pages/lyear1.php?year=" + year
    # print(URL)
    result = requests.get(URL)
    src = result.content  # storing the contents of the website into variable src
    soup = BeautifulSoup(src, 'lxml')  # creating object to parse the website
    # print(soup.prettify())

    list = []

    for see in soup.findAll('font'):
        see.replaceWithChildren()

    for row in soup.find_all('tr'):
        for data in row.find_all('b'):
            data = data.text
            list.append(data.strip())
        csv_write.writerow(list)
        list = []

years = ['2018', '2019']
for year in years:
    URL = "http://www.imd.gov.in/pages/lyear2.php?year=" + year
    result = requests.get(URL)
    src = result.content  # storing the contents of the website into variable src
    soup = BeautifulSoup(src, 'lxml')  # creating object to parse the website
    # print(soup.prettify())

    list = []

    for see in soup.findAll('font'):
        see.replaceWithChildren()

    for row in soup.find_all('tr'):
        for data in row.find_all('b'):
            data = data.text
            list.append(data.strip())
        csv_write.writerow(list)
        list = []


csv_file.close()





