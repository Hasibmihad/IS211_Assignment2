import urllib.request
import logging
from datetime import datetime

def loggerSetup():
    LOG_FILENAME = 'errors.log'
    my_logger = logging.getLogger('assignment2')
    my_logger.setLevel(logging.ERROR)
    return my_logger

def downloadData(url,my_logger):
    with urllib.request.urlopen(url) as response:
      csv_data = response.read().decode('utf-8')

      return csv_data


def processData(data,my_logger):
    data2 = data.split('\n') #split upon new line for processing
    personData={}
    for i in range (1,len(data2)-1):
        each_data = data2[i].split(',')
        ID=each_data[0]
        name=each_data[1]
        stringbirthday =each_data[2]
    #print(ID)
    #print(name)
        try:
            birthday = datetime.strptime(stringbirthday, '%d/%m/%Y').date()
            personData[int(ID)] = (name, birthday)
        except ValueError:
            my_logger.error(f"Error processing line #{i+1} for ID #{ID} - Invalid date: {stringbirthday}")
    return personData

def main() :
    #logger
    logger=loggerSetup
   
    url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"
    downloadedData = downloadData(url,logger)
    #print(downloadedData)

    personData=processData(downloadedData,logger)
    print(personData)
if __name__ == "__main__":

    main() 


