from bs4 import BeautifulSoup  # to parse the website
import requests  # to gaccess the webpage
import csv

result = requests.get("http://www.imd.gov.in/pages/lyear1.php?year=2015")
src = result.content  # storing the contents of the website into variable src
soup = BeautifulSoup(src, 'lxml')  # creating object to parse the website

csv_file = open('Earthquake.csv','w',newline='')
csv_write = csv.writer(csv_file)
csv_write.writerow(['Date','Time(UTC)','Time(IST)','Lat', 'Lang','Depth(KM)','Magnitude','Region'])
# print(soup.prettify())
list = []

for see in soup.findAll('font'):
    see.replaceWithChildren()

for row in soup.find_all('tr'):
    for data in row.find_all('b'):
        data = data.text
        list.append(data.strip())
    csv_write.writerow(list)
    list=[]







