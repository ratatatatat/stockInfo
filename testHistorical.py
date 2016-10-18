from historicalGen import HistoricalData

upperYear = 2012
upperMonth = 3
upperDay = 11

lowerMonth = 5
lowerYear = 2011
lowerDay = 21
symbol = 'aapl'
newData = HistoricalData(upperYear,upperMonth,upperDay,lowerMonth,lowerDay,lowerYear,symbol)

newDataArray = newData.getData()
print newDataArray