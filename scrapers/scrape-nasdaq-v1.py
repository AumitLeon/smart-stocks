"""Will print the fiscal data as published by the nasdaq"""
# Need to implement error handling. 
# Initial commit -- needs changes and expansion
from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://www.nasdaq.com/symbol/td/earnings-forecast').read()

#Set the directories according to where you download this script. Make sure the text files are created
#in the same directory. 
f = open('C:\Users\Aumit\Documents\GitHub\midd-books\scrapers\data.txt', 'w')
e = open('C:\Users\Aumit\Documents\GitHub\midd-books\scrapers\errors.txt', 'w')
soup = BeautifulSoup(r, "lxml")

temp = soup.find("div", {"class" : "genTable"}).find('table')
f.write("Fiscal Year ------------------- High EPS"+'\n')


x = 0

tableStats = temp
while (x < 3):
	for row in tableStats.find_all('tr')[1:]:
		col = row.find_all('td')
		fiscalYear = col[0].string.encode('ascii', 'ignore')
		highEPSForecast = col[2].string.encode('ascii', 'ignore')
		f.write(fiscalYear+"-------------------"+highEPSForecast+'\n')
		x = x + 1
f.close
e.close
