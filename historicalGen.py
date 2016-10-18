import csv
import sys
import urllib2
sys.path.append('/home/rajiv/AnonCrawl/anonRequestPY')
from anonRequest import AnonRequest


class HistoricalData:
	def __init__(self,upperYear,upperMonth,upperDay,lowerMonth,lowerDay,lowerYear,symbol):
		source = 'yahoo'
		self.reqObj = AnonRequest()
		self.tickerData = self.getDataArray(upperYear,upperMonth,upperDay,lowerMonth,lowerDay,lowerYear,symbol,'yahoo')

	def getDataArray(self,upperYear,upperMonth,upperDay,lowerMonth,lowerDay,lowerYear,symbol,source):
			if(source == 'yahoo'):		
				self.tickerData = self.getYahooData(upperYear,upperMonth,upperDay,lowerMonth,lowerDay,lowerYear,symbol)
				return self.tickerData
	def getData(self):
			source = 'yahoo'
			if (source == 'yahoo'):
				self.ticObjArray = self.processData(self.tickerData)
				return self.ticObjArray
			else:
				return {}


	def getYahooData(self,upperYear,upperMonth,upperDay,lowerMonth,lowerDay,lowerYear,symbol):
			upperMonth = upperMonth -1
			upperMonth = str(upperMonth)
			upperDay = str(upperDay)
			upperYear = str(upperYear)
			lowerMonth = lowerMonth - 1
			lowerMonth = str(lowerMonth)
			lowerDay = str(lowerDay)
			lowerYear = str(lowerYear)
			print type(symbol)
			print "upperMonth",upperMonth
			print "upperDay", upperDay
			print "upperYear",upperYear
			print "lowerMonth",lowerMonth
			print "lowerYear", lowerYear
			print "lowerDay", lowerDay
			print "symbol",symbol
			url = 'http://ichart.finance.yahoo.com/table.csv?d='+upperMonth+'&e='+upperDay+'&f='+upperYear+'&g=d&a='+lowerMonth+'&b='+lowerDay+'&c='+lowerYear+'&ignore=.csv&s='+symbol
			response = self.reqObj.getDownloadCsv(url)
			cr = csv.reader(response)
			return cr

	def processData(self,csvArray):
		# Designed to handle yahoo output
		i = 0
		objDummy = {}
		objArray = []
		keyArray = []
		for row in csvArray:
		    if(i == 0):
		        keyArray = row
		        i=i+1
		        continue
		    else:
		        for key,value in zip(keyArray,row):
		            objDummy[key] = value
		        objArray.append(objDummy)
		    i = i+1
		return objArray
        
