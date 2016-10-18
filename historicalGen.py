import csv
import sys
import urllib2
sys.path.append('/home/rajiv/AnonCrawl/anonRequestPY')
from anonRequest import AnonRequest

reqObj = AnonRequest()
url = 'http://winterolympicsmedals.com/medals.csv'
response = reqObj.getDownloadCsv(url)
# response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
	print row