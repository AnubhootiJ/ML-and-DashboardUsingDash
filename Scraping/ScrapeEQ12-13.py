from bs4 import BeautifulSoup  # to parse the website
import requests  # to gaccess the webpage
import csv

csv_file = open('Earthquake12-13.csv', 'w', newline='')  # opening the CSV files
csv_write = csv.writer(csv_file)
csv_write.writerow(['Date', 'Time', 'Lat', 'Lang', 'Depth(KM)', 'Magnitude', 'Region'])  # writing the headers

years = ['2012', '2013']  # year list for URLs
for year in years:
    URL = "http://www.imd.gov.in/pages/lyear.php?year=" + year
    result = requests.get(URL)
    src = result.content  # storing the contents of the website into variable src
    soup = BeautifulSoup(src, 'lxml')  # creating object to parse the website
    # print(soup.prettify())

    list = []

    for row in soup.find_all('tr'):
        for data in row.find_all('b'):
            data = data.text
            list.append(data.strip())
        csv_write.writerow(list)
        list = []

csv_file.close()





