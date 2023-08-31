import urllib.request

def downloadData(url):
    with urllib.request.urlopen(url) as response:
      csv_data = response.read().decode('utf-8')

      return csv_data


#checking if it works
#url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"
#downloadedData = downloadData(url)
#print(downloadedData)

import logging

LOG_FILENAME = 'errors.log'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('assignment2')
my_logger.setLevel(logging.ERROR)