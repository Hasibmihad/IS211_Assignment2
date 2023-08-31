import urllib.request
import logging
from datetime import datetime
import sys
import argparse


def loggerSetup():
    logging.basicConfig(filename="errors.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 
    logger=logging.getLogger("assignment2") 
    logger.setLevel(logging.ERROR) 
    return logger



def downloadData(url,my_logger):
  try:
    with urllib.request.urlopen(url) as response:
      csv_data = response.read().decode('utf-8')
  except ValueError:
      my_logger.error("URL IS INVALID")
      return csv_data



def processData(data,my_logger):
    data2 = data.split('\n') #split upon new line for processing
    personData={}
    for i in range (1,len(data2)-1):
        each_data = data2[i].split(',')
        ID=each_data[0]
        name=each_data[1]
        stringbirthday =each_data[2]

        try:
            birthday = datetime.strptime(stringbirthday, '%d/%m/%Y').date()
            personData[int(ID)] = (name, birthday)
        except ValueError:
            my_logger.error(f"Error processing line #{i+1} for ID #{ID}")
    return personData


def displayPerson(id,personData):
    if id in personData:
        print (f"Person #{id} is {personData[id][0]} with a birthday of {personData[id][1].strftime('%Y-%m-%d')}")
    else :
        print ("No user found with that id")





def main(url) :

    logger=loggerSetup()

   # url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"
    downloadedData = downloadData(url,logger)


    personData=processData(downloadedData,logger)

    

    while True:
        print ("Please enter an ID to look up:")
        input_id=int(input())
        if input_id <= 0:
            print("Exiting the program.")
            sys.exit()
        else:
            displayPerson(input_id, personData)
    






if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, help="URL parameter without any double quotation")
    args = parser.parse_args()
    if args.url:
           main(args.url)
    else:
        print("URL Invalid. Exiting the program.")
        sys.exit()


